import React, { useEffect, useState } from "react";
import Divider from "@material-ui/core/Divider";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Navbar2 from "./Navbar2";
import axios from "./HttpCommon";
import { Link, Redirect, useParams } from "react-router-dom";
import StyleCard from "./StyleCard";

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    flexWrap: "wrap",
    "& > *": {
      margin: theme.spacing(1),
      width: theme.spacing(16),
      height: theme.spacing(16),
    },
  },
}));

const mycol = {
  border: "2px solid rgb(20, 31, 62)",
  height: "225px",
  "background-color": "#141f3e",
  "padding-top": "15px",
};

const styles = {
  height: "400px",
};

const CustomerSalon = (props) => {
  const classes = useStyles();
  const { slug } = useParams();
  const [salonStyles, setSalonStyles] = useState([]);
  useEffect(() => {
    axios
      .get("/service/getservices/")
      .then((res) => {
        console.log(res.data);
        setSalonStyles(res.data);
      })
      .catch((err) => console.log(err));
  }, []);
  console.log(slug);
  return (
    <>
      <Navbar2 />
      <div className="container-fluid fixed">
        <div className="row">
          <div className="col-md-3 col-sm-12" style={mycol}>
            <div className=" align-item-center">
              <img
                src="images/barbershop.jpg"
                className="align-self-center img-fluid rounded"
                alt="..."
              />
            </div>
          </div>
          <div className="col-md-6 mycol col-sm-12" style={mycol}>
            <h3 className="text-white text-capitalize">Sherlock salon</h3>
            <p className="text-muted text-capitalize">the game is on</p>
            <span className="text-light text-capitalize ">
              3rd Eye II, Ellis Bridge, CG Road, Navrangpura
            </span>
            <p className="text-light text-capitalize ">
              Appointments Left:<span className="text-danger">&nbsp;2</span>
            </p>
          </div>
          <div className="col-md-3 mycol col-sm-12" style={mycol}>
            <h4 className="text-white text-capitalize text-center">OFFER</h4>
            <hr className="w-75 pt-2 bg-light" />
            <p className="text-light text-capitalize ">
              Grab 5% Disccount on Corean Cut
            </p>
            <span className="text-light">5% Discount to 1st Customer </span>
          </div>
        </div>
      </div>
      <div className="container-fluid">
        <div className="row">
          <div className="col-md-5 p-2" style={styles}>
            <h3 className="text-dark text-capitalize text-center">
              appointments
            </h3>
            <hr className="w-25 mx-auto pt-2" />
            <ul class="list-group">
              <li class="list-group-item">Appointment 1:9:30 to 10:00</li>
              <li class="list-group-item">Appointment 2:10:00 to 10:30</li>
              <li class="list-group-item">Appointment 3:11:00 to 11:30</li>
              <li class="list-group-item">Appointment 4:11:30 to 12:00</li>
            </ul>
            <a
              href="/appointment"
              className="btn btn-secondary btn-sm active center"
              role="button"
              aria-pressed="true"
            >
              Make an Appointment
            </a>
          </div>
          <Divider orientation="vertical" flexItem />
          <div className="col-md-5 p-2" style={styles}>
            <h3 className="text-dark text-capitalize text-center">styles</h3>
            <hr className="w-25 mx-auto pt-2" />
            <ul class="list-group">
              <StyleCard data={salonStyles} />
            </ul>
          </div>
        </div>
      </div>
    </>
  );
};

export default CustomerSalon;
