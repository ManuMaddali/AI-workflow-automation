from flask import Blueprint, jsonify, request
from backend.__init__ import db
from backend.models.user import User
from backend.operator_utils import operator_request

routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    return {"message": "Welcome to the Workflow Automation MVP!"}

@routes.route("/add_user", methods=["POST"])
def add_user():
    from backend import db
    from backend.models.user import User

    try:
        data = request.json

        # Validate input
        if not data or not data.get("email") or not data.get("password_hash"):
            return jsonify({"error": "Invalid input"}), 400

        # Check for existing user with the same email
        existing_user = User.query.filter_by(email=data["email"]).first()
        if existing_user:
            return jsonify({"error": "User with this email already exists"}), 400

        # Create a new User instance
        new_user = User(email=data["email"], password_hash=data["password_hash"])
        db.session.add(new_user)
        db.session.commit()

        # Return a response with the user ID
        return jsonify({"message": "User added successfully!", "id": new_user.id})

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@routes.route("/users", methods=["GET"])
def get_users():
    from backend import db  # Import db here to avoid circular import
    from backend.models.user import User  # Import model here to avoid circular import

    users = User.query.all()
    return jsonify([{"id": u.id, "email": u.email} for u in users])

@routes.route("/add_workflow", methods=["POST"])
def add_workflow():
    from backend import db
    from backend.models.workflow import Workflow

    try:
        data = request.json

        # Validate input
        if not data or not data.get("user_id") or not data.get("name"):
            return jsonify({"error": "Invalid input"}), 400

        # Check if user exists
        user = User.query.get(data["user_id"])
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Check for duplicate workflow name
        existing_workflow = Workflow.query.filter_by(user_id=data["user_id"], name=data["name"]).first()
        if existing_workflow:
            return jsonify({"error": "Workflow with this name already exists for the user"}), 400

        # Create workflow
        new_workflow = Workflow(
            user_id=data["user_id"],
            name=data["name"],
            description=data.get("description", "")
        )
        db.session.add(new_workflow)
        db.session.commit()

        return jsonify({"message": "Workflow added successfully!", "id": new_workflow.id})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@routes.route("/add_task", methods=["POST"])
def add_task():
    from backend import db
    from backend.models.task import Task
    from backend.models.workflow import Workflow

    try:
        data = request.json

        # Validate input
        if not data or not data.get("workflow_id") or not data.get("name"):
            return jsonify({"error": "Invalid input"}), 400

        # Check if workflow exists
        workflow = Workflow.query.get(data["workflow_id"])
        if not workflow:
            return jsonify({"error": "Workflow not found"}), 404

        # Create task
        new_task = Task(
            workflow_id=data["workflow_id"],
            name=data["name"],
            description=data.get("description", ""),
            status=data.get("status", "pending")
        )
        db.session.add(new_task)
        db.session.commit()

        return jsonify({"message": "Task added successfully!", "id": new_task.id})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@routes.route("/workflows", methods=["GET"])
def get_workflows():
    from backend.models.workflow import Workflow
    workflows = Workflow.query.all()
    return jsonify([
        {"id": wf.id, "user_id": wf.user_id, "name": wf.name, "description": wf.description}
        for wf in workflows
    ])

@routes.route("/tasks", methods=["GET"])
def get_tasks():
    from backend.models.task import Task
    tasks = Task.query.all()
    return jsonify([
        {"id": task.id, "workflow_id": task.workflow_id, "name": task.name, "description": task.description, "status": task.status}
        for task in tasks
    ])

@routes.route("/update_workflow/<int:id>", methods=["PUT"])
def update_workflow(id):
    from backend import db
    from backend.models.workflow import Workflow

    try:
        data = request.json
        workflow = Workflow.query.get(id)

        if not workflow:
            return jsonify({"error": "Workflow not found"}), 404

        workflow.name = data.get("name", workflow.name)
        workflow.description = data.get("description", workflow.description)
        db.session.commit()

        return jsonify({"message": "Workflow updated successfully!"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@routes.route("/delete_workflow/<int:id>", methods=["DELETE"])
def delete_workflow(id):
    from backend import db
    from backend.models.workflow import Workflow
    try:
        workflow = Workflow.query.get(id)

        if not workflow:
            return jsonify({"error": "Workflow not found"}), 404

        db.session.delete(workflow)
        db.session.commit()

        return jsonify({"message": "Workflow deleted successfully!"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@routes.route("/update_task/<int:id>", methods=["PUT"])
def update_task(id):
    from backend import db
    from backend.models.task import Task
    try:
        data = request.json
        task = Task.query.get(id)

        if not task:
            return jsonify({"error": "Task not found"}), 404

        task.name = data.get("name", task.name)
        task.description = data.get("description", task.description)
        task.status = data.get("status", task.status)
        db.session.commit()

        return jsonify({"message": "Task updated successfully!"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Task updated successfully!"})

@routes.route("/delete_task/<int:id>", methods=["DELETE"])
def delete_task(id):
    from backend import db
    from backend.models.task import Task
    try:
        task = Task.query.get(id)

        if not task:
            return jsonify({"error": "Task not found"}), 404

        db.session.delete(task)
        db.session.commit()

        return jsonify({"message": "Task deleted successfully!"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@routes.route("/test_operator", methods=["POST"])
def test_operator():
    """
    Test endpoint for sending a prompt to Operator.
    """
    from backend.operator_utils import operator_request

    data = request.json
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    result = operator_request(prompt)
    return jsonify({"response": result})

@routes.route("/execute_workflow/<int:id>", methods=["POST"])
def execute_workflow(id):
    from backend.models.workflow import Workflow
    from backend.operator_utils import operator_request

    workflow = Workflow.query.get(id)
    if not workflow:
        return jsonify({"error": "Workflow not found"}), 404

    if not workflow.steps:
        return jsonify({"error": "No steps defined for this workflow"}), 400

    logs = []
    for step in workflow.steps:
        try:
            logs.append(f"Executing step: {step}")
            result = operator_request(step)
            logs.append(f"Result: {result}")
        except Exception as e:
            logs.append(f"Error: {str(e)}")
            break

    workflow.execution_logs = "\n".join(logs)
    db.session.commit()

    return jsonify({"message": "Workflow executed", "logs": logs})
