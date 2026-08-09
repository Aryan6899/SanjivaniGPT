import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!message.trim()) {
      return;
    }

    const userMessage = {
      role: "user",
      content: message
    };

    setMessages((previous) => [...previous, userMessage]);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/chat/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            message: message
          })
        }
      );

      const data = await response.json();

      const botMessage = {
        role: "assistant",
        content: data.reply
      };

      setMessages((previous) => [...previous, botMessage]);
    } catch (error) {
      console.error(error);

      const errorMessage = {
        role: "assistant",
        content: "Unable to connect to SanjivaniGPT backend."
      };

      setMessages((previous) => [...previous, errorMessage]);
    }

    setMessage("");
  };


  return (
    <div className="app">

      <header className="header">
        <h1>SanjivaniGPT</h1>
        <p>Sanjivani University's AI Ecosystem</p>
      </header>


      <main className="chat-container">

        <div className="messages">

          {messages.length === 0 && (
            <div className="welcome">
              <h2>Welcome to SanjivaniGPT 👋</h2>

              <p>
                Ask anything about Sanjivani University.
              </p>
            </div>
          )}


          {messages.map((msg, index) => (
            <div
              key={index}
              className={`message ${msg.role}`}
            >
              <strong>
                {msg.role === "user"
                  ? "You"
                  : "SanjivaniGPT"}
              </strong>

              <p>{msg.content}</p>
            </div>
          ))}

        </div>


        <div className="input-area">

          <input
            type="text"
            placeholder="Ask SanjivaniGPT..."
            value={message}
            onChange={(event) =>
              setMessage(event.target.value)
            }
            onKeyDown={(event) => {
              if (event.key === "Enter") {
                sendMessage();
              }
            }}
          />

          <button onClick={sendMessage}>
            Send
          </button>

        </div>

      </main>

    </div>
  );
}

export default App;