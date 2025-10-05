document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("thankButton");
  const message = document.getElementById("message");

  button.addEventListener("click", () => {
    message.classList.remove("hidden");
    button.textContent = "Thank you! 💚";
    button.disabled = true;

    // simple confetti-like effect
    for (let i = 0; i < 15; i++) {
      const confetti = document.createElement("div");
      confetti.className = "confetti";
      document.body.appendChild(confetti);

      confetti.style.left = Math.random() * 100 + "vw";
      confetti.style.animationDuration = (Math.random() * 2 + 2) + "s";

      setTimeout(() => confetti.remove(), 4000);
    }
  });
});
