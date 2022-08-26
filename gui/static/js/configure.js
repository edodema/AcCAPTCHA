//  * Variables.
var inputs = document.getElementsByTagName('input');
// We want all boxes to be unchecked to avoid inequalities.
for (var i = 0; i < inputs.length; i++) {
    if (inputs[i].type == 'checkbox') {
        inputs[i].checked = false;
    }
}

// Button.
const submit_bt = document.querySelector("#submit");

// Checkboxes values.
let values = new Object();

// * Listeners.
submit_bt.addEventListener("click", () => {
    let checkboxes = document.querySelectorAll("input[name='mode']");
    checkboxes.forEach((checkbox) => {
        values[checkbox.id] = + checkbox.checked;
    });
    check_mode();
});

// * Functions.
function check_mode() {
    // We want to be conservative, thus the user has to choose modalities explicitly.
    // ? Hearing is a bit problematic, how can you give an input to a computer?
    // ? Is sight necessary?
    let tests = {
        finger_count: values.sight * values.camera * values.gesture,
        image_classification: values.sight * values.mouse,
        text_recognition: values.sight * values.keyboard,
        word_reading: values.sight * values.speech * values.microphone
    };

    // Get methods that can be used.
    let doable_tests = [];
    for (let key in tests) {
        if (tests[key] == 1) {
            doable_tests.push(key);
        }
    }

    // Given that list, now sample one method randomly and get redirected.
    if (doable_tests.length <= 0) {
        alert("The combination you chose is not valid. Please, choose another.");
        window.location = "/";
    } else {
        // Pick a random test.
        const test_idx = Math.floor(Math.random() * doable_tests.length);
        const window_test = doable_tests[test_idx];
        console.log(window_test);
        window.location = window_test;
    }
}