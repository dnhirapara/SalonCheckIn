import React,{useState} from 'react'
import axios from 'axios'
import Alert from './Alert';
import { Redirect, Route, Switch } from 'react-router-dom/cjs/react-router-dom.min';
import Navbar from './Navbar';



const Login = () =>{
    const [data,setData]=useState({
        pass:"",
        email:"",
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
        alert(` ${data.email} ${data.pass} `);
        var bodyFormData = new FormData();
        bodyFormData.append('username', data.email);
        bodyFormData.append('password', data.pass);
    
        axios.post('http://127.0.0.1:8000/api/accounts/login',bodyFormData).then(res=>{
            let result = res.data;
            console.log(result['token']);
            localStorage.setItem('token',result['token']);
            window.location = "http://localhost:3000/shoplist";

        }).catch(e=>{
            console.log(e.response.data.non_field_errors);
            alert(e.response.data.non_field_errors)
            // <Alert response={e.response.data.non_field_errors}/>
        });
    }
    return (
        <>
            <Navbar/>
            <div className="my-5">
                <h2 className="text-center">Login</h2>
                <hr className="w-25 mx-auto pt-2"/>
            </div>
            <div className="container">
            <div className="row">
                <div className="col-md-4 col-8 mx-auto">
                <form onSubmit={formSubmit}>
                    <div className="mb-3">
                        <label htmlFor="exampleFormControlInput1" className="form-label">Email Address</label>
                        <input type="email" className="form-control" id="exampleFormControlInput1"  placeholder="name@example.com" name="email" value={data.email} onChange={inputEvent} required/>
                    </div>
                    <div className="mb-3">
                        <label htmlFor="inputPassword4" className="form-label">Password</label>
                        <input type="password" className="form-control" id="inputPassword4" name="pass" value={data.pass} onChange={inputEvent} required/>
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

export default Login;