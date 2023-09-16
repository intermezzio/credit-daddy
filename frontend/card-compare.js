// Get all filter options
const filterOptions = document.querySelectorAll(".filter-option");

// Add click event listener to each filter option
filterOptions.forEach(option => {
    option.addEventListener("click", function () {
        // Toggle the "clicked" class on the clicked filter option
        option.classList.toggle("clicked");
    });
});