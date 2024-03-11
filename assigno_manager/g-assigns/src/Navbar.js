import React from 'react';

const Navbar = () => {
  return (
    <nav className="navbar navbar-dark bg-dark fixed-top">
      <div className="container-fluid d-flex">
        <a className="navbar-brand me-3" href="#">
          Home
        </a>
        <a className="navbar-brand me-3" href="#">
          Notifications
        </a>
        <a className="navbar-brand" href="#">
          Grades
        </a>
        <a className="navbar-brand me-3" href="#">
          Your progress
        </a>
      </div>
    </nav>
  );
}

export default Navbar;