from random import *
inp = input("Du: ")
while inp != "Genug":
    if inp == "Alles okay?":
        for i in range(1,4):
            print("Bot: SOS")
        inp = input("Du: ")
    elif inp == "Wie geht es dir?":
        zahl = randint(0,2)
        if zahl == 0:
            print("Bot: Gut")
        elif zahl == 1:
            print("Bot: Schlecht")
        else:
            print("Bot: Passt schon")
        inp = input("Du: ")
    elif inp == "Was ist der Sinn des Lebens?":
        print("Bot: 42")
        inp = input("Du: ")
    elif inp == "Rechne aus wie als ich bin":
        geburtsmonat = int(input("Monat als Zahl: "))
        geburtstag = int(input("Tag: "))
        geburtsjahr = int(input("Jahr: "))

        if geburtsmonat <= 11 or (geburtsmonat==11 and geburtstag <9):
            print("Bot: " + str(2018- geburtsjahr))
        elif geburtsmonat == 11 and geburtstag == 9:
            print(2018-geburtsjahr)
            print("Bot: Herzlichen Glückwunsch")
        else:
            print("Bot: "+ str(2018-geburtsjahr-1))
        inp = input("Du: ")
    else:
        print("Bot: Stelle mir eine andere Frage")
        inp = input("Du: ")
print("Bot: Schade")