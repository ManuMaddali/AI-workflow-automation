import React, { useEffect, useState } from "react";
import api from "./services/api";

function App() {
    const [message, setMessage] = useState("");

    useEffect(() => {
        // Fetch data from the Flask backend
        api.get("/")
            .then((response) => {
                setMessage(response.data.message); // Set the message from the backend
            })
            .catch((error) => {
                console.error("Error fetching data:", error);
            });
    }, []);

    return (
        <div>
            <h1>Frontend App</h1>
            <p>Backend says: {message}</p>
        </div>
    );
}

export default App;
