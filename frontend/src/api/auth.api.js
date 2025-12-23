const API_URL = "http://localhost:8000"

export async function login(username, password) {
  const body = new URLSearchParams()
  body.append("username", username)
  body.append("password", password)

  const res = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body,
  })

  if (!res.ok) {
    throw new Error("Invalid credentials")
  }

  return res.json()
}

export async function register(username, password, token = null) {
  const headers = {
    "Content-Type": "application/json",
  }

  if (token) {
    headers.Authorization = `Bearer ${token}`
  }

  const res = await fetch(`${API_URL}/auth/register`, {
    method: "POST",
    headers,
    body: JSON.stringify({ username, password }),
  })

  if (!res.ok) {
    const err = await res.json()
    throw new Error(err.detail || "Register failed")
  }

  return res.json()
}
