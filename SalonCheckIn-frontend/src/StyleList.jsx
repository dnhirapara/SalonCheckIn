import React, { useState } from "react";
import { getStyles } from "./StyleData";
import Style from "./Style";
import Navbar2 from "./Navbar2";
import Sdata from "./ShopListData";

function nstyle(val, ind) {
  return (
    <Style
      name={val.name}
      price={val.price}
      duration={val.duration}
      key={ind}
    />
  );
}

const StyleList = () => {
  const [styleData, setstyleData] = useState([]);

  let SData = [];

  getStyles().then(function (response) {
    console.log(typeof response);
    console.log(JSON.stringify(response.data));
    response.data.forEach((element) => {
      Sdata.push(element);
    });
    setstyleData(Sdata);
  });
  return (
    <>
      <div className="my-5">
        <h3 className="text-center">Your Styles</h3>
        <hr className="w-25 mx-auto pt-2" />
      </div>
      <div className="container-fluid mb-5">
        <div className="row gy-4">
          <div className="col-10 mx-auto">
            <div className="row">{styleData.map(nstyle)}</div>
          </div>
        </div>
      </div>
    </>
  );
};

export default StyleList;
