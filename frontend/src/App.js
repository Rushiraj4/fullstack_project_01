import LoginPanel from "./components/Login/Login";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      {/* Add other routes as needed */}
    </Routes>
  );
}

export default App;
