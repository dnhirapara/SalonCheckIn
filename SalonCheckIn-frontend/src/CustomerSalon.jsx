import React from 'react';
import Divider from '@material-ui/core/Divider';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    '& > *': {
      margin: theme.spacing(1),
      width: theme.spacing(16),
      height: theme.spacing(16),
    },
  },
}));

const mycol ={
    'border': '2px solid rgb(20, 31, 62)',
    'height': '225px',
    'background-color':'#141f3e',
    'padding-top': '15px'
}

const styles = {
    // 'border' :'2px solid white',
    'height' : '400px',
    // 'background-color':'grey',
}

const CustomerSalon = () => {
    const classes = useStyles();
    return (
        <>
         <div className="container-fluid fixed" >
    <div className="row">
      <div className="col-md-3 col-sm-12" style={mycol}>
      <div className=" align-item-center" >
      <img src='images/barbershop.jpg' className="align-self-center img-fluid rounded" alt="..."/>
      </div>
     
      </div>
      <div className="col-md-6 mycol col-sm-12" style={mycol}>
       <h3 className="text-white text-capitalize">sherlock salon</h3>
       <p className="text-muted text-capitalize">the game is on</p>
       <span className="text-light text-capitalize ">3rd Eye II, Ellis Bridge, CG Road, Navrangpura</span>
       <p className="text-light text-capitalize ">Appointments Left:<span className="text-danger">&nbsp;5</span></p>

      </div>
      <div className="col-md-3 mycol col-sm-12" style={mycol}>
       <h4 className="text-white text-capitalize text-center">OFFER</h4>
       <hr className="w-75 pt-2 bg-light"/>
       <p className="text-light text-capitalize ">Grab 10% Discount on Corean Cut</p>
       <span className="text-light">5% Discount to 1st Customer </span>
      </div>
    </div>
  </div>
  <div className="container-fluid">
  <div className="row">
     <div className="col-md-7 p-2" style={styles}>
     <h3 className="text-dark text-capitalize text-center">styles</h3>

     <hr className="w-25 mx-auto pt-2"/>
     </div>
      <Divider orientation="vertical" flexItem />
      <div className="col-md-3 p-2" style={styles}>
     
      <h3 className="text-dark text-capitalize text-center">Cart</h3>
      <hr className="w-25 mx-auto pt-2"/>
      </div>
  </div>
  </div>
           
        </>
    )
};

export default CustomerSalon;
