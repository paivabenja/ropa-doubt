import { Link } from "react-router-dom";

export const Navbar = () => {
  return (
    <div className="flex border border-solid border-gray-50">
      <button>
        <Link to="/profile">Perfil</Link>
      </button>
      <button>
        <Link to="/signup">Sign Up</Link>
      </button>
      <h1>
        <Link to="/shop">Home</Link>
      </h1>
    </div>
  );
};
