import React from 'react';
import About from './About';


const Home = () =>{
    return (
        <>
            <div className="row mb-4 container-fluid">
                <div className="col md-6">
                    <img src='./images/login.jpg' className="img-fluid"alt="img" />
                </div>
            </div>
            <About/>
            
        </>
    )
}

export default Home;