import React from 'react';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../node_modules/bootstrap/dist/js/bootstrap.bundle';
// const img1 = 'https://source.unsplash.com/300x200/?salon,scissors';


function Shop(props) {
	return (
		<>
			
		<div className="col-md-4 col-10 mx-auto my-2">
			<div className="card">
				<img src='images/barbershop.jpg' className="card-img-top" alt="..."/>
				<div className="card-body">
					<h5 className="card-title">{props.title}</h5>

					<span className="card-text text-black-50">Appointments: <span  className="text-success">{props.appointment}</span></span>
					<p className="card-text">Styles: <span className="text-success" >{props.style}</span></p>
					<NavLink to="#" className="btn btn-outline-info ">Proceed</NavLink>
  				</div>
			</div>
		</div>
		</>
	);
}

export default Shop;
