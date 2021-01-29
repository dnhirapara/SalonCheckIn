import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';

const useStyles = makeStyles((theme) => ({
	root: {
		width: '100%',
		maxWidth: 360,
		backgroundColor: theme.palette.background.paper
	}
}));

export default function Appointment() {
	const classes = useStyles();

	return (
		<List className={classes.root}>
			<ListItem>
				<ListItemAvatar />
				<ListItemText primary='Appointment-1' secondary='10:00 AM to 11:00 AM' />
			</ListItem>
			<ListItem>
				<ListItemAvatar />
				<ListItemText primary='Appointment-2' secondary='11:00 AM to 12:00 Noon' />
			</ListItem>
			<ListItem>
				<ListItemAvatar />
				<ListItemText primary='Appointment-3' secondary='12:00 Noon to 1:00 PM' />
			</ListItem>
		</List>
	);
}
