//  * Variables.
// Checkboxes.
const sight_cb = document.querySelector("#sight");
// Button.
const submit_bt = document.querySelector("#submit");

// * Listeners.
submit_bt.addEventListener("click", () => {
    let checkboxes = document.querySelectorAll("input[name='mode']");
    let values = new Object();
    checkboxes.forEach((checkbox) => {
        values[checkbox.id] = checkbox.checked;
    });
    // TODO: Save this object as a json in logs.
    console.log(values)
});