import requests

BASE_URL = "http://127.0.0.1:5000"

def print_response(response):
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("-" * 50)

def test_add_user():
    print("Testing Add User...")
    url = f"{BASE_URL}/add_user"
    payload = {
        "email": "test@example.com",
        "password_hash": "hashedpassword"
    }
    response = requests.post(url, json=payload)
    print_response(response)
    if response.status_code == 400 and "User with this email already exists" in response.text:
        print("User already exists. Continuing...")
        return None
    return response.json().get("id")

def test_add_workflow(user_id):
    print("Testing Add Workflow...")
    url = f"{BASE_URL}/add_workflow"
    payload = {
        "user_id": user_id,
        "name": "Test Workflow",
        "description": "A test workflow description"
    }
    response = requests.post(url, json=payload)
    print_response(response)
    return response.json().get("id")

def test_add_task(workflow_id):
    print("Testing Add Task...")
    url = f"{BASE_URL}/add_task"
    payload = {
        "workflow_id": workflow_id,
        "name": "Test Task",
        "description": "A test task description",
        "status": "pending"
    }
    response = requests.post(url, json=payload)
    print_response(response)
    return response.json().get("id")

def test_update_workflow(workflow_id):
    print("Testing Update Workflow...")
    url = f"{BASE_URL}/update_workflow/{workflow_id}"
    payload = {
        "name": "Updated Workflow",
        "description": "Updated description for workflow"
    }
    response = requests.put(url, json=payload)
    print_response(response)

def test_update_task(task_id):
    print("Testing Update Task...")
    url = f"{BASE_URL}/update_task/{task_id}"
    payload = {
        "name": "Updated Task",
        "description": "Updated description for task",
        "status": "completed"
    }
    response = requests.put(url, json=payload)
    print_response(response)

def test_get_users():
    print("Testing Get Users...")
    url = f"{BASE_URL}/users"
    response = requests.get(url)
    print_response(response)

def test_get_workflows():
    print("Testing Get Workflows...")
    url = f"{BASE_URL}/workflows"
    response = requests.get(url)
    print_response(response)

def test_get_tasks():
    print("Testing Get Tasks...")
    url = f"{BASE_URL}/tasks"
    response = requests.get(url)
    print_response(response)

def test_delete_workflow(workflow_id):
    print("Testing Delete Workflow...")
    url = f"{BASE_URL}/delete_workflow/{workflow_id}"
    response = requests.delete(url)
    print_response(response)

def test_delete_task(task_id):
    print("Testing Delete Task...")
    url = f"{BASE_URL}/delete_task/{task_id}"
    response = requests.delete(url)
    print_response(response)

def main():
    print("Starting API Tests...")

    user_id = test_add_user()
    if not user_id:
        print("Skipping workflow and task creation as user could not be added.")
        return

    workflow_id = test_add_workflow(user_id)
    if not workflow_id:
        print("Skipping task creation as workflow could not be added.")
        return

    task_id = test_add_task(workflow_id)
    if not task_id:
        print("Skipping updates and deletions as task could not be added.")
        return

    test_update_workflow(workflow_id)
    test_update_task(task_id)

    test_get_users()
    test_get_workflows()
    test_get_tasks()

    test_delete_task(task_id)
    test_delete_workflow(workflow_id)

    print("API Tests Completed.")

if __name__ == "__main__":
    main()
