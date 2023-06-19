import React from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

import SidebarMenu from "./components/SidebarMenu";
import Banner from "./components/Banner";
import UploadSection from "./components/UploadSection";

import React, { useEffect } from 'react';
import './services/signup-auth.js'; // Import the file

function App() {
  return (
    <div className="container">
      <Banner /> {/* Add the Banner component */}
      <div className="content">
        <SidebarMenu />
        <UploadSection />
      </div>
    <div>
      {/* Your other component JSX */}
      <button id="yourSignupBtnIDHere">Signup</button>
    </div>
      
    </div>
  );
}

export default App;
