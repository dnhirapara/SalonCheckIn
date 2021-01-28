import React from 'react'
import RegisterSalonCustomer from './RegisterSalonCustomer';
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "../node_modules/bootstrap/dist/js/bootstrap.bundle";

import Alert from './Alert';

const RegisterCustomer = () =>{

    const showAlert = (al)=>
    {
        alert(al);
        return (<Alert response={al}/>)
    }
    return (
        <>
            <RegisterSalonCustomer type="Customer" Show={showAlert}/>
        </>
    )
}

export default RegisterCustomer;