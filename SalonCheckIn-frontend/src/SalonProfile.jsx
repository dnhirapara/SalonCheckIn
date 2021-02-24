import React from 'react';
import axios from 'axios';
import Alert from './Alert';
import { Redirect, Route, Switch } from 'react-router-dom/cjs/react-router-dom.min';
import Navbar2 from './Navbar2';
import TimeLine from './TimeLine';

const SalonProfile = () => {
    return (
        <>
        <Navbar2/>
        <TimeLine/>


        </>
    );
};

export default SalonProfile;
