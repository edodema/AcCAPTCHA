// * Variables.
const img = document.querySelector("#img");
const submit = document.querySelector("#submit");
// Path and choices.
const path = "static/logs/image_classification.json";
const labels = [
    document.querySelector("#l0"),
    document.querySelector("#l1"),
    document.querySelector("#l2"),
    document.querySelector("#l3")
]
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

    // Populate radio buttons.
    for (let i = 0; i < obj.choices.length; i++) {
        let choice = labels[i];
        // Add value to both ri and li.
        radio = document.querySelector("#" + choice.attributes.for.value)
        radio.value = obj.choices[i];
        choice.innerHTML = obj.choices[i];
    }
}

function check_test() {
    const value = document.querySelector("input[name='answers']:checked").value;

    if (value == obj.truth) {
        // TODO: Page that says "the test is finished".
        alert("The test is passed. You will be redirected to the home page.");
        // Go back to another page.
        // TODO: I temporarily set the homepage.
        window.location = window_alert;
    }
}