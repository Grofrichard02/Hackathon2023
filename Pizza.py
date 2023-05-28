import time

pizzak = {
    'sonkas': 1000,
    'gombas': 1100,
    'vegetarianus': 900,
    'hawaii': 1200
}

feltetek = {
    'extra sajt': 200,
    'szalami': 300,
    'olivabogyo': 150,
    'ananasz': 100
}

innivalok = {
    'szensavas uditok': 300,
    'gyumolcse': 250,
    'asvanyviz': 200,
    'energiaital': 400
}

desszertek = {
    'tiramisu': 600,
    'csokoladetorta': 550,
    'fagylalt': 350,
    'piskotarolad': 500,
    'nemkerek': 0
}

szoszok = {
    'paradicsomos': 0,
    'fokhagymas': 0,
    'bbq': 0
}

rendeles = {
    'pizza': '',
    'szosz': '',
    'feltet': [],
    'innivalo': '',
    'desszert': ''
}

def menu_megjelenitese():
    print("Pizza valasztek:")
    for pizza, ar in pizzak.items():
        print("- " + pizza + " (" + str(ar) + " Ft)")
    print("\nPlusz feltetek:")
    for feltet, ar in feltetek.items():
        print("- " + feltet + " (" + str(ar) + " Ft)")
    print("\nInnivalok:")
    for innivalo, ar in innivalok.items():
        print("- " + innivalo + " (" + str(ar) + " Ft)")
    print("\nDesszertek:")
    for desszert, ar in desszertek.items():
        print("- " + desszert + " (" + str(ar) + " Ft)")
    print("\nValaszthato szoszok:")
    for szosz, ar in szoszok.items():
        print("- " + szosz)

def rendeles_feldolgozasa():
    teljes_ar = pizzak[rendeles['pizza']]
    print("\nRendelesi reszletek:")
    print("Pizza: " + rendeles['pizza'] + " (" + str(teljes_ar) + " Ft)")
    if rendeles['szosz']:
        print("Szosz: " + rendeles['szosz'])
    if rendeles['feltet']:
        print("Plusz feltetek:")
        for feltet in rendeles['feltet']:
            teljes_ar += feltetek[feltet]
            print("- " + feltet + " (" + str(feltetek[feltet]) + " Ft)")
    if rendeles['innivalo']:
        teljes_ar += innivalok[rendeles['innivalo']]
        print("Innivalo: " + rendeles['innivalo'] + " (" + str(innivalok[rendeles['innivalo']]) + " Ft)")
    if rendeles['desszert']:
        teljes_ar += desszertek[rendeles['desszert']]
        print("Desszert: " + rendeles['desszert'] + " (" + str(desszertek[rendeles['desszert']]) + " Ft)")
    print("\nVegosszeg: " + str(teljes_ar) + " Ft")

def rendelesi_fajl_keszitese():
    with open('rendelesek.txt', 'a', encoding="utf-8") as file:
        file.write("Rendelesi reszletek:\n")
        file.write("Pizza: " + rendeles['pizza'] + " (" + str(pizzak[rendeles['pizza']]) + " Ft)\n")
        if rendeles['szosz']:
            file.write("Szosz: " + rendeles['szosz'] + "\n")
        if rendeles['feltet']:
            file.write("Plusz feltetek:\n")
            for feltet in rendeles['feltet']:
                file.write("- " + feltet + " (" + str(feltetek[feltet]) + " Ft)\n")
        if rendeles['innivalo']:
            file.write("Innivalo: " + rendeles['innivalo'] + " (" + str(innivalok[rendeles['innivalo']]) + " Ft)\n")
        if rendeles['desszert']:
            file.write("Desszert: " + rendeles['desszert'] + " (" + str(desszertek[rendeles['desszert']]) + " Ft)\n")
        file.write("\n")

print("Udvozollek a pizzarendelo chatbotban!")

while True:
    menu_megjelenitese()
    print("\nKerlek, add meg a rendelesed reszleteit!")

    pizza = input("Milyen pizzat szeretnel rendelni? ")
    if pizza.lower() not in pizzak:
        print("Sajnalom, ez a pizza nem szerepel a valasztekban.")
        continue
    rendeles['pizza'] = pizza.lower()

    print("\nValaszthato szoszok:")
    for szosz in szoszok:
        print("- " + szosz)
    szosz = input("Milyen soszt szeretnel a pizzahoz? ")
    if szosz.lower() not in szoszok:
        print("Sajnalom, ez a szosz nem szerepel a valasztekban.")
        continue
    rendeles['szosz'] = szosz.lower()

    while True:
        feltet = input("Szeretnel plusz feltet hozzaadni? (igen/nem) ")
        if feltet.lower() == "igen":
            print("\nPlusz feltetek:")
            for feltet, ar in feltetek.items():
                print("- " + feltet + " (" + str(ar) + " Ft)")
            kivalasztott_feltet = input("Melyiket szeretned hozzaadni? ")
            if kivalasztott_feltet.lower() in feltetek:
                rendeles['feltet'].append(kivalasztott_feltet.lower())
            else:
                print("Sajnalom, ez a plusz feltet nem szerepel a valasztekban.")
        elif feltet.lower() == "nem":
            break
        else:
            print("Kerlek, valaszolj 'igen' vagy 'nem'.")

    print("\nInnivalok:")
    for innivalo, ar in innivalok.items():
        print("- " + innivalo + " (" + str(ar) + " Ft)")
    innivalo = input("Milyen innivalot szeretnel rendelni? ")
    if innivalo.lower() not in innivalok:
        print("Sajnalom, ez az innivalo nem szerepel a valasztekban.")
        continue
    rendeles['innivalo'] = innivalo.lower()

    print("\nDesszertek:")
    for desszert, ar in desszertek.items():
        print("- " + desszert + " (" + str(ar) + " Ft)")
    desszert = input("Milyen desszertet szeretnel rendelni? ")
    if desszert.lower() not in desszertek:
        print("Sajnalom, ez a desszert nem szerepel a valasztekban.")
        continue
    rendeles['desszert'] = desszert.lower()

    rendeles_feldolgozasa()
    rendelesi_fajl_keszitese()

    megerosites = input("\nBiztos vagy benne, hogy elkulded a rendelest? (igen/nem) ")
    if megerosites.lower() == "igen":
        print("Rendeles elkuldve! Koszonjuk!")
        break
    else:
        print("Rendeles megszakitva.")
        rendeles = {
            'pizza': '',
            'szosz': '',
            'feltet': [],
            'innivalo': '',
            'desszert': ''
        }
        time.sleep(1)
