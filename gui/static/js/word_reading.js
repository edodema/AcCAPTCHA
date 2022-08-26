// * HTML
const words = document.querySelector("#words");
const record = document.querySelector("#record");
// * Variables
const path = "static/logs/word_reading.json";
const window_record = "/word_record";
let obj;

// * Listeners.
record.addEventListener("click", start_record);


// * Functions.
async function get_words() {
    // Load JSON file.
    const res = await fetch(path)
    obj = await res.json();

    // Combine words in a sentence.
    let txt = "";
    for (i in obj.truth) {
        txt += obj.truth[i] + "<br>";
    }
    // Show text on web page.
    words.innerHTML = txt;
}

function start_record() {
    window.location = window_record;
}