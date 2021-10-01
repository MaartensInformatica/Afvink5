import random
n = 0
def willekeur ():
    n = random.randint(1,4)
    return n
antwoord = 0
def steenpapierschaar(n):
    if n == 1:
        antwoord = 'steen'
    elif n == 2:
        antwoord = 'papier'
    else:
        antwoord = 'schaar'
    return antwoord
    
def main():
    speler = input('steen, papier of schaar?: ')
    antwoord = steenpapierschaar(willekeur())   
    if speler == 'steen' and antwoord == 'schaar':
        print('speler wint')
    elif speler == 'steen' and antwoord == 'papier':
        print('computer wint')
    elif speler == 'papier' and antwoord == 'schaar':
        print('computer wint')
    elif speler == 'papier' and antwoord == 'steen':
        print('speler wint')
    elif speler == 'schaar' and antwoord == 'steen':
        print('computer wint')
    elif speler == 'schaar' and antwoord == 'papier':
        print('speler wint')
    else:
        print('remise')
        main()
        
main()
