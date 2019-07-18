#Igra vislic
import random

seznam_besed = ['banana', 'koleraba', 'motorsist', 'puščica']
geslo = seznam_besed[random.randint(0,4)].upper()
geslo = geslo.upper()
geslo_seznam = list(geslo)
geslo_uganjeno =[]



def zacetno_geslo():
    '''Ustvari seznam dolžine gesla s samimi ničlami'''
    for _ in range(len(geslo)):
        geslo_uganjeno.append(0)
    return geslo_uganjeno


def preveri(crka, zivljenja):
    '''Preveri, ce je crka v geslu'''
    if crka.upper() in geslo_seznam:
        print('Ta crka je v besedi')
        return zivljenja
    else:
        print('Ta crka ni v besedi') 
        return zivljenja - 1 


def odpri_crko(crka):
    '''V geslu odpre vse crke'''
    indeks = 0
    for i in geslo_seznam:
        if crka == i:
            geslo_uganjeno[indeks] = crka
        indeks += 1
    return geslo_uganjeno


def igra(geslo, zivljenja): 
    geslo_uganjeno = zacetno_geslo()
    ze_uganjene_crke =[]
    while zivljenja != 0:
        print('')
        print('Geslo, ki ga ugibate je: {}'.format(geslo_uganjeno))
        print('Ugibali ste ze te crke {}'.format(ze_uganjene_crke))
        print ('Uganite crko:')
        crka = input()
        crka = crka.upper()
        if len(crka) != 1:
            print('To ni bil le en znak. Vpišite eno crko!')

        elif crka in ze_uganjene_crke:
            print('To crko ste že poskusili')
            print('Poskusite drugo')

        else:
            zivljenja = preveri(crka, zivljenja)
            geslo_uganjeno = odpri_crko(crka)
            ze_uganjene_crke.append(crka)
            if not (0 in geslo_uganjeno):
                print('')
                print('Cestitke zmagali ste igro!')
                quit()
    print('')
    print('Zal vam je zmanjkalo poskusov')
    quit()


igra(geslo, 7)