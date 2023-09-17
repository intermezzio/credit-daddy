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

let cardId;
const currentUrl = window.location.href;
const queryString = currentUrl.split("?")[1]; // Get the part of the URL after the "?"
if (queryString) {
    const params = queryString.split("&"); // Split parameters by "&"
    for (const param of params) {
        const [key, value] = param.split("=");
        if (key === "card") {
            cardId = decodeURIComponent(value); // Decode the value
            break; // Exit the loop once "card" parameter is found
        }
    }
}

let cardData;
async function fetchData() {
    try {
        const response = await fetch('http://api.creditdaddy.tech/card/' + cardId);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        cardData = data;
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
            cardColours = ["#4CF30A", "#58bf76"];
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
        document.querySelector("#foreign-fee").innerText = data["foreign-fee"].toString() + "%";
        document.querySelector("#intro-offer-details").innerText = introOfferDetails;
        document.querySelector("#annual-fee").innerText += data["annual-fee"];
        document.querySelector("#overcharge-fee").innerText += data["overcharge-fee"];
    } catch (error) {
        console.error('There was a problem fetching the data:', error);
    }
}

// Call the function to fetch and log the data
fetchData();

// document.querySelector("#submit-query").addEventListener("onclick", questionAsked());

function questionAsked() {
    document.querySelector(".lds-ring").classList.remove("hidden");
    let rawQuestionText = document.querySelector("#chat-query").value;
    let questionText = rawQuestionText + "More information: " + JSON.stringify(cardData) + "Use your judgement and general knowledge";
    let answerText;
    if (questionText == "") {
        return;
    }
    let answerPlace = "http://api.creditdaddy.tech/ask/" + cardId + "/" + encodeURIComponent(questionText);
    async function fetchAnswerData() {
        try {
            const response = await fetch(answerPlace);

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const data = await response.text();
            answerText = data;

            // You can now work with the 'data' object containing the fetched data
            console.log(data);

            document.getElementById("liveQuestionBox").classList.add("show");
            document.querySelector("#question").innerText = rawQuestionText;
            document.querySelector("#answer").innerText = answerText;
        } catch (error) {
            console.error("There was a problem fetching the data:", error, answerPlace);
        }
        document.querySelector(".lds-ring").classList.add("hidden");


    }

    // Call the function to fetch the data
    fetchAnswerData();

}

async function fetchLast3Objects() {
    try {
        // Fetch the JSON data from the API
        const response = await fetch("http://api.creditdaddy.tech/chats/" + cardId);

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await response.json();

        // Get the last 5 objects from the array
        const last3Objects = data.slice(-3);

        // Log the last 5 objects to the console
        console.log("Last 3 Objects:", last3Objects);

        const faqContainer = document.querySelector(".faq");

        // Loop through your JSON data and create question boxes
        last3Objects.forEach(item => {
            // Create a new question box
            const questionBox = document.createElement("div");
            questionBox.classList.add("question-box");

            let questionString = item.question;
            const moreInfoIndex = questionString.indexOf('More information:');

            if (moreInfoIndex !== -1) {
                // Extract the question part (text before 'More information:')
                questionString = questionString.substring(0, moreInfoIndex);
            }

            // Create the question element and set its text
            const questionElement = document.createElement("div");
            questionElement.classList.add("question");
            questionElement.textContent = questionString;

            // Create the answer element and set its text
            const answerElement = document.createElement("div");
            answerElement.classList.add("answer");
            answerElement.textContent = item.answer;

            // Append the question and answer elements to the question box
            questionBox.appendChild(questionElement);
            questionBox.appendChild(answerElement);

            // Append the question box to the FAQ container
            faqContainer.appendChild(questionBox);
        });

    } catch (error) {
        console.error("There was a problem fetching the data:", error);
    }
}

// Call the function to fetch the last 5 objects
fetchLast3Objects();
