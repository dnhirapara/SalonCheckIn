import React, { useState } from "react";

const LogOut = () => {
  localStorage.clear();
  window.location = "http://localhost:3000/";
  return;
};

export default LogOut;
