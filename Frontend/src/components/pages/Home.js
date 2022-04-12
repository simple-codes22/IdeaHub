import { Box } from '@mui/material';
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { makeStyles } from '@mui/styles';
import { GetIdeas, GetUsers } from '../../client/fetchFile';

const homeStyle = makeStyles(theme => ({
    /* Styling for the home page(component) */
}))

const Home = () => {
    // This is basically the default page for the frontend web app
    return (
        <Box component='div'>
            
        </Box>
    )
}

export default Home