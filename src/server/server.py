import os

from flask import Flask

from src.server.routes.agent_routes import agent_bp
from src.server.routes.api_routes import api_bp

app = Flask(__name__)
port = 5001

# Disable parallelism for huggingface/tokenizers
os.environ["TOKENIZERS_PARALLELISM"] = "false"


@app.route('/')
def home():
    return "Hello, Flask!"


def run_server():
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(agent_bp, url_prefix='/agent')

    app.run(debug=True, use_reloader=False, port=port)

    return app
