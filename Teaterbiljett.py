# Skrivet av Ella Syk
# 2012-05-02
# P-uppgift 140: SÃ¥lda teaterbiljetter

class Teater(object):

    def __init__(self, namn, platser, prisVuxen, prisBarn, prisPensionÃ¤r):
        """Initierar varje teaters attribut.
        Attributen Ã¤r teaterns namn, pris fÃ¶r vuxna/barn/pensionÃ¤rer, antalet vuxna/barn/pensionÃ¤rer samt teaterns intÃ¤kter och belÃ¤ggning.
        INDATA Ã¤r teaterns namn, antal platser och priser."""
         
        self.__namn = namn
        self.__platser = platser
        self.__prisVuxen = prisVuxen
        self.__prisBarn = prisBarn
        self.__prisPensionÃ¤r = prisPensionÃ¤r
        self.__antalVuxen = 0
        self.__antalBarn = 0
        self.__antalPensionÃ¤r = 0
        self.__intÃ¤kter = 0
        self.__belÃ¤ggning = 0

    def __str__(self):
        """RETURNERAR en strÃ¤ngrepresentation av varje 	teaterobjekt:
        Skriver ut teaterns namn, prisklasser,
        platser, antal bokade platser och intÃ¤kter. """

        status = "\n" + self.__namn + ":"
        status += "\n\nTotalt " + str(self.__platser) + " platser i salongen."
        status += "\n\n" + str(self.__antalVuxen) + " vuxenbiljetter Ã¤r bokade."
        status += "\n" + str(self.__antalBarn) + " barnbiljetter Ã¤r bokade."
        status += "\n" + str(self.__antalPensionÃ¤r) + " pensionÃ¤rbiljetter Ã¤r bokade."
        status += "\n\nVuxenbiljett: " + str(self.__prisVuxen) + "kr."
        status += "\nBarnbiljett: " + str(self.__prisBarn) + "kr."
        status += "\nPensionÃ¤rbiljett: " + str(self.__prisPensionÃ¤r) + "kr."
        
        return status

    def bokaBiljetter(self, vuxen, barn, pensionÃ¤r):
        """Bokar biljetter dvs. Ã¤ndrar attributen antalVuxen, antalBarn och antalPensionÃ¤r.
            INDATA Ã¤r antalet biljetter som bokats i de olika prisklasserna."""

        self.__antalVuxen += vuxen
        self.__antalBarn += barn
        self.__antalPensionÃ¤r += pensionÃ¤r

    def totaltAntalPersoner(self):
        """RÃ¤knar ut totalt antal bokade platser i salongen.
        RETURNERAR summan."""
        
        totaltAntalPersoner = self.__antalVuxen + self.__antalBarn + self.__antalPensionÃ¤r
        return totaltAntalPersoner
        

    def belÃ¤ggning(self, totaltAntalPersoner):
        """RÃ¤knar ut och skriver ut varje teaters belÃ¤ggning i procent och skriver ut den.
        Ã„NDRAR attributet self.__belÃ¤ggning
        INDATA Ã¤r totalt antal personer.
        RETURNERAR belÃ¤ggningsprocenten."""

        belÃ¤ggProcent = (totaltAntalPersoner/self.__platser)*100
        self.__belÃ¤ggning = belÃ¤ggProcent


    def __lt__(self, other):
        """Villkor fÃ¶r att sortera teatrarna utefter belÃ¤ggning, hÃ¶gst fÃ¶rst och sen fallande"""

        if self.__belÃ¤ggning < other.__belÃ¤ggning:
            return False
        else:
            return True

            
    def sÃ¥ldaBiljetterScenarion(self, intÃ¤kter):
        """BerÃ¤knar alla mÃ¶jliga heltalslÃ¶sningar til hur stort antal av biljetterna
        som Ã¤r av varje prisklass utifrÃ¥n teaterns intÃ¤kter och prisklasser.
        INDATA Ã¤r teaterns intÃ¤kter."""
        
        maximum = self.__platser
        print("UtifrÃ¥n " + self.__namn + "s intÃ¤kter Ã¤r fÃ¶ljande bokningar mÃ¶jliga: \n")
        for antalSortVuxen in range(maximum + 1): 
            for antalSortBarn in range(maximum + 1):
                for antalSortPensionÃ¤r in range(maximum + 1):

                    antal = antalSortVuxen + antalSortBarn + antalSortPensionÃ¤r  
                    summa = self.__prisVuxen * antalSortVuxen + self.__prisBarn * antalSortBarn + self.__prisPensionÃ¤r * antalSortPensionÃ¤r

                    
                    if antal <= maximum and summa == self.__intÃ¤kter:
                         print(str(antalSortVuxen) + "st vuxenbiljetter\n" + str(antalSortBarn) + "st barnbiljetter \n" + str(antalSortPensionÃ¤r) + "st pensionÃ¤rbiljetter \n")

    
    def summaIntÃ¤kterEnTeater(self, teaterLista):
        """RÃ¤knar ut varje teaters intÃ¤kter (Ã„NDRAR self.__intÃ¤kter) och skriver ut dem.
        INDATA Ã¤r en lista med teaterobjekt."""

        summaVuxen = self.__prisVuxen*self.__antalVuxen
        summaBarn = self.__prisBarn*self.__antalBarn
        summaPensionÃ¤r = self.__prisPensionÃ¤r*self.__antalPensionÃ¤r

        self.__intÃ¤kter = summaVuxen + summaBarn + summaPensionÃ¤r        

        print(self.__namn + "s intÃ¤kter Ã¤r "+ str(self.__intÃ¤kter) + "kr.")
        
        
    def typAvBesÃ¶kare(self, totaltAntalPersoner): 
        """RÃ¤knar ut hur mÃ¥nga procent av besÃ¶karna som var vuxna/barn/pensionÃ¤rer.
        INDATA Ã¤r totalt antal bokade biljetter."""

        andelVuxna = (self.__antalVuxen/totaltAntalPersoner)*100
        andelBarn = (self.__antalBarn/totaltAntalPersoner)*100
        andelPensionÃ¤rer = (self.__antalPensionÃ¤r/totaltAntalPersoner)*100

        print("\nAv de som besÃ¶kt " + self.__namn + " var:\n" + str(andelVuxna)[:4] + "% vuxna\n" + str(andelBarn)[:4] + "% barn\n" + str(andelPensionÃ¤rer)[:4] + "% pensionÃ¤rer.\n")


    def Ã¥tkomstPlatser(self):
        """Ger Ã¥tkomst till attributet __platser.
        RETURNERAR antalet platser pÃ¥ en teater."""
        
        return self.__platser

    def Ã¥tkomstIntÃ¤kter(self):
        """Ger Ã¥tkomst till attributet __intÃ¤kter.
        RETURNERAR teaterns intÃ¤kter."""
        
        return self.__intÃ¤kter

    def Ã¥tkomstNamn(self):
        """Ger Ã¥tkomst till attributet __namn.
        RETURNERAR teaterns namn."""
        
        return self.__namn

    def Ã¥tkomstBelÃ¤ggning(self):
        """Ger Ã¥tkomst till attributet __belÃ¤ggning.
        RETURNERAR en teaters belÃ¤ggningsprocent."""
        
        return self.__belÃ¤ggning

        
############################# FUNKTIONER ###################################


def lÃ¤saInTeatrar():
    """LÃ¤ser in teatrarnas information frÃ¥n fil.
    INDATA Ã¤r filen
    RETURNERAR Ã¤r en lista med alla teatrar och deras information."""

    import sys
    
    try:
        infil = open("teatrar.txt", "r")
    except(IOError, UnboundLocalError):
        print("Fil existerar inte/gÃ¥r ej att Ã¶ppna! Kontrollera filen.")
        sys.exit()
  
    objektLista = []
    try:
        for rad in infil:
            teaterLista = rad.split("/")
            namn = teaterLista[0]
            platser = int(teaterLista[1])
            prisVuxen = int(teaterLista[2])
            prisBarn = int(teaterLista[3])
            prisPensionÃ¤r = int(teaterLista[4])

            if prisVuxen < prisBarn or prisPensionÃ¤r < prisBarn or prisVuxen < prisPensionÃ¤r:
                print("Kontrollera priserna i filen!")
                sys.exit()

            elif len(namn) >= 10:
                print("Kontrollera teaternamnen!")
                sys.exit()                

            objekt = Teater(namn, platser, prisVuxen, prisBarn, prisPensionÃ¤r)
            objektLista.append(objekt)
            
    except:
        print("Filen Ã¤r korrupt!")
        sys.exit()

  
    infil.close()               
    return objektLista


def meny():
    """ Skriver ut huvudmenyn."""

    print("""
                            Vad vill du gÃ¶ra?                      

                        1 - Boka biljetter
                        2 - Se biljettintÃ¤kter
                        3 - Se belÃ¤ggning 
                        4 - Se bokningsscenarion utifrÃ¥n teaterns intÃ¤kter
                        5 - Statistik
                        6 - Avsluta
                
    """)
    
  
def valMeny():
    """LÃ¤ser in anvÃ¤ndarens val.
    RETURNERAR en siffra motsvarande valda menyalternativet."""

    val = None
    try:
        val = int(input("Var god vÃ¤lj ett av alternativen 1-6: "))
    except(ValueError, UnboundLocalError):
        print("\nDet dÃ¤r var inte en siffra. Skriv in ett tal mellan 1-6!")
        print("\n")
        
    return val


def anropaMetod(val, teaterLista):
    """Anropar den valda metoden.
    INDATA Ã¤r siffran motsvarande valda menyalternativet OCH listan med teaterobjekt."""

    if val == 1:
        
        print("\nTeatrarna: \n")
        rÃ¤knare = 1
        for teater in teaterLista:
            teaterNamn = teater.Ã¥tkomstNamn()
            print(rÃ¤knare, teaterNamn)
            rÃ¤knare +=1

        valTeater = None
        while valTeater not in range(1,6):
            try:
                valTeater = int(input("\nHos vilken teater vill du boka biljetter? \nVar god vÃ¤lj siffran motsvarande ditt val: "))
                if valTeater not in range(1,6):
                    print("\nDet finns bara 5 teatrar. FÃ¶rsÃ¶k igen.")
                    
            except(ValueError):
                print("\nDu skulle vÃ¤lja en siffra! FÃ¶rsÃ¶k igen.")
            
        
        print("\n" + str(teaterLista[valTeater-1]))

        biljettTyp = "vuxen"
        vuxen = bokaBiljetter(valTeater, teaterLista, biljettTyp)
        teaterLista[valTeater-1].bokaBiljetter(vuxen, 0, 0)

        biljettTyp = "barn"
        barn = bokaBiljetter(valTeater, teaterLista, biljettTyp)
        teaterLista[valTeater-1].bokaBiljetter(0, barn, 0)

        biljettTyp = "pensionÃ¤r"
        pensionÃ¤r = bokaBiljetter(valTeater, teaterLista, biljettTyp)
        teaterLista[valTeater-1].bokaBiljetter(0, 0, pensionÃ¤r)
        
        if vuxen or barn or pensionÃ¤r > 0:
            print("\nDin bokning:")
            print(str(vuxen) + "st vuxenbiljetter\n" +  str(barn) + "st barnbiljetter\n" + str(pensionÃ¤r) + "st pensionÃ¤rbiljetter")
            input("\nDin bokning har registrerats. Tryck enter fÃ¶r att fortsÃ¤tta.")

        else:
            input("\nDu har bokat 0 biljetter. Tryck enter fÃ¶r att fortsÃ¤tta.")


    elif val == 2:
        
        print("\n")
        for teater in teaterLista:
            teater.summaIntÃ¤kterEnTeater(teaterLista)

        totalaIntÃ¤kter = 0
        for intÃ¤kter in teaterLista:
            totalaIntÃ¤kter += intÃ¤kter.Ã¥tkomstIntÃ¤kter()

        print("\nTeatrarnas sammanlagda intÃ¤kter Ã¤r totalt " + str(totalaIntÃ¤kter) + "kr.")
      

    elif val == 3:
        
        print("\n")
        for teater in teaterLista:
            totaltAntalPersoner = teater.totaltAntalPersoner()
            teater.belÃ¤ggning(totaltAntalPersoner)

            teaterNamn = teater.Ã¥tkomstNamn()
            belÃ¤ggning = teater.Ã¥tkomstBelÃ¤ggning()
            print(str(belÃ¤ggning)[:5] + "% av " + teaterNamn + "s platser Ã¤r bokade.")            
            

    elif val == 4:

        print("\n") 
        for teater in teaterLista:
            intÃ¤kter = teater.summaIntÃ¤kterEnTeater(teaterLista)
            teater.sÃ¥ldaBiljetterScenarion(intÃ¤kter)
            
      
    elif val == 5:
    
        valStatistik = None
        while valStatistik !=3:
            menyStatistik()
            valStatistik = valMenyStatistik()
            statistik(teaterLista, valStatistik)


    elif val == 6:
        print("\nVÃ¤lkommen Ã¥ter.")

                        


def menyStatistik():
    """Meny fÃ¶r att se olika statistik"""

    print("""\n
                                Statistik

            1 - Se vilken teater som har hÃ¶gst belÃ¤ggning
            2 - Ã…ldersfÃ¶rdelningen bland besÃ¶karna
            3 - Tillbaka till huvudmenyn
            
            """)


def valMenyStatistik():
    """LÃ¤ser in valet i statistikmenyn frÃ¥n anvÃ¤ndaren.
    RETURNERAR en siffra motsvarande valet."""

    valStatistik = None
    try:
        valStatistik = int(input("Var god vÃ¤lj ett alternativ 1-3: "))
        if valStatistik not in range(1,4):
            print("\nDet finns bara 3 alternativ! FÃ¶rsÃ¶k igen.")
            
    except(ValueError, UnboundLocalError):
        print("\nDet dÃ¤r var inte en siffra. Skriv in ett tal mellan 1-3!")

    return valStatistik
    

def statistik(teaterLista, valStatistik):
    """Anropar metoder som utfÃ¶r valt alternativ.
    INDATA Ã¤r valStatistik, alltsÃ¥ val i statistikmenyn motsvarande en siffra, samt en lista med teaterobjekt."""

    try:
        if valStatistik == 1:
            print("\n\nI fallande ordning de teatrar som haft hÃ¶gst belÃ¤ggning:")

            for teater in teaterLista:
                totaltAntalPersoner = teater.totaltAntalPersoner()
                belÃ¤ggning = teater.belÃ¤ggning(totaltAntalPersoner)

            teaterLista.sort()
            for teater in teaterLista:
                print(teater)


        elif valStatistik == 2:

            for teater in teaterLista:
                totaltAntalPersoner = teater.totaltAntalPersoner()
                namn = teater.Ã¥tkomstNamn()
                try:
                    teater.typAvBesÃ¶kare(totaltAntalPersoner)
                except(ZeroDivisionError):
                    print("\n" + namn + ": \nNoll biljetter bokade.")

    except():
        print("Felaktig inmatning. Ska vara ett tal mellan 1-3!")
        

def bokaBiljetter(valTeater, teaterLista, biljettTyp):
    """Bokar biljetter.
    INDATA Ã¤r val av teater, en lista med teaterobjekt samt typ av biljett som ska bokas.
    RETURNERAR antalet biljetter som ska bokas."""

    kontroll = None
    antalPersoner = 0

    while kontroll != True:
        try:
            antalPersoner = int(input("\nHur mÃ¥nga " + biljettTyp + "biljetter vill du boka? "))
            kontroll = ledigaPlatser(valTeater, teaterLista, antalPersoner)

        except(ValueError):
            print("\nDin inmatning ska vara en siffra! FÃ¶rsÃ¶k igen.")

    return antalPersoner


def ledigaPlatser(valTeater, teaterLista, antalPersoner):
    """Bidrar till att gÃ¶r sÃ¥ att man inte kan boka fler platser Ã¤n de som finns i salongen.
    INDATA Ã¤r valet av teater och antalet biljetter man vill boka i varje prisklass, samt en lista med teaterobjekt.
    RETURNERAR true eller false."""
    
    bokadePlatser = teaterLista[valTeater-1].totaltAntalPersoner()
    platserISalong = teaterLista[valTeater-1].Ã¥tkomstPlatser()
    ledigaPlatser = platserISalong - bokadePlatser


    if antalPersoner > ledigaPlatser:
        print("\nDet finns inte sÃ¥ mÃ¥nga lediga platser! Endast " + str(ledigaPlatser) + " platser Ã¤r lediga.")

        return None
    else:
        return True


def main():
    """Startar programmet."""

    teaterLista = lÃ¤saInTeatrar()    
    val = None
    print("\t\t\t\t VÃ¤lkommen!")
    print("\t    Detta program behandlar bokningar av teaterbiljetter.")

    while val != 6:

        if val  not in range(1,6):
            print("\nFinns endast 6 alternativ att vÃ¤lja mellan!")
            
        meny()
        val = valMeny()
        anropaMetod(val, teaterLista)


############################
####### Main ###############
############################   

try:
    main()
except(SystemExit):
    print("Programmet avslutas.")


############################
############################


