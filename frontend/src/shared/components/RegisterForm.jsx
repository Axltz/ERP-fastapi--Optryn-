import { useState } from "react";
import { registerUser } from "../api/auth";
import AdminAuthModal from "./AdminAuthModal";

export default function RegisterForm({ requiresAdmin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [showAdminModal, setShowAdminModal] = useState(false);
  const [adminToken, setAdminToken] = useState(null);

  const submitRegister = async (token = null) => {
    const res = await registerUser(
      { username, password },
      token
    );

    if (res.status === 403) {
      setShowAdminModal(true);
      return;
    }

    if (!res.ok) {
      alert("Error al registrar");
      return;
    }

    alert("Usuario registrado correctamente");
  };

  return (
    <div>
      <h3>Registro</h3>

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

      <button onClick={() => submitRegister(adminToken)}>
        Registrar
      </button>

      {showAdminModal && (
        <AdminAuthModal
          onSuccess={(token) => {
            setAdminToken(token);
            setShowAdminModal(false);
            submitRegister(token);
          }}
          onClose={() => setShowAdminModal(false)}
        />
      )}
    </div>
  );
}
