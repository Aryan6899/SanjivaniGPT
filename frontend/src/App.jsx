import { useEffect, useState } from "react";

function App() {
  const [backendStatus, setBackendStatus] = useState("Checking...");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/health")
      .then((response) => response.json())
      .then((data) => {
        setBackendStatus(data.status);
      })
      .catch(() => {
        setBackendStatus("Backend disconnected");
      });
  }, []);

  return (
    <div>
      <header>
        <h1>SanjivaniGPT</h1>
        <p>Sanjivani University's AI Ecosystem</p>
      </header>

      <main>
        <section>
          <h2>Welcome to SanjivaniGPT</h2>

          <p>
            Your university AI assistant for knowledge,
            documents, campus information and more.
          </p>

          <div>
            Backend Status: <strong>{backendStatus}</strong>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;