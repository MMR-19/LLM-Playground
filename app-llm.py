# Libraries
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import litellm 
import os
import logging
import requests
from dotenv import load_dotenv
import webbrowser

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Enable debug mode
# litellm.return_response_headers = True
# litellm._turn_on_debug()

# start app with web sockets
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# available models
def get_available_models():

    # Load API key from environment variable
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY not found in environment variables")

    # Set API endpoint
    url = "https://openrouter.ai/api/v1/models"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Filter free models (you may need to adjust based on exact response format)
        free_models = []
        
        for model in data.get("data", []):
            pricing = model.get("pricing", {})

            # check if all pricing options are zero
            if all(val == '0' for val in pricing.values()):
                free_models.append(model["id"])

        # sort models alphabetically
        free_models.sort()

        return free_models

    except Exception as e:
        logging.error(f"Error fetching models: {str(e)}")
        return []

# index
@app.route("/")
def index():
    # fetch free models
    models = get_available_models()
    if not models:
        raise RuntimeError("No free models available or error fetching models.")
    
    return render_template("playground.html", models=models)

# send prompt
@socketio.on("send_prompt")
def handle_prompt(data):    
    system_prompt = data.get("system_prompt")
    user_prompt = data.get("user_prompt")
    model = data.get("model")

    if not user_prompt or not model:
        emit("error", {"error": "Prompt or model not provided"})
        return

    try:
        messages = [{"content": user_prompt, "role": "user"}]
        if system_prompt:
            messages.insert(0, {"content": system_prompt, "role": "system"})

        response = litellm.completion(
            response_format={ "type": "json_object" },
            model = f"openrouter/{model}:free",
            messages = messages,
            # stream = False,
            # temperature = 1,
            # top_p = 1
        )
    
        try:
            # Send response and rate limits to frontend
            result = response["choices"][0]["message"]["content"]
            emit("response", {"result": result, "response": response.json(), "params" : response._hidden_params})

        except Exception as e:
            emit("error", {"error": f"Error getting response from model... {str(e)}"})
        

    except Exception as e:
        emit("error", {"error": str(e)})


# get rate limits
@app.route("/rate_limits")
def get_rate_limits():
    
    # Load API key from environment variable
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY not found in environment variables")

    # Set API endpoint
    url = "https://openrouter.ai/api/v1/auth/key"
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        return jsonify(data.get("data", {}).get("rate_limit", {}))
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = 5000

    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        webbrowser.open("http://localhost:" + str(port))

    socketio.run(app, debug=True, host="0.0.0.0", port=port)