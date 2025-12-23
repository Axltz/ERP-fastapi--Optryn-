import { useState } from "react";
import { login } from "../../api/auth.api";

export default function AdminAuthModal({ onSuccess, onClose }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    const res = await login(username, password);

    if (!res.access_token) {
      setError("Credenciales de admin inválidas");
      return;
    }

    onSuccess(res.access_token);
  };

  return (
    <div className="modal">
      <h3>Autenticación de Admin</h3>

      <input
        placeholder="Admin username"
        value={username}
        onChange={e => setUsername(e.target.value)}
      />

      <input
        type="password"
        placeholder="Admin password"
        value={password}
        onChange={e => setPassword(e.target.value)}
      />

      {error && <p style={{ color: "red" }}>{error}</p>}

      <button onClick={handleSubmit}>Confirmar</button>
      <button onClick={onClose}>Cancelar</button>
    </div>
  );
}
