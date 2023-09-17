let cardArray;
// Get the current URL
const currentUrl = window.location.href;

// Use a regular expression to extract the "card" argument
const cardMatches = currentUrl.match(/[?&]card=([^&]+)/);

if (cardMatches) {
    const cardValue = cardMatches[1]; // Extracted card argument
    cardArray = cardValue.split(","); // Split by comma
    console.log("Separated Card Argument:", cardArray);
} else {
    console.log("No 'card' argument found in the URL.");
}

for (let i = 0; i < cardArray.length; i++) {
    let cardId = cardArray[i];
    async function fetchData() {
        try {
            let response = await fetch('http://api.creditdaddy.tech/card/' + cardId);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            let data = await response.json();

            // Intro Offer Details
            let introOfferDetails;
            if (data["intro-offer-details"] !== "") {
                introOfferDetails = data["intro-offer-details"];
            } else {
                introOfferDetails = "This card does not offer a sign up bonus."
            }

            // Card Color
            let cardColours;
            if (data["company-name"] === "Royal Bank of Canada" || data["company-name"] === "RBC") {
                cardColours = ["#0088ff", "#FFF814"];
            }
            else if (data["company-name"] === "Canadian Imperial Bank of Commerce" || data["company-name"] === "CIBC") {
                cardColours = ["#FF0000", "#ff88a3"];
            }
            else if (data["company-name"] === "The Toronto-Dominion Bank" || data["company-name"] === "TD") {
                cardColours = ["#4CF30A", "#58bf76"];
            }
            else {
                cardColours = ["#16BF82", "#2CCAED"];
            }
            document.querySelector("#credit-card-template-bg-1-"+i+" > g > path").setAttribute("style", "fill: " + cardColours[0] + ";");
            document.querySelector("#credit-card-template-bg-2-"+i+" > g > path").setAttribute("style", "fill: " + cardColours[1] + ";");
            console.log(cardColours);

            // Filling in Information
            document.querySelector("#credit-card-company-" + i).innerText = data["company-name"];
            document.querySelector("#credit-card-name-" + i).innerText = data["name"];
            document.querySelector("#avg-apr" + i).innerText = data["avg-apr"].toString() + "%";
            document.querySelector("#cashback" + i).innerText = "Between " + data["min-cashback"].toString() + "%" + " and " + data["max-cashback"].toString() + "%";
            document.querySelector("#foreign-fee" + i).innerText = data["foreign-fee"].toString() + "%";
            document.querySelector("#intro-offer-details" + i).innerText = introOfferDetails;
            document.querySelector("#annual-fee" + i).innerText += data["annual-fee"];
            document.querySelector("#overcharge-fee" + i).innerText += data["overcharge-fee"] + "%";
        } catch (error) {
            console.error('There was a problem fetching the data:', error);
        }
    }

    // Call the function to fetch and log the data
    fetchData();
}