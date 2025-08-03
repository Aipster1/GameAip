//static/quizLogic.js

import {socket, username} from './script.js';

// Spielername aus localStorage holen (wurde zuvor in index.html gespeichert)
const name = localStorage.getItem('username');

// Spieler direkt beim Laden der Seite beim Server registrieren
socket.emit('register', {username: name});

console.log(username);
console.log(name);

function changeQuestion(questionCounter) {
    socket.emit('getQuestion', {questionCounter: questionCounter});
}

socket.on('nextQuestion', (data) => {
    if (data.error) {
        console.error("Fehler vom Server:", data.error);
        return;
    }

    document.getElementById("question").textContent = data.frage;
    console.log(`Frage ${data.id}: ${data.frage}`);
});


function submitAnswer() {

    console.log("Hallo Welt");

    // Holt den eingegebenen Antworttext
    const userAnswer = document.getElementById("answer").value;

    // Sendet ein "answer"-Event mit der Antwort an den Server
    socket.emit('answer', {username: name, answer: userAnswer});


    // Leert das Eingabefeld nach dem Absenden
    document.getElementById("answer").value = "";
}

socket.on('updateScore', (data) => {

    console.log('Empfangene Daten:', data);

    const list = document.getElementById("players");
    list.innerHTML = "";


    if (data.players) {
        data.players.forEach(p => {
            const li = document.createElement("li");
            li.textContent = `${p.username}: ${p.Score} Punkte`;
            list.appendChild(li);
        });
    } else {
        console.log("Keine Spieler-Daten empfangen");
    }

    if (data.questionCounter !== undefined) {
        console.log("Aktueller Fragezähler:", data.questionCounter);
        changeQuestion(data.questionCounter)
    } else {
        console.log("Kein Fragezähler empfangen");
    }

});


socket.on('initPlayer', function (players) {
    console.log("Aktuelle Spieler:", players);

    const list = document.getElementById("players");
    list.innerHTML = "";

    if (players && players.length > 0) {
        players.forEach(p => {
            const li = document.createElement("li");
            li.textContent = `${p.username}: ${p.Score} Punkte`;
            list.appendChild(li);
        });
    } else {
        console.log("Keine Spieler-Daten empfangen");
    }
});


window.submitAnswer = submitAnswer;

window.addEventListener('load', () => {
    socket.emit('initPlayerList', {});
    changeQuestion(1);
});