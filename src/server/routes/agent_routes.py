from flask import Blueprint, jsonify, request

from src.agents.agents import create_agent, agents

agent_bp = Blueprint('agent', __name__)


@agent_bp.route('/get', methods=['GET'])
def get_agents():
    print({"message": "Hello, API! Getting Agents."})
    data = {name: agent.to_dict() for name, agent in agents.items() if name != "default"}
    return jsonify(data)


@agent_bp.route('/create/<name>', methods=['GET'])
def create_agents(name):
    print({"message": "Hello, API! Creating New Agent."})
    agent = create_agent(name)
    data = {name: agent.to_dict()}
    return jsonify(data)


# Agent Actions
@agent_bp.route('/ask', methods=['GET'])
def ask_question():
    print({"message": "Hello, API! Asking Question"})
    name = request.args.get('name')
    question = request.args.get('question')

    if not name:
        name = "default"

    if not question:
        return jsonify({"message": "Missing 'question' query parameter"}), 400

    agent = agents.get(name)
    if agent is None:
        return jsonify({"message": "Agent not found"}), 404

    best_matches = agent.ask(question)
    if best_matches is None:
        return jsonify({"message": "No relevant information found"}), 404

    return jsonify({"best_matches": best_matches})


@agent_bp.route('/parse/web', methods=['GET'])
def agent_parse_url():
    name = request.args.get('name')
    url = request.args.get('url')

    if not name:
        name = "default"

    if not url:
        return jsonify({"message": "Missing 'url' query parameter"}), 400

    print({"message": "Hello, API! Parsing url"}, url)
    agent = agents.get(name)

    if agent is None:
        return jsonify({"message": "Agent not found"}), 404

    print(f"Agent {name} parsing web url: {url}")
    agent.parse_web(url)

    data = {name: agent.to_dict()}
    return jsonify(data)
