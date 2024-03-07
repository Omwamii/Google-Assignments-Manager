import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

const url = 'http://localhost:8000/';

const Home = () => {
    const [pendingWork, setPendingWork] = useState([]);
    
}