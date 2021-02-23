import React, { useState } from "react";
import axios from "axios";
import Alert from "./Alert";
import Navbar2 from "./Navbar2";

const AddStyle = () => {
  const [data, setData] = useState({
    styleName: "",
    styleTags: "1",
    styleCost: "",
    styleDuration: "",
  });

  const inputEvent = (event) => {
    const { name, value } = event.target;
    setData((prev) => {
      return {
        ...prev,
        [name]: value,
      };
    });
  };

  const formSubmit = (e) => {
    e.preventDefault();
    alert(
      ` ${data.styleName} ${data.styleCost} ${data.styleDuration} ${data.styleTags} `
    );
    var bodyFormData = new FormData();
    bodyFormData.append("name", data.styleName);
    bodyFormData.append("tags", data.styleTags);
    bodyFormData.append("price", data.styleCost);
    bodyFormData.append("duration", data.styleDuration);
    console.log(bodyFormData.entries());

    axios
      .post("http://127.0.0.1:8000/api/service/getservices/", bodyFormData, {
        headers: {
          Authorization: "Token " + localStorage.getItem("token"),
        },
      })
      .then((res) => {
        let result = res.data;
        window.location = "http://localhost:3000/shopprofile";
      })
      .catch((e) => {});
  };
  return (
    <>
      <Navbar2 />
      <div className="my-5">
        <h2 className="text-center">Style</h2>
        <hr className="w-25 mx-auto pt-2" />
      </div>
      <div className="container">
        <div className="row">
          <div className="col-md-4 col-8 mx-auto">
            <form onSubmit={formSubmit}>
              <div className="mb-3">
                <label htmlFor="styleName" className="form-label">
                  Style name
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="styleName"
                  placeholder=""
                  name="styleName"
                  value={data.styleName}
                  onChange={inputEvent}
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="styleCost" className="form-label">
                  Style cost
                </label>
                <input
                  type="number"
                  className="form-control"
                  id="styleCost"
                  placeholder="in rupees"
                  name="styleCost"
                  value={data.styleCost}
                  onChange={inputEvent}
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="styleDuration" className="form-label">
                  Style Duration
                </label>
                <input
                  type="number"
                  className="form-control"
                  id="styleDuration"
                  placeholder="in minutes"
                  name="styleDuration"
                  value={data.styleDuration}
                  onChange={inputEvent}
                  required
                />
              </div>
              <div className="mb-3">
                <button className="btn btn-outline-secondary" type="submit">
                  ADD
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  );
};

export default AddStyle;
