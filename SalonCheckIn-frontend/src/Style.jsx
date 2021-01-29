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

export default function Style() {
	const classes = useStyles();

	return (
		<List className={classes.root}>
			<ListItem>
				<ListItemAvatar />
				<ListItemText primary='Red-Hair' secondary='Price: 50/-' />
			</ListItem>
			<ListItem>
				<ListItemAvatar />
				<ListItemText primary='Hair-Cut' secondary='Price: 70/-' />
			</ListItem>
			<ListItem>
				<ListItemAvatar />
				<ListItemText primary='Hair-Cut Corean' secondary='Price-100' />
			</ListItem>
		</List>
	);
}
