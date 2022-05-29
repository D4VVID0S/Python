### Przesukanie dictionary po kluczu ###
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
name = input()
for x in contacts:
    if name in x:
        print(str(x[0]) + " is " + str(x[1]))
        # print(str(x[0])) ---> wydrukuj tuple od x o indeksie [0]
        # każdy tuple ma dwie wartości czyli indeks od 0 do 1
        break
else:
    print('Not Found')

### Zmienne z gwiazdka biora tyle liczb z zasiegu ile to mozliwe i tworza z tego liste ###
a, b, c, d, *e, f, g = range(20)
print(range(20))
print(len(e))

### Sprawdzanie czy liczba jest pierwsza za pomoca generatora skonczonego ###
def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    for number in range(a, b):
        if isPrime(number):
            yield number
    
f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))

# LETTER COUNTER
text = input()
dict = {}

for char in text:
    dict[char] = text.count(char)
print(dict)

### Example ###
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

### Lambda - anonymous function
def my_func(f, arg):
    print(f(arg))
    return f(arg)

my_func(lambda x: 2*x*x, 5)

# Classes
class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width*self.height)

class Rectangle(Shape):
    #your code goes here
    def perimeter(self):
        print(2*(self.width+self.height))
    

w = int(input())
h = int(input())

r = Rectangle(w, h)
r.area()
r.perimeter()

