const dropArea = document.getElementById("drop-area");
const fileInput = document.getElementById("file");

// Prevent default drag behaviors
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
    document.body.addEventListener(eventName, preventDefaults, false);
});

// Highlight drop area when a file is dragged over it
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false);
});

// Remove highlighting when the file is dragged out of the drop area
['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false);
});

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false);

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

function highlight() {
    dropArea.classList.add('highlight');
}

function unhighlight() {
    dropArea.classList.remove('highlight');
}

function handleDrop(e) {
    const apiUrl = 'http://api.creditdaddy.tech/upload-card';
    const dt = e.dataTransfer;
    const files = dt.files;

    if (files.length === 1 && files[0].type === 'application/pdf') {
        // If a single PDF file is dropped, set it as the input value
        fileInput.files = files;
        const formData = new FormData();
        formData.append('pdf_file', fileInput.files[0]);

        // Fetch options for the POST request
        const fetchOptions = {
            method: 'POST',
            body: formData,
        };

        // Send the POST request
        fetch(apiUrl, fetchOptions)
        .then((response) => {
            if (response.ok) {
            return response.text();
            } else {
            throw new Error(`Error: ${response.status} - ${response.statusText}`);
            }
        })
        .then((data) => {
            console.log('File successfully uploaded:', data);
        })
        .catch((error) => {
            console.error('An error occurred:', error.message);
        });

    } else {
        alert("Please drop a single PDF file.");
    }
}

const selectFileText = document.getElementById("drop-area");

selectFileText.addEventListener("click", function () {
    fileInput.click(); // Trigger a click event on the hidden input
});

// Listen for file selection and update the text
fileInput.addEventListener("change", function () {
    if (fileInput.files.length > 0) {
        const fileName = fileInput.files[0].name;
        selectFileText.querySelector(".text-wrapper-4").textContent = fileName;
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const questions = document.querySelectorAll(".header-question");
    let currentQuestionIndex = 0;
  
    // Function to fade out the current question and fade in the next question
    function fadeNextQuestion() {
      const currentQuestion = questions[currentQuestionIndex];
      currentQuestion.style.opacity = 0; // Fade out
  
      currentQuestionIndex = (currentQuestionIndex + 1) % questions.length;
  
      const nextQuestion = questions[currentQuestionIndex];
      nextQuestion.style.opacity = 1; // Fade in
  
      setTimeout(fadeNextQuestion, 4000); // Switch questions every 4 seconds
    }
  
    // Initial setup to display the first question
    questions[currentQuestionIndex].style.opacity = 1;
  
    // Start the rotation of questions
    setTimeout(fadeNextQuestion, 4000); // Start after 4 seconds
  });
  