// import DuoAuthn auth methods
const { startLogin } = DuoAuthn;
/**
 * Login Button
 */
document
  // 5. EDIT your Login button html 'id' below
  .getElementById("yourLoginBtnIDHere")
  .addEventListener("click", async () => {
    /* Generate login options for your user */
    // 6. EDIT this fetch request your route that will make the api request to our server
    const resp = await fetch("/your-login-route-here");
    const opts = await resp.json();
    // Start bloc Login
    let authResp;
    try {
      authResp = await startLogin(opts);
    } catch (err) {
      throw new Error(err);
    }
    /* Send response to server */
    // 7. EDIT this fetch request your route that will make the api request to our server
    const verificationResp = await fetch("/your-verify-login-route-here", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(authResp),
    });
    // Report validation response
    const verificationRespJSON = await verificationResp.json();
    const { verified, msg } = verificationRespJSON;
    if (verified) {
      /* Redirect to your "login required" page */
      // 8. EDIT this location to redirect the user to your login required page
      window.location = "/your/redirect/location/here";
    } else {
      console.log("not authenticated");
    }
  });
