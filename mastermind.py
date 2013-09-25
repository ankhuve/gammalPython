import random

allcolors = ["yellow","blue","red","green","orange","black","white"]
colors = ["yellow","blue","red","green","orange","black","white"] # Lista med användbara färger


def randColorlist(colors):   # Funktion för att skapa slumpad colorlist
    i = 0   # Skapa räknare
    colorlist = []  # Skapa tom lista
    while i < 5:    # Slumpa fram fem färger från colors och lägg till i colorlist
        rand = random.choice(colors)
        colorlist.append(rand)
        colors.remove(rand) # Ta bort färgen från listan så att den inte väljs två gånger
        i += 1
    return colorlist

def guessColorlist(allcolors, colorlist):  # Funktion för gissning av färger
    guesslist = []
    c = 0   # Räknare
    while c < 5:
        c += 1
        guess = ""
        while guess not in allcolors:   # Felhantering
            try:
                print ("Gissa färg nr", c, ":")
                guess = raw_input("")
            except:
                0+0
            while guess in guesslist:
                try:
                    print ("Du har redan gissat den färgen, ta en annan:")
                    guess = raw_input("")
                except:
                    0+0
            if guess == "ellaärsötast": #   Fuskkod med sanning :)
                print (colorlist)
        guesslist.append(guess)
    return guesslist

def checkColor(guesslist, colorlist):   # Funktion för att kontrollera vilka färger som var rätt
    n = 0
    correctColor = 0
    for color in guesslist:
        if guesslist[n] in colorlist[:5]:
            correctColor += 1
        n += 1
    return correctColor     # Returnera antalet rätta färger

def checkPos(guesslist, colorlist):     # Funktion för att kontrollera hur många färger som var på rätt plats
    n = 0
    correctPos = 0
    for color in guesslist:
        if guesslist[n] == colorlist[n]:
            correctPos += 1
        n += 1
    return correctPos   # Returnera antalet rätta färger på rätt plats

def main():
    colorlist = randColorlist(colors)
    print ("Datorn har slumpat fram fem färger av dessa:\n", allcolors, "\n\nFörsök lista ut vilka färger datorn har valt!")
    guesslist = []
    tries = 0
    while guesslist != colorlist:   # Kör programmet tills gissningen är korrekt
        guesslist = guessColorlist(allcolors, colorlist)
        correctColor = checkColor(guesslist, colorlist)
        correctPos = checkPos(guesslist, colorlist)
        tries += 1
        if correctPos == 5:
            print ("Du listade ut färgerna, grattis! Det tog dig BARA", tries, "försök..")
        else:
            print ("Din gissning var:", guesslist, "\nDu hade", correctColor, "rätta färger och", correctPos, "var på rätt plats. Försök igen!\n")

main()
