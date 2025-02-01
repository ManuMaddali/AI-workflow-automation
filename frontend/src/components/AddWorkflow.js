import React, { useState } from "react";
import api from "../services/api";

function AddWorkflow({ refreshWorkflows }) {
    const [userId, setUserId] = useState("");
    const [name, setName] = useState("");
    const [description, setDescription] = useState("");
    const [message, setMessage] = useState(""); // Success message state

    const handleAddWorkflow = () => {
        api
            .post("/add_workflow", { user_id: userId, name, description })
            .then((response) => {
                setMessage(`Workflow added: ID ${response.data.id}`);
                refreshWorkflows(); // Refresh the workflow list
            })
            .catch((error) => {
                setMessage("Error: " + (error.response?.data?.error || "Unknown error"));
            });
    };

    return (
        <div>
            <h3>Add Workflow</h3>
            <input
                type="text"
                placeholder="User ID"
                value={userId}
                onChange={(e) => setUserId(e.target.value)}
            />
            <input
                type="text"
                placeholder="Workflow Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
            <textarea
                placeholder="Workflow Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />
            <button onClick={handleAddWorkflow}>Add Workflow</button>
            {message && <p>{message}</p>} {/* Display success or error message */}
        </div>
    );
}

export default AddWorkflow;
