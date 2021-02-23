import React from "react";
import RegisterSalonCustomer from "./RegisterSalonCustomer";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "../node_modules/bootstrap/dist/js/bootstrap.bundle";

import Alert from "./Alert";

// let x="bhdsc";
const showAlert = (al) => {
  alert(al);
  console.log(al[0]);
  console.log(typeof al);
  <Alert response={al[0]} />;
};

const RegisterSalon = () => {
  return (
    <>
      {/* <Alert response="hello"/> */}
      <RegisterSalonCustomer type="Shop" Show={showAlert} />
    </>
  );
};

export default RegisterSalon;
