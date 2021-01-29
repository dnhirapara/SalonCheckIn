import React from 'react';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../node_modules/bootstrap/dist/js/bootstrap.bundle';
// const img1 = 'https://source.unsplash.com/300x200/?salon,scissors';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';


const useStyles = makeStyles({
	root: {
		maxWidth: 345
	},
	media: {
		height: 140
	}
});



function Shop(props) {
	const classes = useStyles();
	return (
		<>
		<div className="col-md-4 col-10 mx-auto my-2">
			{/* <div className="card">
				<img src='images/barbershop.jpg' className="card-img-top" alt="..."/>
				<div className="card-body">
					<h5 className="card-title">{props.title}</h5>

					<span className="card-text text-black-50">Appointments: <span  className="text-success">{props.appointment}</span></span>
					<p className="card-text">Styles: <span className="text-success" >{props.style}</span></p>
					<NavLink to="#" className="btn btn-outline-info ">Proceed</NavLink>
  				</div>
			</div> */}
			<Card className={classes.root}>
			<CardActionArea>
				<CardMedia
					className={classes.media}
					image='images/barbershop.jpg'
					title='Contemplative Reptile'
				/>
				<CardContent>
					<Typography gutterBottom variant='h5' component='h2'>
						{props.title}
					</Typography>
					<Typography variant='body2' color='textSecondary' component='p'>
						Appointments:  <span  className="text-success">{props.appointment}</span>
						
					</Typography>
					<Typography variant='body3' color='textSecondary' component='p'>
					Styles: <span className="text-success" >{props.style}</span>
					</Typography>

				</CardContent>
			</CardActionArea>
			<CardActions>
				<Button size='small' color='secondary'>
					Proceed
				</Button>
			</CardActions>
		</Card>
		</div>
		</>
	);
}

export default Shop;
