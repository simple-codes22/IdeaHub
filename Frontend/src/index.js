import React from 'react'
import { render } from "react-dom";

const Index = () => {
  return (
    <div>index</div>
  )
};

const container = document.getElementById("app");
render(<Index />, container);