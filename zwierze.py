class Zwierze:
    def __init__(self, nazwa, wiek, waga):
        self.nazwa = nazwa
        self.waga = waga
        self.wiek = wiek

    def podaj_dane(self):
        print(
            f'Jestem zwierzęciem {self.nazwa}, mam {self.wiek} lat i ważę {self.waga} kg.')


class Slon(Zwierze):
    pass


class Lew(Zwierze):
    def __init__(self):
        self.iloscKlow = 4


Dumbo = Slon()
Dumbo.nazwa = "Słonik Dumbo"
Dumbo.waga = 300
Dumbo.wiek = 400

Simba = Lew()
Simba.iloscKlow = 3
Simba.wiek = 34
Simba.nazwa = "Lew Simba"
Simba.waga = 450

Simba.podaj_dane()
Dumbo.podaj_dane()
