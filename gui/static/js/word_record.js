// * HTML
// * Variables
const window_alert = "/";

// * Functions.
async function check_test() {
    let obj;
    const res = await fetch(path)
    obj = await res.json();

    // The test is passed, go back somewhere.
    let txt_alert = "";
    console.log(obj.passed)
    if (obj.passed == 0) {
        txt_alert = "The test has not been passed.";
    }
    else if (obj.passed == 1) {
        txt_alert = "The test is passed."
    }

    // * Alert and redirection.
    txt_alert += " You will be redirected to the home page."
    alert(txt_alert);
    // Go back to another page.
    window.location = window_alert;
}