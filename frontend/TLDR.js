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
