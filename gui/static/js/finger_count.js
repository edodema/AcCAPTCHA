// * Variables
const timer = document.querySelector("#timer");
const target = document.querySelector("#target");
// The page to which we will be redirected after an alert.
const window_alert = "/";
// 5 minutes.
let duration = 5 * 60;
// JSON file path.
const path = "static/logs/finger_count.json";


// * Function.
// Display a countdown on screen.
function countdown() {
    if (duration < 0) {
        alert("Time expired. Please take another test.");
        // Go back to another page.
        // TODO: I temporarily set the homepage.
        window.location = window_alert;
    }
    // Display minutes and seconds.
    let minutes = Math.floor((duration / 60));
    let seconds = Math.floor((duration % 60));

    timer.innerHTML = minutes + "m" + seconds + "s";

    // Decrement for next cycle.
    duration--;
}

// Retrieve the number that should be shown with fingers and display it.
async function show_target() {
    // Load JSON file.
    let obj;
    const res = await fetch(path)
    obj = await res.json();

    // Show target number.
    target.innerHTML = obj.target;
}

async function check_test() {
    // Load JSON file.
    let obj;
    const res = await fetch(path)
    obj = await res.json();

    // The test is passed, go back somewhere.
    if (obj.passed == 1) {
        // TODO: Page that says "the test is finished".
        alert("The test is passed. You will be redirected to the home page.");
        // Go back to another page.
        // TODO: I temporarily set the homepage.
        window.location = window_alert;
    }
}

// ! Alternative that uses JQuery, should be bette but an internet connection is needed.
// function show_target() {
//     $.getJSON(path, function (json) {
//         target.innerHTML = json.target;
//     });
// }