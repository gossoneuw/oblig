print("==Tarjeis Pakke Liste==")
pakkeliste = []

funkjsoner = ['legge til noe', 'slette noe', 'skrive ut listen', 'slette hele listen', 'stoppe programmet']

slutt = False
while not slutt:
    print(f"\nHva vil du gjøre?")
    print(f"1: {funkjsoner[0]}")
    print(f"2: {funkjsoner[1]}")
    print(f"3: {funkjsoner[2]}")
    print(f"4: {funkjsoner[3]}")
    print(f"5: {funkjsoner[4]}")

    valg = input(f"Velg ved å skrive et av tallene over: ")

    if valg not in ('1', '2', '3', '4', '5'):
        print(f"Nå har du gjort noe feil, prøv igjen!")

    if valg == '1':
        print(f"Du har valgt å legge til noe i listen")
        pakkeliste.append(input(f"skriv hva du ønsker å legge til: "))

    elif valg == '2':
        print(f"Du har valgt å slette noe i listen")
        pakkeliste.remove(input(f"Skriv det du ønsker å fjerne fra listen: "))

    elif valg == '3':
        print()
        print(pakkeliste)

    elif valg == '4':
        print(f"du har valgt å slette hele listen")
        slette_hele_listen = input("er du sikker på at du vil slette hele listen? (Y/N): ")
        if slette_hele_listen.upper() == 'Y':
            pakkeliste.clear()

    elif valg == '5':
        print(f"vil du avslutte programmet og skrive ut listen?")
        avslutte = input("(Y/N): ")
        if avslutte.upper() == 'Y':
            print(pakkeliste)
            slutt = True
