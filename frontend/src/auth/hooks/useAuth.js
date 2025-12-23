import { login as apiLogin, registerUser } from "../../api/auth.api";

export function useAuth() {
  const login = async (username, password) => {
    const data = await apiLogin(username, password);
    localStorage.setItem("token", data.access_token);
    return data;
  };

  const logout = () => {
    localStorage.removeItem("token");
  };

  const register = async (userData) => {
    const token = localStorage.getItem("token");
    return registerUser(userData, token);
  };

  return { login, logout, register };
}
