class Pracownik:
    def __init__(self, imie, nazwisko, zarobki):
        self.__set_imie(imie)
        self.__nazwisko = nazwisko
        self.__zarobki = zarobki

    def __get_imie(self):
        return self.__imie()

    def __set_imie(self, imie):
        self.__imie = imie

    def __get_nazwisko(self):
        return self.__nazwisko()

    def __set_nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    def __get_zarobki(self):
        return self.__zarobki()

    def __set_zarobki(self, zarobki):
        self.__zarobki = zarobki

    def __str__(self):
        return f"[Pracownik] {self.__imie} {self.__nazwisko}, zarobki: {self.__zarobki}"

    imie_pro = property(__get_imie, __set_imie)
    nazwisko_pro = property(__get_nazwisko, __set_nazwisko)
    zarobki_pro = property(__get_zarobki, __set_zarobki)


p1 = Pracownik("Stanisław", "Wokulski", 5600)
p2 = Pracownik("Stanisław", "Wokulski", 5600)
print(p1)


class KierownikZespolu(Pracownik):
    def __init__(self, imie, nazwisko, zarobki, odpowiedzialnosc):
        super().__init__(imie, nazwisko, zarobki)
        self.__podwladni = []
        self.__odpowiedzialnosc = odpowiedzialnosc

    def __get_podwladni(self):
        return self.__podwladni()

    def __set_podwladni(self, podwladni):
        self.__podwladni = podwladni

    def __get_odpowiedzialnosc(self):
        return self.__odpowiedzialnosc()

    def __set_odpowiedzialnosc(self, odpowiedzialnosc):
        self.__odpowiedzialnosc = odpowiedzialnosc

    podwladni_pro = property(__get_podwladni, __set_podwladni)
    odpowiedzialnosc_pro = property(__get_odpowiedzialnosc, __set_odpowiedzialnosc)

    def dodaj_pracownika(self, prac):
        self.__podwladni.append(prac)

    def usun_pracownika(self,prac):
        self.__podwladni.remove(prac)

    def __str__(self):
        return f"{super().__str__()}, {self.__odpowiedzialnosc}, Podwładni: {','.join([str(prac) for prac in self.__podwladni])}"

k1 = KierownikZespolu("Jan", "Kowalski", 9600, "Zarządzanie")
k1.dodaj_pracownika(p1)
k1.dodaj_pracownika(p2)

print(k1)