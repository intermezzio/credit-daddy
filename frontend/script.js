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
    const dt = e.dataTransfer;
    const files = dt.files;

    if (files.length === 1 && files[0].type === 'application/pdf') {
        // If a single PDF file is dropped, set it as the input value
        fileInput.files = files;
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
