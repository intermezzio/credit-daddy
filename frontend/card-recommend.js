submit_btn = document.getElementById("submit");

submit_btn.addEventListener("onclick", recommend);

function recommend() {
    let sliders = document.querySelectorAll(".slidecontainer input.slider");
    let url = "http://api.creditdaddy.tech/recommend?foreign_overcharge="
                + sliders[0].valueAsNumber + "&apr_annual="
                + sliders[1].valueAsNumber + "&selective_general="
                + sliders[2].valueAsNumber;
    
    async function fetchAnswerData() {
        try {
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const redirectHere = await response.text();
            window.location.href = redirectHere;
            
        } catch (error) {
            console.error("There was a problem fetching the data:", error, answerPlace);
        }
        document.querySelector(".lds-ring").classList.add("hidden");


    }

    // Call the function to fetch the data
    fetchAnswerData();

}