from flask import Blueprint, jsonify, request

api_bp = Blueprint('api', __name__)


@api_bp.route('/data', methods=['GET'])
def get_data():
    data = {"message": "Hello, API!"}
    return jsonify(data)


@api_bp.route('/data', methods=['POST'])
def post_data():
    data = request.json
    return jsonify(data), 201
