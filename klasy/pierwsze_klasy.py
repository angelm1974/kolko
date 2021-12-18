# class MojaKlasa:
#     def wyswietl(x):
#         return 'Witaj swiecie'


# x = MojaKlasa()
# print(x.wyswietl())

class Prostopadloscian:
    def __init__(self):
        self.podstawa_a = 0
        self.podstawa_b = 0
        self.wysokosc_h = 0

    def Objetosc(self):
        return self.podstawa_a * self.podstawa_b * self.wysokosc_h

wtc=Prostopadloscian()
wtc.podstawa_a=100
wtc.podstawa_b=200
wtc.wysokosc_h=400
print(wtc.Objetosc())

