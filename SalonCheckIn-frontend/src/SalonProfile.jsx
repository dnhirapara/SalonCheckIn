import React, { useEffect, useState } from "react";
import axios from "./HttpCommon";
import Alert from "./Alert";
import Appointment from "./Appointment";
import Divider from "@material-ui/core/Divider";
import SalonAppointments from "./SalonAppointments";
import { makeStyles } from "@material-ui/core/styles";
import {
  Redirect,
  Route,
  Switch,
} from "react-router-dom/cjs/react-router-dom.min";
import Navbar from "./Navbar";
import TimeLine from "./TimeLine";

const styles = {
  height: "400px",
  display: "block",
};

const SalonProfile = () => {
  const [appointments, setAppointments] = useState([]);
  useEffect(() => {
    axios
      .get("/appointment/getappointmentssalon/", {
        headers: {
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then((res) => {
        console.log("Appointment: ");
        console.log(res.data);
        setAppointments(res.data);
        console.log(appointments);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);
  return (
    <>
      <Navbar />
      <div className="col-md-5 p-2">
        <h3 className="text-dark text-capitalize text-center">appointments</h3>
        <hr className="w-25 mx-auto pt-2" />
        {/* <Appointment data={appointments} style={styles} /> */}
        <SalonAppointments data={appointments} />
      </div>
      <Divider orientation="vertical" flexItem />
    </>
  );
};

export default SalonProfile;
