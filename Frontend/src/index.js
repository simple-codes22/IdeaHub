import React from 'react'
import Home from './components/pages/Home';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

const Index = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route index exact path='/' element={<Home />} />
        <Route path='*' element={<p>Wrong page</p>} />
      </Routes>
    </BrowserRouter>
  )
};

const container = document.getElementById("app");
const root = createRoot(container);
root.render(<Index />);