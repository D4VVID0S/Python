# if, else, elif (elif == else if)
def warunki():
    print("Hello World")
    if 1 == 2:
        print("Yeah Baby")
    elif 1 == 1:
        print("Yo mama")

# Listy i zasięg
def listy_i_zasiegi():
    nums = list(range(5))
    for x in nums:
        print(x)

    print(nums[4])

# Wyswietlanie ostatniego znaku pobranego od uzytkownika wyrazu
    str = input()
    print(str[-1:])

# Szukanie słów, liczb w liscie
def przeszukanie_listy():
    lista_slow = ["klocki", "malpa", "drewno", "kupa", "osteoporoza", "paznokiec"]
    szukane_slowo = input()
    if szukane_slowo in lista_slow:
        print("Wyszukane slowo znajduje sie w liscie.")
    else:
        print("Niestety wyszukane slowo nie znajduje sie w liscie.")

    lista_liczb = [1, 3 , 5, 12, 18, 21, 33, 43, -2, -8, -123]
    szukana_liczba = int(input())
    if szukana_liczba not in lista_liczb:
        print("Niestety podana przez Ciebie liczba nie znajduje sie w liscie.")
    else:
        print("Podana przez Ciebie liczba znajduje sie w liscie.")