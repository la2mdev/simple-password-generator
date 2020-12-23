const length = document.querySelector("input[type='range']");
const container = document.querySelector(".toast-container");

length.addEventListener("click", () => {
    showLength();
});

const showLength = () => {
    const notification = document.createElement("div");
    notification.classList.add("toast");
    notification.innerText = length.value;

    container.appendChild(notification);

    setTimeout(() => {
        notification.remove();
    }, 2000);
}
