#ćwiczenie 9.2
lista_osob = [
    {'imie': 'Stefan', 'nazwisko': 'Mierzyński', 'wiek': 30, 'miasto': 'Bydgoszcz', 'branża': 'Marketing'},
    {'imie': 'Maria', 'nazwisko': 'Kowalska', 'wiek': 25, 'miasto': 'Warszawa', 'branża': 'HR'},
    {'imie': 'Konrad', 'nazwisko': 'Grzybowski', 'wiek': 26, 'miasto': 'Wroclaw', 'branża': 'IT'},
    {'imie': 'Jan', 'nazwisko': 'But', 'wiek': 55, 'miasto': 'Płock', 'branża': 'Logistyka'},
    {'imie': 'Janina', 'nazwisko': 'Kopała', 'wiek': 47, 'miasto': 'Radom', 'branża': 'Produkcja'},
    {'imie': 'Janusz', 'nazwisko': 'Kowalski', 'wiek': 56, 'miasto': 'Sopot', 'branża': 'Hotelarstwo'},
    {'imie': 'Małgorzata', 'nazwisko': 'Łopata', 'wiek': 23, 'miasto': 'Sandomierz', 'branża': 'Sprzedaż'},
    {'imie': 'Leszek', 'nazwisko': 'Wesołowski', 'wiek': 36, 'miasto': 'Poznań', 'branża': 'Sprzedaż'}
]

#print(lista_osob)

#mlodsze_niz_30 = [osoba for osoba in lista_osob if osoba['wiek'] < 30]
#print(mlodsze_niz_30)

branza_srzedaz = [osoba for osoba in lista_osob if osoba['branża'] == 'Sprzedaż']
print(f"Lista osób, które pracują w sprzedaży {branza_srzedaz}")