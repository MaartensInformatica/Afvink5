import random

def willekeur():

    "Willekeurig getal opvragen en teruggeven"
    n = random.randint(1,101)
    return n


def uitkomst(gebruiker, klaar, n):

    """input vergelijken met willekeurig getal. en tekstbericht als variabele
    meegeven"""
    
    if gebruiker < n:
        print('Too low, try again')
        return klaar
    elif gebruiker > n:
        print('Too high, try again')
        return klaar
    elif gebruiker == n:
        print('Gefeliciteerd!!')
        klaar = True
        return klaar
    else:
        print('Invalid Number')
        return klaar


def main():
    """loop doorzetten zolang nummer niet geraden is"""
    """loop opnieuw beginnen als de gebruiker daarom vraagt """

    n = willekeur()
    klaar = False
    while klaar == False:
        gebruiker = int(input('Voer een getal tussen de 0 en de 100 in: '))
        klaar = uitkomst(gebruiker, klaar, n)
        if klaar == True:
            break
    keuze = ""
    while keuze.lower() != 'n':
        keuze = input('Wil je doorgaan: ')
        if keuze == 'y':
            main()
            break
        else:
            break
    
main()
