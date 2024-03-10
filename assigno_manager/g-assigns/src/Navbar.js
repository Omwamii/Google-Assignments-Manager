import './index.css';

import React from 'react'; // Import React

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
        <a className="navbar-brand me-3" href="#">
          Submissions
        </a>
        <a className="navbar-brand" href="#">
          Grades
        </a>
      </div>
    </nav>
  );
}

export default Navbar;