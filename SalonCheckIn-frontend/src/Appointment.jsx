import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import ListItemAvatar from "@material-ui/core/ListItemAvatar";

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
    maxWidth: 360,
    backgroundColor: theme.palette.background.paper,
    display: "block",
  },
}));

export default function Appointment(props) {
  const classes = useStyles();
  console.log("In appointments: timepass");
  console.log(props.data);
  return (
    <List className={classes.root}>
      <ListItem>
        {props.data.map((res) => (
          <ListItemText
            primary={`Appointment ${res.service}: ${res.status}`}
            secondary={`${res.date}`}
          />
        ))}
      </ListItem>
    </List>
  );
}
