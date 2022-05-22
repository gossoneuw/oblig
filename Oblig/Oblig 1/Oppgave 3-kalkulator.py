print("===== Kalkulator =====")
#liste over de forskjellige regnetypene man kan bruke. disse printes ut i konsollen
matte = ['Addisjon', 'Subtraksjon', 'Multiplikasjon', 'Divisjon', 'Prosent av', 'Opphøye', 'Dele med nedrunding']

print("\nHva vil du gjøre?")
print(f"1 - {matte[0]}")
print(f"2 - {matte[1]}")
print(f"3 - {matte[2]}")
print(f"4 - {matte[3]}")
print(f"5 - {matte[4]}")
print(f"6 - {matte[5]}")
print(f"7 - {matte[6]}")

valg = input("\nVelg med å skrive et av tallene over: ")
#ut ifra hvilket tall userimput er så velger kalkulatoren hvilken regneformel den skal bruke
if valg in ('1', '2', '3', '4', '5', '6', '7'):
    nummer1 = float(input("\nX verdi: "))
    nummer2 = float(input("Y verdi: "))
    if valg == '1':
        print(f"\n{nummer1} + {nummer2} = {nummer1 + nummer2}")

    elif valg == '2':
        print(f"\n{nummer1} - {nummer2} = {nummer1 - nummer2}")

    elif valg == '3':
        print(f"\n{nummer1} * {nummer2} = {nummer1 * nummer2}")

    elif valg == '4':
        print(f"\n{nummer1} / {nummer2} = {nummer1 / nummer2}")

    elif valg == '5':
        print(f"\n{nummer1} % av {nummer2} = {nummer1 * nummer2 / 100}")

    elif valg == '6':
        print(f"\n{nummer1} Opphøyd i {nummer2} = {nummer1 ** nummer2}")

    elif valg == '7':
        print(f"\n{nummer1} Dele med nedrunding {nummer2} = {nummer1 // nummer2}")
