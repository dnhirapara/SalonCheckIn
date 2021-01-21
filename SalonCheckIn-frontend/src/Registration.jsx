import React from 'react'
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';

const img1={
    'width':'1000px',
    'height': '390px',
    'marginTop':'30px'
}

const img2={
    'width':'1000px',
    'height': '400px',
    'marginTop':'20px'
}

const Registration = () =>{
    return (
        <>
        <div className="container-fluid about">
            <h1 className="text-center text-capitalize">Register</h1>
            <hr className="w-50 mx-auto pt-4"/>
            <div className="row mb-5">
                <div className="col-lg-6 col-md-6">
                    <h5 className="card-title text-lg-center">Salon</h5>
                    <div className="card" style={{'width': '18 rem'}}>
                        <img src="images/tools.jpg" style={img1} className="card-img-top img-fluid" alt="..."/>
                        <div className="card-body text-center">
                        <NavLink to="/register/salon" className="btn btn-primary" >Register</NavLink>
                        </div>
                    </div>
                </div>
                <div className="col-lg-6 col-md-6 ">
                    <h5 className="card-title text-lg-center">Customer</h5>
                    <div className="card" style={{'width': '18 rem'}}>
                        <img src="images/haircut.svg" style={img2} className="card-img-top img-fluid" alt="..."/>
                        <div className="card-body text-center">
                        <NavLink to="/register/customer" className="btn btn-primary">Register</NavLink>
                        </div>
                    </div>
                    
                </div>
            </div>
        </div>    
        </>
    )
}

export default Registration;