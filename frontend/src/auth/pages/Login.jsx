import { useState } from "react"
import { login } from "../../api/auth.api"
import { useNavigate } from "react-router-dom"

export default function Login() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState("")
  const navigate = useNavigate()

  const handleLogin = async (e) => {
    e.preventDefault()
    setError("")

    try {
      const data = await login(username, password)
      localStorage.setItem("token", data.access_token)
      navigate("/dashboard")
    } catch {
      setError("Invalid credentials")
    }
  }

  return (
    <form onSubmit={handleLogin}>
      <h2>Login</h2>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <input value={username} onChange={e => setUsername(e.target.value)} />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} />

      <button type="submit">Login</button>
      <button type="button" onClick={() => navigate("/register")}>
        Register
      </button>
    </form>
  )
}
