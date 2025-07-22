import {socket, username} from './script.js';

// Spielername aus localStorage holen (wurde zuvor in index.html gespeichert)
const name = localStorage.getItem('username');

// Spieler direkt beim Laden der Seite beim Server registrieren
socket.emit('register', {username: name});

console.log(username);
console.log(name);

function setFirstQuestion(){

    fetch('/static/data/json/questions.json')
        .then(response => response.json())
        .then(data => {
            document.getElementById("question").textContent = data.question; //ID fehlt noch
        })
        .catch(error => {
            console.error('Fehler beim Laden der JSON-Datei:', error);
        });

}

function submitAnswer() {

    console.log("Hallo Welt du Hurensohn");

    // Holt den eingegebenen Antworttext
    const userAnswer = document.getElementById("answer").value;

    // Sendet ein "answer"-Event mit der Antwort an den Server
    socket.emit('answer', {username: name, answer: userAnswer});


    // Leert das Eingabefeld nach dem Absenden
    document.getElementById("answer").value = "";
}


// Reagiert auf das "player_list"-Event vom Server
// Dieses Event enthält eine Liste aller Spieler mit ihren Punkten

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

function changeQuestion(questionCounter) {
    fetch('/static/data/json/questions.json')
        .then(response => response.json())
        .then(data => {
            document.getElementById("question").textContent = data.question; //ID fehlt noch
        })
        .catch(error => {
            console.error('Fehler beim Laden der JSON-Datei:', error);
        });
}

window.submitAnswer = submitAnswer;

