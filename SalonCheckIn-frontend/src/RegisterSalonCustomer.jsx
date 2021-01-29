import React, { useState } from 'react'
import axios from 'axios';
import Alert from './Alert';
import { Redirect, Route, Switch } from 'react-router-dom/cjs/react-router-dom.min';





const RegisterSalonCustomer = (props) => {

    const [data,setData]=useState({
        Name:"",
        pass:"",
        cpass:"",
        address:"",
        email:"",
        type:(props.type==='Shop'?'2':'1'),
    });

    const inputEvent = (event)=>{
       
        const {name,value}=event.target;
        setData((prev)=>{
            return {
                ...prev,
                [name]:value,
            }
        })
    }

    const formSubmit = (e)=>{
        e.preventDefault();
        var bodyFormData = new FormData();
        bodyFormData.append('email', data.email);
        bodyFormData.append('password', data.pass);
        bodyFormData.append('password2', data.cpass);
        bodyFormData.append('username', data.Name);
        bodyFormData.append('role', data.type);
       
        axios.post('http://127.0.0.1:8000/api/accounts/register',bodyFormData).then(res=>{
            let result = res.data;
            console.log(result);
            if(typeof result["username"]=='undefined'||typeof result["email"]=='undefined')
            {
                console.log("result");
                if(typeof result["username"]=='undefined')
                {
                    props.Show(result["email"]);
                }
                else if(typeof result["email"]=='undefined')
                {
                    props.Show(result["username"]);
                }
            }
            else
            {
                console.log("hello");
                window.location = "http://localhost:3000/login";
            }
        }).catch(e=>{
            console.log("error");
            console.log(e);
            props.Show(e.response.data['password'][0]);
        });
    }
    return (
        <>

        <div className="my-5">
            <h2 className="text-center">Register {props.type}</h2>
            <hr className="w-25 mx-auto pt-2"/>
        </div>
        <div className="container">
            <div className="row">
                <div className="col-md-6 col-10 mx-auto">
                <form onSubmit={formSubmit}>
                    <div className="mb-3">
                        <label htmlFor="exampleFormControlInput1" className="form-label">{props.type} Name</label>
                        <input type="text" className="form-control" id="exampleFormControlInput1" name="Name" value={data.Name} onChange={inputEvent} placeholder="Name" required/>
                    </div>
                    <div className="mb-3">
                        <label htmlFor="exampleFormControlInput1" className="form-label">Email address</label>
                        <input type="email" className="form-control" id="exampleFormControlInput2" name="email" value={data.email} onChange={inputEvent} placeholder="name@example.com" required/>
                    </div>
                    <div className="mb-3">
                        <label htmlFor="inputPassword4" className="form-label">Password</label>
                        <input type="password" className="form-control" id="inputPassword4" name="pass" value={data.pass} onChange={inputEvent} required/>
                    </div>
                    <div className="mb-3">
                        <label htmlFor="inputPassword4" className="form-label">Confirm Password</label>
                        <input type="password" className="form-control" id="inputPassword5" name="cpass" value={data.cpass} onChange={inputEvent} required/>
                    </div>
                    <div className="mb-3">
                        <label htmlFor="exampleFormControlTextarea1" className="form-label">Address</label>
                        <textarea className="form-control" id="exampleFormControlTextarea1" rows="3" name="address" value={data.address} onChange={inputEvent} required></textarea>
                    </div>
                    <div className="mb-3">
                        <button className="btn btn-outline-secondary" type="submit">Submit</button>
                    </div>
                </form>
                </div>
            </div>
        </div>

        </>
    )
    }

export default RegisterSalonCustomer;