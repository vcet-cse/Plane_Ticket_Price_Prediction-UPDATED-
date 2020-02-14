import React from 'react';
import gif from './img/airoplane.gif';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
	<div id="page_start">
	    <h1 id="heading"> Flight Ticket Price Prediction </h1>
            <img src={gif} className="App-logo" alt="logo" />
	</div>
	    <a id="start_button" href="predict">Start</a>
	    <a id="about_us" href="#">About_us</a>
      </header>
    </div>
  );
}

export default App;
