//static/keywordLogic.js

console.log("✅ JavaScript-Datei wurde erfolgreich geladen!");
document.addEventListener("DOMContentLoaded", function () {
    const popup = document.getElementById("word-popup");
    const options = document.querySelectorAll(".word-option");

    options.forEach(button => {
        button.addEventListener("click", () => {
            console.log("🔤 Gewähltes Wort:", button.textContent);
            popup.classList.add("hidden");
        });
    });

    // Neue Logik für Akzeptieren/Ablehnen
    const acceptButtons = document.querySelectorAll(".accept");
    const rejectButtons = document.querySelectorAll(".reject");

    acceptButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const row = btn.closest(".word-row");
            row.style.backgroundColor = "#c8f7c5"; // Hellgrün
        });
    });

    rejectButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const row = btn.closest(".word-row");
            row.style.backgroundColor = "#f7c5c5"; // Hellrot
        });
    });
});
