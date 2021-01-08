import random
import time

#Einleitung
print("***************************"); time.sleep(0.5)
print("* SCHERE | STEIN | PAPIER *"); time.sleep(0.5)
print("***************************\n\n"); time.sleep(0.5)

#Variablen
figuren = ("Schere, Stein, Papier")
spielen = True

while spielen:

    #Spielerfigur wählen
    spielerauswahl = 0
    while spielerauswahl not in(1, 2, 3):
        spielerauswahl = int(input("[1]-Schere, [2]-Stein, [3]-Papier\n"))
    spielerfigur = figuren[spielerauswahl - 1]

    #Computerfigur wahl
    computerfigur = figuren[random.randint(0, 2)]

    #Sieger
    if spielerauswahl == computerfigur:
        print("Unentschieden! Computer wählte: ", computerfigur)
    else:
        
        if spielerfigur == "Schere":
            if computerfigur == "Stein":
                print("Computer gewinnt!, denn Computer wählte: ", computerfigur)
            else:
                print("Gewonnen!, dennn der Computer wählte: ", computerfigur)

        if spielerfigur == "Stein":
            if computerfigur == "Papier":
                print("Computer gewinnt!, denn Computer wählte: ", computerfigur)
            else:
                print("Gewonnen!, denn Computer wählte: ", computerfigur)

        if spielerfigur == "Papier":
            if computerfigur == "Schere":
                print("Computer gewinnt!, denn Computer wählte: ", computerfigur)
            else:
                print("Gewonnen!, denn Computer wählte: ", computerfigur)


    #Restart?
    time.sleep(1)
    entscheidung = ""
    while entscheidung not in ("y", "n"):
        entscheidung = input("\nNochmal spielen? [y]:Ja  [n]:Nein\n")

    if entscheidung == "n":
        spielen = False
