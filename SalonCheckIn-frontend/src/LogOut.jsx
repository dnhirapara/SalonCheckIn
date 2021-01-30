import React, { useState } from 'react';

const LogOut = () => {
	localStorage.removeItem('token');
	window.location = 'http://localhost:3000/';
};

export default LogOut;
