// Banner.js

import UploadFiles from "./upload-files.component";

function UploadSection() {
  return(
  <div style={{ width: "100%" }}>
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
  )
}

export default UploadSection;
