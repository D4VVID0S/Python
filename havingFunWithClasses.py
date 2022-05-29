class car():
    def __init__(self, marka, rok, kolor, przebieg):
        self.marka = marka
        self.rok = rok
        self.kolor = kolor
        self.przebieg = przebieg

    def print_car_details(self):
        print("Marka: " + str(car_1.marka))
        print("Kolor: " + str(car_1.kolor))
        print("Rok produkcji: " + str(car_1.rok))
        print("Przebieg: " + str(car_1.przebieg))
        car_1.silnik()

    def silnik(self):
        print("Wroooooooooooooom!!!!")

"""
MAIN
"""
marka = input("Podaj marke samochodu: ")
rok = input("Podaj rok samochodu: ")
kolor = input("Podaj kolor samochodu: ")
przebieg = input("Podaj przebieg samochodu: ")

car_1 = car(marka, rok, kolor, przebieg)
car_1.print_car_details()