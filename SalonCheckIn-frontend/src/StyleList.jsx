import React from 'react';
import StyleData from './StyleData';
import Style from './Style';
import Navbar2 from './Navbar2';

function nstyle(val,ind)
{
	return (
		<Style name={val.name} price={val.price}  duration={val.duration} key={ind} />
	)
}


const StyleList = ()=>{
    return (
        <>
        <div className="my-5">
			<h3 className="text-center">Your Styles</h3>
            <hr className="w-25 mx-auto pt-2"/>
		</div>
        <div className="container-fluid mb-5">
            <div className="row gy-4">
            <div className="col-10 mx-auto">
            <div className="row">
            {StyleData.map(nstyle)}
            </div>
            </div>
            </div>
        </div>
        </>
    )
}

export default StyleList;
