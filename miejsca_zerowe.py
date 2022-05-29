"""
OBLICZANIE DELTY
"""
from math import sqrt
# importowanie funkcji sqrt() czyli pierwiastkowania z bilbioteki match
# from math import * <--- from math import all

print("Podaj wartosc wspolczynnika a:")
a = float(input())
print("Podaj wartosc wspolczynnika b:")
b = float(input())
print("Podaj wartosc wspolczynnika c:")
c = float(input())

delta = (b * b) - (4 * a * c)

if delta <= 0:
    print("Delta jest rowna " + delta + " czyli mniejsza od zera i nie ma miejsc zerowych")
elif delta == 0:
    x0 = -b / (2*a)
    print("Delta jest rowna 0 i ma jedno miejsce zerowe rowne " + x0 + ".")
else:
    x1 = (-b - sqrt(delta)) / (2 * a)
    x2 = (-b + sqrt(delta)) / (2 * a)
    print("Delta ma dwa miejsca zerowe.")
    print("x1 = ", x1)
    print("x2 = ", x2)