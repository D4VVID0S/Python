# https://www.w3resource.com/python-exercises/python-basic-exercises.php

# sys - zadanie 2 - dodaje informacje o wersji pythona
import sys
# datetime - zadanie 3 - dodaje czas
import datetime
# math - zadanie 4 - importuje rzeczy potrzebne do obliczen matematycznych (np. pi, sqrt)
from math import *
# calendar - dodaje kalendarz
import calendar
# importuje daty
from datetime import date

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

def zadanie_10():
    x = int(input("Podaj liczbe: "))
    x1 = int("%s" % x)
    x2 = int("%s%s" % (x, x))
    x3 = int("%s%s%s" % (x, x, x))
    print(x1 + x2 + x3)

def zadanie_11():
    # wyswietla docstring funkcji podanej jako argument
    print(abs.__doc__)

def zadanie_12():
    rok = int(input("Podaj rok: "))
    miesiac = int(input("Podaj miesiac: "))
    print(calendar.month(rok, miesiac))

def zadanie_13():
    print("""
    a string that you "don't" have to escape
    This
    is a  ....... multi-line
    heredoc string --------> example
    """)

def zadanie_14():
    f_date = date(2014, 7, 2)
    l_date = date(2014, 7, 11)
    delta = l_date - f_date
    print(delta.days)

def zadanie_15():
    radius = 6
    print(4/3*pi*radius**3)

def zadanie_16():
    num = int(input())
    if num <= 17:
        print(print(abs((num-17)*2)))
    else:
        print(num - 17)

def z17():
    num = int(input())
    if (1000 - num) <= 100 or (2000 - num) <= 100:
        print(True)
    else:
        print(False)

def z18():
    a = int(input())
    b = int(input())
    c = int(input())
    sum = a + b + c

    if a == b == c:
        print(sum * 3)
    else:
        print(sum)

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
# zadanie_10()
# zadanie_11()
# zadanie_12()
# zadanie_13()
# zadanie_14()
# zadanie_15()
# zadanie_16()
# z17()
z18()