import random

def začetek_igre():
    karta_barva = ['Srce', 'Kara', 'Križ', 'Pik']
    karta_vrednost = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Pob', 'Kraljica', 'Kralj']
    komplet = [(karta, vrsta1) for vrsta1 in karta_barva for karta in karta_vrednost]

    def karta_tocke(card):
        if card[0] in ['Pob', 'Kraljica', 'Kralj']:
            return 10
        elif card[0] == 'As':
            return 11
        else:
            return int(card[0])
        
    random.shuffle(komplet)
    igralec_karte = [komplet.pop(), komplet.pop()]
    delilec_karte = [komplet.pop(), komplet.pop()]
    igralec_tocke = sum(karta_tocke(karta) for karta in igralec_karte)
    delilec_tocke = sum(karta_tocke(karta) for karta in delilec_karte)
    
    # Print player's and dealer's cards at the start of the game
    print("Karte igralca:", igralec_karte)
    print("Točke igralca:", igralec_tocke)
    print("\n")
    print("Karte delilca:", [delilec_karte[0], ('?', '?')])
    print("Točke delilca:", karta_tocke(delilec_karte[0]))
    print("\n")

    return komplet, igralec_karte, delilec_karte, igralec_tocke, delilec_tocke

def tocke(delilec_tocke, igralec_tocke, delilec_karte, igralec_karte, komplet):
    while delilec_tocke < 17:
        nova_karta = komplet.pop()
        delilec_karte.append(nova_karta)
        delilec_tocke += karta_tocke(nova_karta)

    print("Karte delilca:", delilec_karte)
    print("Točke delilca:", delilec_tocke)
    print("\n")

def karta_tocke(card):
    if card[0] in ['Pob', 'Kraljica', 'Kralj']:
        return 10
    elif card[0] == 'As':
        return 11
    else:
        return int(card[0])

def play_blackjack():
    cekini = 200
    print("Imaš " + str(cekini) + " cekinov.")

    while True:
        komplet, igralec_karte, delilec_karte, igralec_tocke, delilec_tocke = začetek_igre()

        while True:
            odlocitev = input('Kaj boš naredil? ["igram" za novo karto, "stop" za konec igre]: ').lower()
            if odlocitev == "igram":
                nova_karta = komplet.pop()
                igralec_karte.append(nova_karta)
                igralec_tocke = sum(karta_tocke(karta) for karta in igralec_karte)
                if igralec_tocke > 21:
                    print("Karte delilca:", delilec_karte)
                    print("Točke delilca:", delilec_tocke)
                    print("Karte igralca:", igralec_karte)
                    print("Točke igralca:", igralec_tocke)
                    print("Delilec zmaga (igralec ima več kot 21 točk)")
                    cekini -= 50
                    print("Imaš " + str(cekini) + " cekinov.")
                    break
                else:
                    print("Karte igralca:", igralec_karte)
                    print("Točke igralca:", igralec_tocke)
                    if input("Želiš dobiti novo karto? (da/ne): ").lower() != 'da':
                        break
            elif odlocitev == "stop":
                tocke(delilec_tocke, igralec_tocke, delilec_karte, igralec_karte, komplet)
                while delilec_tocke < 17:
                    nova_karta = komplet.pop()
                    delilec_karte.append(nova_karta)
                    delilec_tocke += karta_tocke(nova_karta)
                print("Karte delilca:", delilec_karte)
                print("Točke delilca:", delilec_tocke)
                print("Karte igralca:", igralec_karte)
                print("Točke igralca:", igralec_tocke)
                if igralec_tocke > 21:
                    print("Delilec zmaga (igralec ima več kot 21 točk).")
                    cekini -= 50
                    print("Imaš " + str(cekini) + " cekinov.")
                elif delilec_tocke > 21:
                    print("Zmagal si! (delilec ima več kot 21 točk)")
                    cekini += 50
                    print("Imaš " + str(cekini) + " cekinov.")
                elif igralec_tocke > delilec_tocke:
                    print("Zmagal si! (imaš več točk kot delilec)")
                    cekini += 50
                    print("Imaš " + str(cekini) + " cekinov.")
                elif igralec_tocke < delilec_tocke:
                    print("Delilec zmaga (ima več točk kot igralec).")
                    cekini -= 50
                    print("Imaš " + str(cekini) + " cekinov.")
                else:
                    print("Izenačeno.")
                    print("Imaš " + str(cekini) + " cekinov.")
                break
            else:
                print("Neznana beseda.")
                continue

        if cekini <= 0:
            print("Zmanjkalo ti je cekinov. Konec igre.")
            break
        elif input("Želiš nadaljevati igro? (da/ne): ").lower() != 'da':
            print("Konec igre.")
            break

play_blackjack()
