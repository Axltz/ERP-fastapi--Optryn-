import { Routes, Route, Navigate } from "react-router-dom"
import LoginPage from "../auth/pages/Login"
import RegisterPage from "../auth/pages/Register"

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/register" element={<RegisterPage />} />
    </Routes>
  )
}
