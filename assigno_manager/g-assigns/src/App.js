import React from 'react'; 

import "primereact/resources/themes/lara-light-indigo/theme.css";
import "primereact/resources/primereact.min.css";
import "primeicons/primeicons.css"; 
import 'primeflex/primeflex.css'; 
import './index.css';

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Grades from './Grades';
import Home from './Home';
import Notifs from './Notifs';
import Stats from './Stats';
import NoPage from './NoPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<Home />}></Route>
        <Route path="/notifications" element={<Notifs />}></Route>
        <Route path="/grades" element={<Grades />}></Route>
        <Route path="/stats" element={<Stats />}></Route>
        <Route path="*" element={<NoPage />} />
      </Routes>
    </BrowserRouter>
  )
}
export default App;