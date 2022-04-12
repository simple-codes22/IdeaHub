import React from 'react';
import { Box, Toolbar, AppBar } from '@mui/material';
import { makeStyles } from '@mui/styles';

const navBarStyle  = makeStyles(theme => ({
    /* Styling for the navigation bar */
    intro: {
        fontFamily: "Ms Madi, cursive",
        fontSize: '1.9rem',
        letterSpacing: '1.2px',
    }
}))

const NavBar = () => {
    
    const useStyle = navBarStyle(); // Declaration for the navBarStyle

    return (
        <Box component='div'>
            <AppBar position='static' >
                <Toolbar>
                    <Box component='div' className={useStyle.intro}>
                        IdeaHub
                    </Box>
                </Toolbar>
            </AppBar>
        </Box>
    )
}

export default NavBar