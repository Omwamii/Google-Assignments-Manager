import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar navbar-dark bg-dark fixed-top">
      <div className="container-fluid d-flex">
        <Link className="navbar-brand me-3" to="/">Home</Link>
        <Link className="navbar-brand me-3" to="/notifications">Notifications</Link>
        <Link className="navbar-brand" to='/grades'>Grades</Link>
        <Link className="navbar-brand me-3" to='/stats'>Your progress</Link>
      </div>
    </nav>
  );
}

export default Navbar;