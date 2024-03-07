import './index.css';

const Navbar = () => {
    return (
      <nav className="navbar navbar-dark bg-dark">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">
            Home
          </a>
        </div>
        <div className="container-fluid">
          <a className="navbar-brand" href="#">
            Notifications
          </a>
        </div>
        <div className="container-fluid">
          <a className="navbar-brand" href="#">
            Submissions
          </a>
        </div>
      </nav>
    );
}

export default Navbar;