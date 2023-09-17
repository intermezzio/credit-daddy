const creditCardContainer = document.querySelector(".credit-card-template");

creditCardContainer.addEventListener("mouseenter", () => {
    creditCardContainer.classList.add("hovered"); // Apply 3D effect on hover
});

creditCardContainer.addEventListener("mouseleave", () => {
    creditCardContainer.classList.remove("hovered"); // Remove 3D effect on hover out
    creditCardContainer.style.transform = `rotateX(0deg) rotateY(0deg)`;

});

creditCardContainer.addEventListener("mousemove", (event) => {
    const cardRect = creditCardContainer.getBoundingClientRect();
    const mouseX = event.clientX - cardRect.left;
    const mouseY = event.clientY - cardRect.top;

    const rotationX = (mouseY / cardRect.height - 0.5) * 100; // Adjust rotation based on mouse position
    const rotationY = (mouseX / cardRect.width - 0.5) * 100;

    creditCardContainer.style.transform = `rotateX(${rotationX}deg) rotateY(${rotationY}deg)`;
});

let cardId = "cibc-aventura-visa-infinite-privilege";

// URL Modification
let currentUrl = window.location.href; // Get the current URL

if (!currentUrl.includes("?card")) {
    currentUrl += `?card=${cardId}`;
}
window.history.pushState({ cardId: cardId }, "", currentUrl);

async function fetchData() {
    try {
        const response = await fetch('http://api.creditdaddy.tech/card/' + cardId);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();

        // Intro Offer Details
        let introOfferDetails;
        if (data["intro-offer-details"] !== "") {
            introOfferDetails = data["intro-offer-details"];
        } else {
            introOfferDetails = "This card does not offer a sign up bonus."
        }

        // Card Color
        let cardColours;
        if (data["company-name"] === "Royal Bank of Canada") {
            cardColours = ["#0088ff", "#FFF814"];
        }
        else if (data["company-name"] === "Canadian Imperial Bank of Commerce") {
            cardColours = ["#FF0000", "#ff88a3"];
        }
        else if (data["company-name"] === "The Toronto-Dominion Bank") {
            cardColours = ["#4CF30A", "#FFFFFF"];
        }
        else {
            cardColours = ["#16BF82", "#2CCAED"];
        }
        document.querySelector("#credit-card-template-bg-1 > g > path").setAttribute("style", "fill: " + cardColours[0] + ";");
        document.querySelector("#credit-card-template-bg-2 > g > path").setAttribute("style", "fill: " + cardColours[1] + ";");

        // Filling in Information
        document.querySelector("#company-name").innerText = data["company-name"];
        document.querySelector("#name").innerText = data["name"];
        document.querySelector("#name").innerText = data["name"];
        document.querySelector("#avg-apr").innerText = data["avg-apr"].toString() + "%";
        document.querySelector("#cashback").innerText = "Between " + data["min-cashback"].toString() + "%" + " and " + data["max-cashback"].toString() + "%";
        document.querySelector("#intro-offer-details").innerText = introOfferDetails;
        document.querySelector("#annual-fee").innerText += data["annual-fee"];
        document.querySelector("#overcharge-fee").innerText += data["overcharge-fee"];
    } catch (error) {
        console.error('There was a problem fetching the data:', error);
    }
}

// Call the function to fetch and log the data
fetchData();
