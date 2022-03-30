# https://www.w3resource.com/python-exercises/python-basic-exercises.php

# sys - zadanie 2 - dodaje informacje o wersji pythona
import sys
# datetime - zadanie 3 - dodaje czas
import datetime
# math - zadanie 4 - importuje rzeczy potrzebne do obliczen matematycznych (np. pi, sqrt)
from math import *

def zadanie_1():
    print("Twinkle, twinkle, little star,")
    print("\tHow I wonder what you are!")
    print("\t\tUp above the world so high,")
    print("\t\tLike a diamond in the sky.")
    print("Twinkle, twinkle, little star,")
    print("\tHow I wonder what you are")

def zadanie_2():
    print("Python Version: " + str(sys.version))
    print("Version info: " + str(sys.version_info))

def zadanie_3():
    now = datetime.datetime.now()
    print("Current date and time: " + str(now.strftime("%Y-%m-%d %h:%M:%S")))

def zadanie_4():
    print("Podaj promien: ")
    promien = float(input())
    print("Pole kola o promieniu " + str(promien) + " rowna sie " + str(pi * promien**2))

def zadanie_5():
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    print("Hello " + str(nazwisko) + " " + str(imie))

def zadanie_6():
    liczby = input("Podaj sekwencje liczb po przecinkach: ")
    lista_liczb = liczby.split(",")
    tuple_liczb = tuple(lista_liczb)
    print("Lista liczb: ", lista_liczb)
    print("Tuple liczb: ", tuple_liczb)

def zadanie_7():
    nazwa_pliku = input("Podaj nazwe pliku: ")
    rozszerzenie_pliku = nazwa_pliku.split(".")
    # indeks [-1] wyswietla ostatni element listy
    print("Rozszerzenie pliku to: " + rozszerzenie_pliku[-1])

def zadanie_8():
    color_list = ["Red","Green","White" ,"Black"]
    print(color_list[0] + " " + color_list[-1])

def zadanie_9():
    exam_st_date = (11, 12, 2014)
    print("The examination will start from: %i %i %i" %exam_st_date)

### MAIN ###
# zadanie_1()
# zadanie_2()
# zadanie_3()
# zadanie_4()
# zadanie_5()
# zadanie_6()
# zadanie_7()
# zadanie_8()
# zadanie_9()