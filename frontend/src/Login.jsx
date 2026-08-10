import { useState } from "react";

const API_URL = "http://127.0.0.1:8000";

function Login({ onLogin }) {
  const [prn, setPrn] = useState("");
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError("");
    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/auth/student/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prn, email }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Login failed");
      }

      onLogin(data.student);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="login-page">
      <section className="login-card">
        <div className="brand-mark">SA</div>
        <p className="eyebrow">SANJIVANI UNIVERSITY</p>
        <h1>Sanjivani AI</h1>
        <p className="subtitle">University Intelligence Platform</p>

        <form onSubmit={handleSubmit}>
          <label htmlFor="prn">Student PRN</label>
          <input
            id="prn"
            value={prn}
            onChange={(event) => setPrn(event.target.value)}
            placeholder="Enter your PRN"
            required
          />

          <label htmlFor="email">College Email</label>
          <input
            id="email"
            type="email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
            placeholder="your.email@sanjivani.edu.in"
            required
          />

          {error && <p className="login-error">{error}</p>}

          <button type="submit" disabled={loading}>
            {loading ? "Verifying..." : "Login"}
          </button>
        </form>

        <p className="login-note">
          Your department will be detected automatically after verification.
        </p>
      </section>
    </main>
  );
}

export default Login;
