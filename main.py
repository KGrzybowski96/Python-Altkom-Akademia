import math

koniec = False
pozycja = (0,0)

while not koniec:
    polecenie = input("Podaj polecenie w formacie '<kierunek> <kroki>': ")

    #jeśli polecenie jest puste, tzn., że kończy się
    if polecenie:
        #print(polecenie)
        lista = polecenie.split()
        #print(lista)
        kierunek, kroki = lista
        kroki = int(kroki)
        kierunek = kierunek.upper()
        print(kierunek, kroki)

        if kierunek == 'N':
            pozycja = (pozycja[0], pozycja [1]+kroki)
        elif kierunek =='S':
            pozycja = (pozycja[0], pozycja[1]-kroki)
        elif kierunek =='E':
            pozycja = (pozycja[0]+kroki, pozycja[1])
        elif kierunek == 'W':
            pozycja = (pozycja[0]-kroki, pozycja[1])
        else :
            print("Nieznany kierunek")

        print(f"Po poleceniu {polecenie} obecna pozycja robota to {pozycja}")

    else:
        odległość = math.hypot(pozycja[0], pozycja[1])
        print(f"Robot zakonczył działanie w odległości {odległość} od bazy")
        koniec = True