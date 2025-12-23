import { useState } from "react";
import { login } from "../../api/auth.api";

export default function LoginForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    const res = await login(username, password);

    if (!res.access_token) {
      alert("Credenciales inválidas");
      return;
    }

    localStorage.setItem("token", res.access_token);
    alert("Login correcto");
  };

  return (
    <div>
      <h2>Login</h2>

      <input
        placeholder="Username"
        value={username}
        onChange={e => setUsername(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={e => setPassword(e.target.value)}
      />

      <button onClick={handleLogin}>Entrar</button>
    </div>
  );
}
