import { useState } from "react";
import Login from "./Login";

function App() {
  const [student, setStudent] = useState(null);
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);

  if (!student) return <Login onLogin={setStudent} />;

  const sendMessage = async () => {
    if (!message.trim()) return;
    setMessages((previous) => [...previous, { role: "user", content: message }]);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });
      const data = await response.json();
      setMessages((previous) => [
        ...previous,
        { role: "assistant", content: data.reply },
      ]);
    } catch {
      setMessages((previous) => [
        ...previous,
        { role: "assistant", content: "Unable to connect to Sanjivani AI backend." },
      ]);
    }
    setMessage("");
  };

  return (
    <div className="app">
      <header className="header">
        <div>
          <h1>Sanjivani AI</h1>
          <p>{student.department_name} • Student Portal</p>
        </div>
        <div className="student-badge">
          <strong>{student.name}</strong>
          <span>{student.prn}</span>
        </div>
      </header>

      <main className="chat-container">
        <div className="messages">
          {messages.length === 0 && (
            <div className="welcome">
              <h2>Welcome, {student.name} 👋</h2>
              <p>
                You are logged in as a {student.department_code} student.
                Ask Sanjivani AI a question.
              </p>
            </div>
          )}

          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.role}`}>
              <strong>{msg.role === "user" ? "You" : "Sanjivani AI"}</strong>
              <p>{msg.content}</p>
            </div>
          ))}
        </div>

        <div className="input-area">
          <input
            type="text"
            placeholder="Ask Sanjivani AI..."
            value={message}
            onChange={(event) => setMessage(event.target.value)}
            onKeyDown={(event) => event.key === "Enter" && sendMessage()}
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </main>
    </div>
  );
}

export default App;
