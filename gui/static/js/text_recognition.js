// * Variables.
const img = document.querySelector("#img");
const tbox = document.querySelector("#tbox");
const submit = document.querySelector("#submit");
// Path and choices.
const path = "static/logs/text_recognition.json";
// JSON object.
let obj;
// The page to which we will be redirected after an alert.
const window_alert = "/";

// * Listeners.
submit.addEventListener("click", check_test);

// * Functions.
async function get_data() {
    // Load JSON file.
    const res = await fetch(path)
    obj = await res.json();

    // Display image.
    img.src = obj.path;
    console.log(obj.truth);
}

function check_test() {
    if (tbox.value == obj.truth) {
        alert("The test is passed. You will be redirected to the home page.");
    } else {
        alert("The test has not been passed. You will be redirected to the home page.");
    }
    // Go back to another page.
    window.location = window_alert;
}