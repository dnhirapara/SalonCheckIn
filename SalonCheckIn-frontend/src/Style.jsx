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



function Style(props) {
	const classes = useStyles();
	return (
		<>
		<div className="col-md-4 col-10 mx-auto my-2">
			<Card className={classes.root}>
			<CardActionArea>
				<CardMedia
					className={classes.media}
					image='images/barbershop.jpg'
					title='Contemplative Reptile'
				/>
				<CardContent>
				<Typography variant='body3' color='textSecondary' component='p'>
				Name: <span className="text-dark" >{props.name}</span>
					</Typography>
					<Typography variant='body2' color='textSecondary' component='p'>
						Price:  <span  className="text-success">{props.price} Rs.</span>
						
					</Typography>
					<Typography variant='body3' color='textSecondary' component='p'>
				Duration: <span className="text-success" >{props.duration} minutes</span>
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

export default Style;
