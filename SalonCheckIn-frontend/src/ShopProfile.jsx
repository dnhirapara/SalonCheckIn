import React from 'react'
import Navbar2 from './Navbar2';
import StyleList from './StyleList';


const ShopProfile = () =>{
    return (
        <>
            <Navbar2/>
            <h1 className="text-capitalize text-dark">Welcome to Shop</h1>
            <a className="btn btn-outlined btn-primary" href="/AddStyle" role="button">Add Style</a>
            <StyleList/>
        </>
    )

}

export default ShopProfile;