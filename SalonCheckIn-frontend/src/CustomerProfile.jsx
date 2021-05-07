import React from "react";
import Divider from "@material-ui/core/Divider";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Navbar from "./Navbar";

const mycol = {
  border: "2px solid rgb(20, 31, 62)",
  height: "225px",
  "background-color": "#141f3e",
  "padding-top": "15px",
};

const CustomerProfile = () => {
  return (
    <>
      <h1>Welcome Customer</h1>
      <Navbar />
      <div className="container-fluid fixed">
        <div className="row">
          <div className="col-md-3 col-sm-12" style={mycol}>
            <div className=" align-item-center">
              <img
                src="images/chair.jpg"
                className="align-self-center img-fluid rounded"
                alt="..."
              />
            </div>
          </div>
          <div className="col-md-6 mycol col-sm-12" style={mycol}>
            <h3 className="text-white text-capitalize">Dr. Watson</h3>
            <p className="text-muted text-capitalize">Address:</p>
            <span className="text-light text-capitalize ">
              221B Baker Street
            </span>
            <p className="text-muted text-capitalize">email:</p>
            <span className="text-light text-capitalize ">
              watson@gmail.com
            </span>
            <p className="text-muted text-capitalize">contact number:</p>
            <span className="text-light text-capitalize ">91123</span>
          </div>
        </div>
      </div>
    </>
  );
};

export default CustomerProfile;
