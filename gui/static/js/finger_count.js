// * Variables
const timer = document.querySelector("#timer");
const target = document.querySelector("#target");
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
        window.location = "/";
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
    // TODO For some reason this is different from the file read.
    console.log(obj);
    target.innerHTML = obj.target;
}