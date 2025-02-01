import React, { useState } from "react";
import api from "../services/api";

function ExecuteWorkflow() {
    const [workflowId, setWorkflowId] = useState("");
    const [message, setMessage] = useState(""); // Success or error message

    const handleExecuteWorkflow = () => {
        api
            .post(`/execute_workflow/${workflowId}`)
            .then((response) => {
                setMessage("Workflow executed successfully!");
                console.log(response.data.logs); // You can log or display execution logs if needed
            })
            .catch((error) => {
                setMessage("Error: " + (error.response?.data?.error || "Unknown error"));
            });
    };

    return (
        <div>
            <h3>Execute Workflow</h3>
            <input
                type="text"
                placeholder="Workflow ID"
                value={workflowId}
                onChange={(e) => setWorkflowId(e.target.value)}
            />
            <button onClick={handleExecuteWorkflow}>Execute Workflow</button>
            {message && <p>{message}</p>} {/* Display success or error message */}
        </div>
    );
}

export default ExecuteWorkflow;
