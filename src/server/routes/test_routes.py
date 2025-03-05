from flask import Blueprint, jsonify

from src.services.playwright.automate import read_jsonl, automate_actions
from src.services.socketio.socket import get_sio

test_bp = Blueprint('test', __name__)


@test_bp.route('/sio', methods=['GET'])
def test():
    data = {"message": "Hello, API! Sending message from Flask server."}
    sio = get_sio()
    sio.emit("agent", "hello from vicbot-pybot server")
    return jsonify(data)


@test_bp.route('/pw')
def test_pw():
    # Example usage
    # start_chromium()
    file_path = 'plays/teknixco.net/login.jsonl'
    actions = read_jsonl(file_path)
    automate_actions(actions)
    return jsonify("PW Action ran")
