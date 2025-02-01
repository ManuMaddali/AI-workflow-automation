import React, { useState } from "react";
import api from "../services/api";

function AddTask({ refreshTasks }) {
    const [workflowId, setWorkflowId] = useState("");
    const [name, setName] = useState("");
    const [description, setDescription] = useState("");
    const [status, setStatus] = useState("pending");
    const [message, setMessage] = useState(""); // Success message state

    const handleAddTask = () => {
        api
            .post("/add_task", {
                workflow_id: workflowId,
                name,
                description,
                status,
            })
            .then((response) => {
                setMessage(`Task added: ID ${response.data.id}`);
                refreshTasks(); // Refresh the task list
            })
            .catch((error) => {
                setMessage("Error: " + (error.response?.data?.error || "Unknown error"));
            });
    };

    return (
        <div>
            <h3>Add Task</h3>
            <input
                type="text"
                placeholder="Workflow ID"
                value={workflowId}
                onChange={(e) => setWorkflowId(e.target.value)}
            />
            <input
                type="text"
                placeholder="Task Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
            <textarea
                placeholder="Task Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />
            <select
                value={status}
                onChange={(e) => setStatus(e.target.value)}
            >
                <option value="pending">Pending</option>
                <option value="completed">Completed</option>
            </select>
            <button onClick={handleAddTask}>Add Task</button>
            {message && <p>{message}</p>} {/* Display success or error message */}
        </div>
    );
}

export default AddTask;
