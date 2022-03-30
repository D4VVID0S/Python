# # LETTER COUNTER
# text = input()
# dict = {}

# for char in text:
#     dict[char] = text.count(char)
# print(dict)

### Example ###
# points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
# x = points.count(9)
# print(x)

### Lambda - anonymous function - 
def my_func(f, arg):
    print(f(arg))
    return f(arg)

my_func(lambda x: 2*x*x, 5)