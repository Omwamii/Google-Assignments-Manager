import React from 'react'; 

import "primereact/resources/themes/lara-light-indigo/theme.css";
import "primereact/resources/primereact.min.css";
import "primeicons/primeicons.css"; 
import 'primeflex/primeflex.css'; 
import './App.css';
import './index.css';

import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Grades from './Grades';
import Home from './Home';
import Navbar from './Navbar';
import Notifs from './Notifs';
import Stats from './Stats';

// import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <Navbar />
      <div className="app-content">
      <Stats />
        {/* <Grades /> */}
        {/* <Home /> */}
        {/* <Notifs /> */}
      </div>
    </div>
  );
}

export default App;