import React, { useState, useEffect } from "react";
import Shop from "./Shop";
import Navbar2 from "./Navbar2";
import axios from "./HttpCommon";

var times = 0;

function nshop(val, ind) {
  var url = val.url;
  const index = url.indexOf("getsalons");
  url = url.slice(index + 10, url.length - 1);
  return (
    <Shop
      title={val.display_name}
      address={val.address}
      desc={val.description}
      url={url}
      key={ind}
    />
  );
}

const ShopList = () => {
  const [shopData, setshopData] = useState([]);
  var shopDataFromApi = [];
  useEffect(() => {
    axios
      .get("/accounts/getsalons/")
      .then((res) => {
        console.log(res);
        // res.data.map((item) => shopDataFromApi.push(item));
        setshopData(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
    console.log(shopDataFromApi);
  }, []);
  console.log(`Shoplist Called: ${times++}`);

  return (
    <>
      <Navbar2 />
      <div className="my-5">
        <h3 className="text-center">Shops</h3>
        <hr className="w-25 mx-auto pt-2" />
      </div>
      <div className="container-fluid mb-5">
        <div className="row gy-4">
          <div className="col-10 mx-auto">
            <div className="row">{shopData.map(nshop)}</div>
          </div>
        </div>
      </div>
    </>
  );
};

export default ShopList;
