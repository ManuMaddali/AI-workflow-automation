import React, { useEffect, useState } from "react";
import api from "./services/api";  // Correct import path
import AddUser from "./components/AddUser";
import AddWorkflow from "./components/AddWorkflow";
import AddTask from "./components/AddTask";
import ExecuteWorkflow from "./components/ExecuteWorkflow";
import "./App.css";

function App() {
    const [users, setUsers] = useState([]);
    const [workflows, setWorkflows] = useState([]);
    const [tasks, setTasks] = useState([]);

    const refreshUsers = () => {
        api
            .get("/users")
            .then((response) => setUsers(response.data))
            .catch((error) => console.error("Error fetching users:", error));
    };

    const refreshWorkflows = () => {
        api
            .get("/workflows")
            .then((response) => setWorkflows(response.data))
            .catch((error) => console.error("Error fetching workflows:", error));
    };

    const refreshTasks = () => {
        api
            .get("/tasks")
            .then((response) => setTasks(response.data))
            .catch((error) => console.error("Error fetching tasks:", error));
    };

    useEffect(() => {
        refreshUsers();
        refreshWorkflows();
        refreshTasks();
    }, []);

    return (
        <div className="container">
            <h1>Workflow Automation App</h1>

            {/* Add User Section */}
            <div className="section">
                <h2>Add User</h2>
                <AddUser refreshUsers={refreshUsers} />
            </div>

            {/* Add Workflow Section */}
            <div className="section">
                <h2>Add Workflow</h2>
                <AddWorkflow refreshWorkflows={refreshWorkflows} />
            </div>

            {/* Add Task Section */}
            <div className="section">
                <h2>Add Task</h2>
                <AddTask refreshTasks={refreshTasks} />
            </div>

            {/* Tables for Users, Workflows, and Tasks */}
            <div className="table-container">
    <h3>Users</h3>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Email</th>
            </tr>
        </thead>
        <tbody>
            {users.map((user) => (
                <tr key={user.id}>
                    <td>{user.id}</td>
                    <td>{user.email}</td>
                </tr>
            ))}
        </tbody>
    </table>

    <h3>Workflows</h3>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            {workflows.map((workflow) => (
                <tr key={workflow.id}>
                    <td>{workflow.id}</td>
                    <td>{workflow.name}</td>
                    <td>{workflow.description}</td>
                </tr>
            ))}
        </tbody>
    </table>

    <h3>Tasks</h3>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Workflow ID</th>
                <th>Name</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            {tasks.map((task) => (
                <tr key={task.id}>
                    <td>{task.id}</td>
                    <td>{task.workflow_id}</td>
                    <td>{task.name}</td>
                    <td>{task.status}</td>
                </tr>
            ))}
        </tbody>
    </table>
</div>


            {/* Execute Workflow Section */}
            <div className="section">
                <h2>Execute Workflow</h2>
                <ExecuteWorkflow />
            </div>
        </div>
    );
}

export default App;
