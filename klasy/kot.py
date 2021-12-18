class Kot:

    def __init__(self):
        self.imie = ''
        self.kolorOczu = ''
        self.kolorSiersci = ''
        self.dlugosc = 0
        self.wysokosc = 0
        self.wiek = 0
        self.waga = 3

    def miauczenie():
        print("Miau!")

    def spanie(self):
        if self.wiek <= 10 and self.wiek > 0:
            print('śpi godzinę')
        elif self.wiek > 10:
            print('śpi 3 godziny')

    def jedzenie(self):
        self.waga += 10
        print(self.waga)
        print('kot dobrze zjadł')

    def drapanie(self):
        if self.waga <= 10:
            print('straty są znikome')
        else:
            print('kot wyrzucony z domu')
