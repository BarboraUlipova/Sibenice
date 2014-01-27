import random
import string
import obrazky
slova = ["kralik","kocka","velbloud","dromedar","ovce","slepice"]
slovo = random.choice(slova) #kdybych tam mela from random import choice, mohla bych to psat jenom choice(slova)
print slovo
spravne = ["_"]*len(slovo)
spatne = []
kontrola_spravne = False
while kontrola_spravne == False: # nekonečný w. c. Zastaví se, až když bude splněna nějaká podmínka vevnitř
    pismeno = raw_input("Hadejte pismeno") # vždycky dávat raw_input. Neraw input přeloží vstup do pythoního kódu, takže by mazaný uživael mohl můj kód měnit.

    if pismeno in string.ascii_lowercase and len(pismeno)==1: #kontroluje, aby uživatel zadal právě jedno písmeno (ne číslo a ne víc písmen). ascii_lowercase je preddefinovaný řetězec. "In" kontroluje, jestli je písmeno jeho podretezec
        if pismeno in slovo:
            #seznamp.append(pismeno)
            for i in range(len(slovo)):
                if slovo[i]==pismeno:
                    spravne[i]=pismeno
            print pismeno
        else:
            if pismeno in spatne:
                print "Opakujes se"
            else:
                print "neni tam"
                spatne.append(pismeno)
                print obrazky.seznam_obrazku[-len(spatne)]
                
        kontrola_spravne = True
        for spravnepismeno in spravne: # range(len) se v pythonu nepoužívá
            if spravnepismeno == "_":
                kontrola_spravne = False
                break   
        if len(spatne)==6:
            print "Prohravas"
            kontrola_spravne = False
            break #ukonci while cyklus, pokud je 6 spatne zadanych cisel
            
        print " ".join(spravne)# spoji prvky seznamu do jednho stringu a oddeli je znakem v uvozovkach
        print " ".join(spatne)   
        
    else:
        print "musi to byt jedno pismeno"
if kontrola_spravne == True:
    print "Vyhravas"
