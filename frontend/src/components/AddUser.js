import React, { useState } from "react";
import api from "../services/api";

function AddUser({ refreshUsers }) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState(""); // Success message state

    const handleAddUser = () => {
        api
            .post("/add_user", { email, password_hash: password })
            .then((response) => {
                setMessage(`User added: ID ${response.data.id}`);
                refreshUsers(); // Refresh the user list
            })
            .catch((error) => {
                setMessage("Error: " + (error.response?.data?.error || "Unknown error"));
            });
    };

    return (
        <div>
            <h3>Add User</h3>
            <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <button onClick={handleAddUser}>Add User</button>
            {message && <p>{message}</p>} {/* Display success or error message */}
        </div>
    );
}

export default AddUser;
