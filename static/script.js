// script.js
export const socket = io(); // Nur das hier

export let username = null;
// Funktion wird aufgerufen, wenn der Benutzer auf „Mitspielen“ klickt
function register() {
    // Holt den eingegebenen Namen aus dem Eingabefeld

    username = document.getElementById("name").value;
    localStorage.setItem('username', username); // ← speichert dauerhaft

    window.username = username;
    window.location.href = '/quizGame';
    socket.emit('register', { username });
}

window.register = register;
