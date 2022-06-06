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

def mlodszy_od_30(osoba):
    return osoba['wiek'] < 30

mlodzi = filter(mlodszy_od_30, lista_osob)

print(*mlodzi)

def postarz_o_rok(osoba):
    osoba['wiek'] += 1
    return osoba

starsi = map(postarz_o_rok, lista_osob)

def zmiana_miasta(osoba):
    osoba['miasto'] += 'Wrocław'
    return osoba

miasta = map(zmiana_miasta, lista_osob)

print(*starsi)