odpowiedniki = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
liczba = int(input("podaj liczbe: "))

rzymska = ''
while 1 < liczba <= 4000:
    for l, m in odpowiedniki:
        while liczba >= l:
            rzymska = rzymska + m
            liczba = liczba - l
    print(rzymska)

if liczba > 4000:
    print("Prosze o inna liczbe")