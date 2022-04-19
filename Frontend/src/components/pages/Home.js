import { Box } from '@mui/material';
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { makeStyles } from '@mui/styles';
import axios from 'axios';
// import { GetIdeas, GetUsers } from '../../client/fetchFile';

const homeStyle = makeStyles(theme => ({
    /* Styling for the home page(component) */
    root: {
        
    }
}))

const Home = (prop) => {
    // This is basically the default page for the frontend web app
    
    const useStyle = homeStyle(); // Making the styles ready for use in the component
    
    const [getIdeas, setIdeas] = useState();
    
    useEffect(() => {
        // Fetching the total list of ideas from the database
        axios.get('/api/v1/ideas')
        .then(resp => {
            return setIdeas(resp.data)
        })
        .catch(err => {
            return setIdeas(err)
        })
    }, [prop.id])

    console.log(getIdeas); // Just checking if the idea list was fetched properly

    return (
        <Box component='section' className={useStyle.root}>
            {getIdeas !== undefined ? getIdeas.map(elem => {
                return (
                    <Box component='div' key={elem.idea_id}>
                        {elem.title}
                    </Box>
                )
            }) : <></>}
        </Box>
    )
}

export default Home