import datetime


class Person:

    def __init__(self, name, second_name, gender, year_brth, address):
        self.name = name
        self.second_name = second_name
        self.gender = gender
        self.year_brth = year_brth
        self.address = address

    def get_name(self):
        return self.__name
    def get_second_name(self):
        return self.__second_name
    def gender(self):
        return self.__gender()
    def year_brth(self):
        return self.__year_brth
    def address(self):
        return self.__address

    def get_gender(self):
        if self.gender:
            return 'mężczyzna'
        else:
            return 'kobieta'

    def ile_lat(self):
        return datetime.date.today().year - self.year_brth

    def __str__(self):
        return (self.name + ' ' + self.second_name + ', płeć: ' + self.get_gender() + ', wiek: '
                + str(self.ile_lat()) + ' lat')


ivan = Person('Ivan', 'Konoval', True, 1998, 'Rodziewiczówny 7/7, 50-000 Wrocław')
julia = Person('Julia', 'Wójcik', False, 2000, 'Ulanowskiego 16/2')
grzegorz = Person('Grzegorz', 'Kosiak', True, 1988, 'Sucha 1')
janusz = Person('Janusz', 'Abramowicz', True, 1700, 'Swobodna 70/22')
wiciu = Person('Wiktor', 'Rak', True, 2021, 'Plac Wolności 1')

while True:
    exit1 = input('Wyszukać osobę? ')
    if exit1.upper() == 'TAK' or exit1.upper() == "YES" or exit1.upper() == "T" or exit1.upper() == "Y":
        try:
            exit2 = input('Wpisz imię wyszukiwanej osoby: ')
            if exit2.upper() == 'IVAN':
                print(ivan.__str__())
            elif exit2.upper() == 'JULIA':
                print(julia.__str__())
            elif exit2.upper() == 'GRZEGORZ':
                print(grzegorz.__str__())
            elif exit2.upper() == 'JANUSZ':
                print(janusz.__str__())
            elif exit2.lower() == 'wiciu':
                print(wiciu.__str__())
            else:
                print('brak osoby')
        except Exception:
            print(Exception.__name__)
    else:
        print('Koniec wyszukiwania\n')
        break
