import React from 'react';
import { Redirect, Route, Switch } from 'react-router-dom/cjs/react-router-dom.min';
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "../node_modules/bootstrap/dist/js/bootstrap.bundle";
import './index.css';
import Home from './Home';
import Registration from './Registration';
import Login from './Login';
import ShopProfile from './ShopProfile';
import CustomerProfile from './CustomerProfile';
import Footer from './Footer';
import RegisterCustomer from './RegisterCustomer';
import RegisterSalon from './RegisterSalon';
import ShopList from './ShopList';
import CustomerSalon from './CustomerSalon';
import AddStyle from './AddStyle';
import LogOut from './LogOut';
import MakeAppointment from './MakeAppointment';
import SalonProfile from './SalonProfile';
// import CustomerSalon from './CustomerSalon'


const App = () =>{
    return (
        <>
        <Switch>
            <Route exact path="/" component={Home}/>
            <Route exact path="/register" component={Registration}/>
            <Route exact path="/register/salon" component={RegisterSalon}/>
            <Route exact path="/register/customer" component={RegisterCustomer}/>
            <Route exact path="/login" component={Login}/>
            <Route exact path="/shoplist" component={ShopList}/>
            <Route exact path="/#about" component={Home}/>
            <Route exact path="/addstyle" component={AddStyle}/>
            <Route exact path="/salonprofile" component={SalonProfile}/>
            <Route exact path="/logout" component={LogOut}/>
            <Route exact path="/appointment" component={MakeAppointment}/>
            <Route exact path="/shopprofile" component={CustomerSalon}/>
            <Route exact path="/customerprofile" component={CustomerProfile}/>
            <Route exact path="/salon" component={CustomerSalon}/>
            <Redirect to="/"/>
        </Switch>
        <Footer/>
        </>
    )
}

export default App;