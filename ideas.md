# Projektname: GameAip

## KeyWords
- [ ] A-Z für Spieler und Mitspieler generieren lassen (Nicht hardgecoded -> Weiß nicht ob das einen Vorteil bringt)
- [ ] Spieleranzahl angeben und dementsprechend Felder generieren
- [ ] Eingetragene Wörter in einem Dic speichern
- [ ] Wörter bei Mitspielern einblenden wenn auf diese geklickt wird
- [ ] Punktesystem einfügen (Wie viele Runden überlebt, Wie viele akzeptierte Wörter,...)
- [ ] Anzeige der bereits geratenen Wörtern
- [ ] Ausgewähltes Startwort oben einblenden
- [ ] Countdown einbauen
- [ ] Feld um Wort zu erraten (Eventuell als Pop-Up einblenden "Raten oder weiter?")

## Quizgame
- [ ] Neue Formate einfügen (Musikquiz, Bilderquiz, ...)


## Notizen
- 

## Offene Fragen
- 


# Mögliche Umsetzung für KeywordsGame

- Spieler connected zur Website
- Connect wir ausgeführt
- spieler muss sich registrieren
- name wird in session und db geschrieben
- auf der Spieleseite kann man dann abfragen welcher name in der Session steht und genau diesen Datensatz als 
  aktuellen Spieler definieren (alle anderen sind dann die Mitspieler)


# Datenbank Brainstorming:

Spieler:
- id
- name
- displayname


Board:
- Zielwort

- list of guessed words

- begriffe_score
- strafpunkte_score
- guessed words count (oder count auf die liste anwenden??)
- list of correct guessed words
- rounds_counter






boards_wordlist_correct
boardid - a - apfel - correct - opened
boardid - b - banane - correct - closed
boardid - c - cola - correct - opened


Game_Player_Score


Gameid - Boardid - score         

Gameid - Boardid - Score
   1   -     1   -  20
   1   -     3   -  6
   1   -     2   -  5
   1   -     4   -  60





Game
Gameid - Playerid - score






Boards_tabelle - alle boards aller spieler gespeichert (a-z)

Keywords Tabelle (Wörterbuch)






Game_Spieler

evt. 
Game_Boards



Game
- spieler 1
    - Board 1
   
- spieler 2
- spieler 3