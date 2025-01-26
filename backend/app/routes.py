from flask import Blueprint, jsonify

routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    return {"message": "Welcome to the Workflow Automation MVP!"}
