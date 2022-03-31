# contacts = [
#     ('James', 42),
#     ('Amy', 24),
#     ('John', 31),
#     ('Amanda', 63),
#     ('Bob', 18)
# ]

# name = input()

# for x in contacts:
#     if name in x:
#         print(str(x[0]) + " is " + str(x[1]))
#         # print(str(x[0])) ---> wydrukuj tuple od x o indeksie [0]
#         # każdy tuple ma dwie wartości czyli indeks od 0 do 1
#         break

# else:
#     print('Not Found')

a, b, c, d, *e, f, g = range(20)
print(range(20))
print(len(e))