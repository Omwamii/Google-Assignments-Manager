import React from 'react';
import Navbar from './Navbar';

function NoPage() {
    return (
        <div>
        <Navbar />
          <h1>404 - Page Not Found</h1>
          <p>The page you are looking for does not exist.</p>
        </div>
      );
}

export default NoPage;