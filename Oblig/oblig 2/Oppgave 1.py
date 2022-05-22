valg = int(input("Hva er meningen med livet? "))

if valg == 42:
    print("Det stemmer, meningen med livet er 42!")

elif valg in range(31, 50):
    print("Nærme, men feil.")

elif valg != 42:
    print("FEIL!")

