import React from "react";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "../node_modules/bootstrap/dist/js/bootstrap.bundle";

const Alert = (props) => {
  return (
    <>
      <div
        className="alert alert-danger alert-dismissible fade show"
        style={{ vissiblity: "hidden" }}
        role="alert"
      >
        <strong>Error!</strong>
        {props.response}
        <button
          type="button"
          className="btn-close"
          data-bs-dismiss="alert"
          aria-label="Close"
        ></button>
      </div>
    </>
  );
};

export default Alert;
