# https://www.w3resource.com/python-exercises/python-basic-exercises.php

# sys - zadanie 2 - dodaje informacje o wersji pythona
from distutils.log import error
from hashlib import new
from re import I, X
import sys
# datetime - zadanie 3 - dodaje czas
import datetime
# math - zadanie 4 - importuje rzeczy potrzebne do obliczen matematycznych (np. pi, sqrt)
from math import *
# calendar - dodaje kalendarz
import calendar
# importuje daty
from datetime import date
# funkcja os.path.isfile/os.path.exists by sprawdzić czy plik istnieje/jest dostepny
import os.path

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

def z19():
    str = input()
    def new_string(str):
        if len(str) >= 2 and str[:2] == "Is":
            return str
        return "Is" + str
    print(new_string(str))

def z20():
    str = input("Podaj stringa: ")
    n = int(input("Podaj ile razy ma sie powtorzyc string: "))
    print(str * n)

def z21():
    def is_even(x):
        if x % 2 == 0:
            return "The given number is even."
        else:
            return "The given number is odd."
    num = int(input("Give a number to check if it is even or odd: "))
    print(is_even(num))

def z22():
    nums = input("Podaj iles licz. Kazda oddzielna liczba po spacji: ")
    nums = nums.split()
    x = input("Podaj liczbe do sprawdzenia czy jest w liscie: ")
    print(nums.count(x))
    
def z23():
    str = input("Podaj stringa: ")
    n = int(input("Podaj ile razy potworzyc pierwsze dwie litery stringa: "))
    print(str[:2] * n)

def z24():
    def isVowel(letter):
        if letter in vowels:
            return "The given letter is a vowel."
        else:
            return "The given letter is not a vowel."

    vowels = 'aeiou'
    ch = input("Give a letter to check if it is a vowel: ")
    print(isVowel(ch))

def z25():
    def str_to_int(lista):
        for i in range(len(lista)):
            lista[i] = int(lista[i])
    
    x = int(input("Podaj liczbe: "))
    nums = input("Podaj liste liczb. Kazda liczba oddzielona spacja: ")
    nums = nums.split()
    str_to_int(nums)
    print(x in nums)  

def z26():
    def str_to_int(lista):
        for i in range(len(lista)):
            lista[i] = int(lista[i])

    def histogram(letter, x):
        for i in range(len(x)):
            print(letter * x[i])

    znak = input("Podaj znak do histogramu: ")
    n = input("Podaj liste licz oddzielone spacja: ")
    n = n.split()
    str_to_int(n)
    histogram(znak, n)

def z27():
    def konkatenacja(nums):
        result = ''
        for i in nums:
            result += str(i)
        return result

    nums = input("Podaj liste liczb kazda oddzielona spacja: ")
    nums = nums.split()
    print(konkatenacja(nums))

def z28():
    numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

    for i in numbers:
        if i == 237:
            print(i)
            break
        elif i % 2 ==0:
            print(i)

def z29():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])

    print(color_list_1 - color_list_2)

def z30():
    podstawa = float(input("Podaj podstawe trojkata:"))
    wysokosc = float(input("Podaj wysokosc trojkata:"))

    print(podstawa * wysokosc / 2)

def z31():
    print("Obliczanie najwiekszego wspolnego dzielnika")
    x = int(input("Podaj x: "))
    y = int(input("Podaj y:"))

    def nwd(a, b):
        while b:
            temp = a
            a = b
            b = temp%b
        return a
    print(nwd(x, y)) 

def z32():
    def nwd(a, b):
        while b:
            temp = a
            a = b
            b = temp%b
        return a

    def nww(a, b):
        return a * b // nwd(a, b)

    print("Obliczanie najwiekszego wspolnego dzielnika")
    x = int(input("Podaj x: "))
    y = int(input("Podaj y:"))
    print(nww(x, y)) 

def z33():
    x = int(input("Podaj x:"))
    y = int(input("podaj y:"))
    z = int(input("Podaj z:"))

    if x == y or x == z or y == z:
        print(0)
    else:
        print(x + y + z)

def z34():
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    
    if a + b in range(15, 21):
        print("Suma jest w przedziale (15, 20) zatem rowna sie 20.")
    else:
        print(a + b)

def z35():
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))

    if a == b or a + b == 5 or a - b == 5 or b - a == 5:
        print(True)
    else:
        print(False)

def z36():
    def if_intiger(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return "Input musi byc intigerem!"

    print(if_intiger(10, 20))
    print(if_intiger(10, 20.23))
    print(if_intiger('5', 6))
    print(if_intiger('5', '6'))

def z37():
    def personal_details(name, age, adres):
        print("Name: {}\nAge: {}\nAddress: {}".format(name, age, adres))
    name = input("Podaj imie: ")
    age = input("Podaj wiek: ")
    adres = input("Podaj adres: ")
    personal_details(name, age, adres)

def z38():
    while True:
        try:
            x = float(input("Podaj X:"))
            y = float(input("Podaj Y:"))
            res = (x+y)**2
            print(res)
            break
        except Exception as e:
            # error_string = str(e)
            # print(error_string)
            print("Something went wrong.")

def z40():
    while True:
        try:
            p1 = [int(input("Podaj X1:")), int(input("Podaj Y1:"))]
            p2 = [int(input("Podaj X2:")), int(input("Podaj Y2:"))]

            res = [p1[0] - p2[0], p1[1] - p2[1]]
            print(res)
            break
        except Exception as e:
            # error_string = str(e)
            # print(error_string)
            print("Something went wrong.")

def z41():
    print(os.path.isfile('main.txt'))
    print(os.path.isfile('main.py'))
    print(os.path.exists('main.txt'))
    print(os.path.exists('main.py'))


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
# z18()
# z19()
# z20()
# z21()
# z22()
# z23()
# z24()
# z25()
# z26()
# z27()
# z28()
# z29()
# z30()
# z31()
# z32()
# z33()
# z34()
# z35()
# z36()
# z37()
# z38()
# z40()
z41()