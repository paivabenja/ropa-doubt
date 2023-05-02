import { Routes, Route, Navigate, BrowserRouter } from "react-router-dom";
import { ProfilePage } from "./pages/ProfilePage";
import { ShopPage } from "./pages/ShopPage";
import { Navbar } from "./components/Navbar";
import { SignPage } from "./pages/SignPage";

function App() {
  return (
    <div className="h-full bg-zinc-800 text-gray-200">
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route index element={<Navigate to="/shop" />} />
          <Route path="/shop" element={<ShopPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/signup" element={<SignPage/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
