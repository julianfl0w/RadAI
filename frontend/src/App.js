import React from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

import SidebarMenu from "./components/SidebarMenu";
import Banner from "./components/Banner";
import UploadSection from "./components/UploadSection";


function App() {
  return (
    <div className="container">
      <Banner /> {/* Add the Banner component */}
      <div className="content">
        <SidebarMenu />
        <UploadSection />
      </div>
    </div>
  );
}

export default App;
