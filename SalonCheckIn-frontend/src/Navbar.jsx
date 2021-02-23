import React from "react";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";

const Navbar = () => {
  return (
    <>
      <header>
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <div className="container-fluid">
            <NavLink className="navbar-brand" to="/">
              SalonCheckIn
            </NavLink>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div
              className="collapse navbar-collapse"
              id="navbarSupportedContent"
            >
              <ul className="navbar-nav ml-auto mb-2 mb-lg-0">
                <li className="nav-item">
                  <NavLink
                    className="nav-link"
                    exact
                    activeClassName="active_class"
                    to="/"
                  >
                    Home
                  </NavLink>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="/#about">
                    About Us
                  </a>
                </li>
                <li className="nav-item">
                  <NavLink
                    className="nav-link"
                    to="/register"
                    exact
                    activeClassName="active_class"
                  >
                    Register
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink
                    className="nav-link"
                    to="/login"
                    exact
                    activeClassName="active_class"
                  >
                    Login
                  </NavLink>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </header>
    </>
  );
};

export default Navbar;
