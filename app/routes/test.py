from flask import Blueprint, jsonify


test_routes = Blueprint("test_routes", __name__)


@test_routes.route("/status")
def test():
    return jsonify({"message": "Server is running..."})
