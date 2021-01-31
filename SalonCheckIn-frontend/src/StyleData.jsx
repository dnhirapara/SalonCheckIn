import React, { useState } from 'react';
import axios from 'axios';
import api from './Services/api';

var config = {
	headers: {
		Authorization: 'Token ' + localStorage.getItem('token')
	}
};

export const getStyles = () => {
	return api.get('/api/service/getservices/', config)
		.then((res) => {
			console.log(res);
		})
		.catch(error => {
			console.log(error.response);
		});
}
