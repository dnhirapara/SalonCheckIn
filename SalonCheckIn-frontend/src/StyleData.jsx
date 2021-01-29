import React, { useState } from 'react';
import axios from 'axios';

var config = {
	method: 'get',
	url: 'http://localhost:8000/api/service/getservices/',
	headers: {
		Authorization: 'Token ' + localStorage.getItem('token')
	}
};
var Sdata;
// Sdata = [
// 	{
// 		name: 'sherlock cut',
// 		price: '6',
// 		duration: '5'
// 	},
// 	{
// 		name: 'watson cut',
// 		price: '7',
// 		duration: '4'
// 	},
// 	{
// 		name: 'jon snow cut',
// 		price: '7',
// 		duration: '4'
// 	}
// ];
console.log(Sdata);

axios(config)
	.then(function(response) {
		console.log(JSON.stringify(response.data));
		Sdata = JSON.stringify(response.data);
		console.log('inside response');
		console.log(Sdata);
	})
	.catch(function(error) {
		console.log(error);
	});
export default Sdata;
console.log('find');

console.log(Sdata);
