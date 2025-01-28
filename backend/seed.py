from backend import db, create_app
from backend.models.user import User
from backend.models.workflow import Workflow
from backend.models.task import Task

app = create_app()
with app.app_context():
    # Create initial users
    user1 = User(email="test1@example.com", password_hash="hashedpassword1")
    user2 = User(email="test2@example.com", password_hash="hashedpassword2")
    db.session.add_all([user1, user2])

    # Create workflows
    workflow1 = Workflow(user_id=user1.id, name="Test Workflow 1", description="A sample workflow")
    workflow2 = Workflow(user_id=user2.id, name="Test Workflow 2", description="Another sample workflow")
    db.session.add_all([workflow1, workflow2])

    # Create tasks
    task1 = Task(workflow_id=workflow1.id, name="Test Task 1", description="First task", status="pending")
    task2 = Task(workflow_id=workflow2.id, name="Test Task 2", description="Second task", status="completed")
    db.session.add_all([task1, task2])

    # Commit changes
    db.session.commit()
    print("Seed data created successfully!")
