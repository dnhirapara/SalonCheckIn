import React from 'react';
import ShopListData from './ShopListData';
import Shop from './Shop';
import Navbar from './Navbar';

function nshop(val,ind)
{
	return (
		<Shop title={val.title} appointment={val.appointments} style={val.styles} key={ind} />
	)
}


const ShopList = ()=>{
    return (
        <>
        <Navbar/>	
        <div className="my-5">
			<h3 className="text-center">Shops</h3>
            <hr className="w-25 mx-auto pt-2"/>
		</div>
        <div className="container-fluid mb-5">
            <div className="row gy-4">
            <div className="col-10 mx-auto">
            <div className="row">
            {ShopListData.map(nshop)}
            </div>
            </div>
            </div>
        </div>
        </>
    )
}

export default ShopList;
