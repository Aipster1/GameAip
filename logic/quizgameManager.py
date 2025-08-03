#logic/quizgameManager.py

import copy
import json
from flask import request
from flask_socketio import emit

currentPlayer = {}
questionCounter = 1

def loadQuizJSON():
    questions = 'static/data/json/questions.json'
    with open(questions, 'r', encoding='utf-8') as f:
        quizQuestions = json.load(f)
    return quizQuestions

import copy

def quizLogicEvents(socketio, currentPlayer, questionCounter):
    questions = loadQuizJSON()

    @socketio.on('answer')
    def handle_answer(data):
        nonlocal questionCounter

        answer = data['answer']
        name = data['username']
        lowerCaseName = name.lower()

        dataBefore = copy.deepcopy(currentPlayer)

        # Hole aktuelle Frage + richtige Antwort
        currentQuestion = None
        correctAnswer = None
        for item in questions["quiz"]:
            if item["id"] == questionCounter:
                currentQuestion = item['frage']
                correctAnswer = item['antwort']
                break

        print("========== ANTWORT-EVENT ==========")
        print(f"Nutzer: {name}")
        print(f"Antwort des Nutzers: {answer}")
        print(f"Frage: {currentQuestion}")
        print(f"Richtige Antwort: {correctAnswer}")
        print(f"Frage-ID: {questionCounter}")
        print("Daten vor dem Aufruf:")
        print(dataBefore)

        if not lowerCaseName or lowerCaseName not in currentPlayer:
            print(f"Antwort erhalten, aber Spieler '{name}' nicht bekannt.")
            return

        if answer.lower() == correctAnswer.lower():
            currentPlayer[lowerCaseName]['Score'] += 1
            for player in currentPlayer.values():
                if player['ip'] == request.remote_addr:
                    player['gaveAnswer'] = True
        else:
            for player in currentPlayer.values():
                if player['ip'] == request.remote_addr:
                    player['gaveAnswer'] = True

        data_after = copy.deepcopy(currentPlayer)

        print("Daten nach dem Aufruf:")
        print(data_after)
        print("====================================\n")

        allAnswersGiven = all(player.get('gaveAnswer', False) for player in currentPlayer.values())

        if allAnswersGiven:
            questionCounter += 1
            for player in currentPlayer.values():
                    player['gaveAnswer'] = False
            emit('updateScore', {
                "players": sorted(currentPlayer.values(), key=lambda p: (-p['Score'], p['username'].lower())),
                "questionCounter": questionCounter,
            }, broadcast=True)

    @socketio.on('getQuestion')
    def handle_get_question(data):
        questionCounter = data.get("questionCounter", 1)
        questions = loadQuizJSON()

        for item in questions["quiz"]:
            if item["id"] == questionCounter:
                emit('nextQuestion', {
                    "id": item["id"],
                    "frage": item["frage"],
                    "antwort": item["antwort"]
                })
                return

        emit('next_question', {"error": "Frage nicht gefunden"})

    @socketio.on('initPlayerList')
    def initPlayerList(data=None):
        print("Die Liste der Spieler lautet: ")
        print(list(currentPlayer.values()))
        emit('initPlayer', list(currentPlayer.values()), broadcast=True)
