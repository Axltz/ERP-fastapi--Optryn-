import { useState } from "react"
import { register, login } from "../../api/auth.api"
import { useNavigate } from "react-router-dom"

export default function Register() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [adminUser, setAdminUser] = useState("")
  const [adminPass, setAdminPass] = useState("")
  const [needAdmin, setNeedAdmin] = useState(false)
  const [error, setError] = useState("")
  const navigate = useNavigate()

  const handleRegister = async () => {
    try {
      await register(username, password)
      navigate("/login")
    } catch (err) {
      if (err.message.includes("Admin")) {
        setNeedAdmin(true)
      } else {
        setError(err.message)
      }
    }
  }

  const handleAdminConfirm = async () => {
    try {
      const adminLogin = await login(adminUser, adminPass)
      await register(username, password, adminLogin.access_token)
      navigate("/login")
    } catch {
      setError("Invalid admin credentials")
    }
  }

  return (
    <>
      <h2>Register</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}

      <input placeholder="Username" onChange={e => setUsername(e.target.value)} />
      <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />

      <button onClick={handleRegister}>Register</button>

      {needAdmin && (
        <div>
          <h4>Admin credentials required</h4>
          <input placeholder="Admin user" onChange={e => setAdminUser(e.target.value)} />
          <input type="password" placeholder="Admin password" onChange={e => setAdminPass(e.target.value)} />
          <button onClick={handleAdminConfirm}>Confirm</button>
        </div>
      )}
    </>
  )
}
