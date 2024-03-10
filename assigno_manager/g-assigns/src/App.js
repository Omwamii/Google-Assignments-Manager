import React from 'react'; // Import React

import './App.css';
import './index.css';
// import Grades from './Grades';
import Navbar from './Navbar';
import Notifs from './Notifs';
import Home from './Home';
import Grades from './Grades';
import "primereact/resources/themes/vela-blue/theme.css"; // This imports theme.css from primereact themes module
import "primereact/resources/primereact.min.css"; // This imports primereact main css
import "primeicons/primeicons.css"; 
import 'primeflex/primeflex.css'; 
// import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  return (
    <div className='App'>
      <Navbar />
      {/* <Notifs /> */}
      <Grades />
      {/* <Home /> */}
      {/* <Notifs /> */}
    </div>
  );
}

export default App;