import React from 'react';
import Navbar from './Navbar';

function NoPage() {
    return (
        <div>
        <Navbar />
        <div className='app-content'>
        <h1 className='disp-text'>404 - Page Not Found</h1>
          <h2 className='disp-text' id="desc">The page you are looking for does not exist.</h2>
        </div>
        </div>
      );
}

export default NoPage;