import React, { useState } from 'react';
import axios from 'axios';

var config = {
	method: 'get',
	url: '/service/getservices/',
	headers: {
		Authorization: 'Token ' + localStorage.getItem('token')
	}
};
let Sdata = [];
// Sdata = [
// 	{
// 		name: 'sherlock cut',
// 		price: '6',
// 		tags: [ 'hair cut', 'spa' ],
// 		duration: '5'
// 	},
// 	{
// 		name: 'watson cut',
// 		price: '7',
// 		tags: [ 'hair cut', 'spa' ],
// 		duration: '4'
// 	},
// 	{
// 		name: 'jon snow cut',
// 		price: '7',
// 		tags: [ 'hair cut', 'spa' ],
// 		duration: '4'
// 	}
// ];

console.log(Sdata);

console.log(typeof Sdata);

export const getStyles = ()=>{
	return axios(config)
	.catch(function(error) {
		console.log(error);
	});
}

axios(config)
	.then(function(response) {
		console.log(typeof response);
		console.log(JSON.stringify(response.data));
		response.data.forEach((element) => {
			Sdata.push(element);
		});
		// Sdata.push(response.data);
		// console.log('inside response');
		// if (Math.random() % 2 == 0) console.log(Sdata);
	})
	.catch(function(error) {
		console.log(error);
	});

console.log('find');

console.log(Sdata);

// export default Sdata;
