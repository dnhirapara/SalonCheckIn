import React, { useEffect, useState } from "react";
import axios from "./HttpCommon";
import Alert from "./Alert";

const MakeAppointment = () => {
  const [data, setData] = useState({
    styleName: "",
  });
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
    var bodyFormData = new FormData();
    bodyFormData.append("styleName", data.styleName);
  };
  return (
    <>
      <div className="my-5">
        <h2 className="text-center">Appointment</h2>
        <hr className="w-25 mx-auto pt-2" />
      </div>
      <div className="container">
        <div className="row">
          <div className="col-md-4 col-8 mx-auto">
            <form onSubmit={formSubmit}>
              <div class="form-group">
                <label for="styleName">Style</label>
                <select class="form-control" id="styleName">
                  {salonStyles.map((style) => (
                    <option value={style.name}>{style.name}</option>
                  ))}
                </select>
              </div>
              {/* <div className="mb-3">
                <label htmlFor="ApptTime" className="form-label">
                  Time
                </label>
                <input
                  type="time"
                  className="form-control"
                  id="ApptTime"
                  placeholder=""
                  name="ApptTime"
                  value={data.ApptTime}
                  onChange={inputEvent}
                  required
                />
              </div> */}
              <div className="mb-3">
                <a
                  href="/shopprofile"
                  className="btn btn-secondary btn-sm active center"
                  role="button"
                  aria-pressed="true"
                >
                  Make an Appointment
                </a>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  );
};

export default MakeAppointment;
