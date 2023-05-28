import React from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

import UploadFiles from "./components/upload-files.component";
import SidebarMenu from "./components/SidebarMenu";

function App() {
  return (
    <div className="container">
      <SidebarMenu />
      <div style={{ margin: "20px 0" }}>
        <div className="radai">
          Upload your
          <ul>
            <li>EHR,</li>
            <li>MRI,</li>
            <li>xRay, or</li>
            <li>CT scan</li>
          </ul>
          To upload and manage multiple documents, 
          create an account
        </div>
        <UploadFiles />
      </div>

    </div>
  );
}

export default App;
