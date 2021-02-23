import React from "react";

const footerStyle = {
  //   marginTop: "auto",
  bottom: "0",
  background: "black",
};

const Footer = () => {
  return (
    <>
      <footer style={footerStyle}>
        <p className="text-lg-center text-info" id="footer">
          &copy; All rights Reserved. saloncheckin.com
        </p>
      </footer>
    </>
  );
};

export default Footer;
