import React from 'react'
import Home from './components/pages/Home';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Register from './components/pages/Register';
import { createTheme, ThemeProvider } from '@mui/material';
import NavBar from './components/misc/NavBar';


const siteTheme = createTheme({
  palette: {
    primary: {
      main: '#353535',
    },
    secondary: {
      main: '#fff',
    }
  }
})

const Index = () => {
  return (
    <ThemeProvider theme={siteTheme}>
      <BrowserRouter>
        <NavBar />
        <Routes>
          <Route index exact path='/' element={<Home />} />
          <Route path='register' element={<Register />} />
          <Route path='*' element={<Home />}/>
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  )
};

const container = document.getElementById("app");
const root = createRoot(container);
root.render(<Index />);