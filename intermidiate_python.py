### LISTS - list of values (string, int, float, ...)
def listy():
    jak_wyglada_lista = ['a', 'b', 'c']
    print(jak_wyglada_lista)
    print(jak_wyglada_lista[0])

### DICTIONARIES - similar to lists but each value is represented by an unchageable key
def slowniki():
    # Dictionary structure
    # dicitionary_name = {
    #     key: value,
    #     key: value
    #     }
    jak_wyglada_dictionary = {
       1: "maslo",
       2: "cukier",
       3: "jajko",
    }
    print(jak_wyglada_dictionary)
    print(jak_wyglada_dictionary[1])
    
    # GET function
    # print(dictionary_name.get())
    print(jak_wyglada_dictionary.get(3, "Znaleziono"))
    print(jak_wyglada_dictionary.get(4, "Nie znaleziono"))

### TUPLES - cannot be changed after being initialized
def tuple_niezmienna_lista():
    jak_wyglada_tuples_1 = ("gitara", "perkusja", "ukulele", "flet")
    jak_wyglada_tuples_2 = "owca", 'krowa', "kon", "kot", 'pies'
    print(jak_wyglada_tuples_1)
    print(jak_wyglada_tuples_1[3])
    print(jak_wyglada_tuples_2)
    print(jak_wyglada_tuples_2[3])

### TUPLES UNAPCKING - allows you to assign each item in a collection to a variable.
def odpakowane_tuple():
    numbers = (1, 2, 3)
    a, b, c = numbers
    print("Tuples NUMBERS:")
    print(a, b, c)

### SETS - unorganized values without indexes. A value does not have an index number
def sety_zestawy():
    letters = {'a', 'b', 'c', 'd', 'e'}
    # there is not number 3 in the set and the printed result is False <--- a boolean value
    print(3 in letters)
    # everytime this line runs the result is different (no indexed values)
    print(letters)
    # prints out the number of values in the set
    print('This set length is: ' + str(len(letters)))
    # set.add(value) <--- add a value to the set
    letters.add('f')
    # set.remove() <--- remove a value from the set
    letters.remove('a')
    print(letters)

### Mathematical operations on sets
def dzialania_matematyczne_na_setach():
    zbior_1 = {1, 2, 3, 4, 5, 6}
    zbior_2 = {4, 5, 6, 7, 8, 9}
    # Union operator | combines two sets to form a new one containing items in either.
    print('Union ' + str(zbior_1 | zbior_2))
    # Intersection operator & gets items only in both
    print('Intersection ' + str(zbior_1 & zbior_2))
    # Difference operator - gets items in the first set but not in the second
    print('Difference ' + str(zbior_1 - zbior_2))
    print('Difference ' + str(zbior_2 - zbior_1))
    # Symmetric difference operator ^ gets items in either set, but not both
    print('Symmetric difference ' + str(zbior_1 ^ zbior_2))

### Map & filter
def mapy():
    def add_five(x):
        return x + 5
    
    nums = [11, 22, 33, 44 , 55]
    result = list(map(add_five, nums))
    print(result)

    # Using lambda function makes it shorter
    result = list(map(lambda x: x+5, nums))
    print(result)

def filtry():
    # Also called predicate
    nums = [11, 22, 33, 44, 55]
    res = list(filter(lambda x: x%2 == 0, nums))
    print(res)

### Generators
def nieskonczone_generatory():
    def infinite_sevens():
        # Infinite loop
        while True:
            # Generator - they can be infinite because they yield one item at a time
            yield 7
            
    for i in infinite_sevens():
        print(i)

def skonczone_generatory():
    def numbers(x):
        for i in range(x):
            if i % 2 == 0:
                yield i
    print(list(numbers(11)))

### Decorators
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

print_text = decor(print_text)
print_text()

# Wrapping a function in a decorator by using @
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text()