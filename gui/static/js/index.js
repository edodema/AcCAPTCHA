// * Variables.
const article = document.querySelector("#content");
const read_bt = document.querySelector("#read-more");
const start_bt = document.querySelector("#start");

// * Listeners.
read_bt.addEventListener("click", read_more);
start_bt.addEventListener("click", redirect);

function read_more() {
    if (article.className == "open") {
        // Read less.
        article.className = "";
        read_bt.innerHTML = "Show more";
    } else {
        // Read more.
        article.className = "open";
        read_bt.innerHTML = "Show less";
    }
};

function redirect() {
    window.location = "configure";
}
