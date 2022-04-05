# Magic Methods

def common_operators():
    ### Common operators
    # __add__ for +
    # __sub__ for -
    # __mul__ for *
    # __truediv__ for /
    # __floordiv__ for //
    # __mod__ for %
    # __pow__ for **
    # __and__ for &
    # __xor__ for ^
    # __or__ for |

    class SpecialString:
        def __init__(self, cont):
            self.cont = cont

        def __truediv__(self, other):
            line = "=" * len(other.cont)
            # Wyswietlenie czegokolwiek dopiero przy returnie wartości do printa
            return "\n".join([self.cont, line, other.cont])

    spam = SpecialString("spam")
    hello = SpecialString("Hello world!")
    print(spam / hello)

def comparisons():
    ### Comparisons
    # __lt__ for <      - less than
    # __le__ for <=     - less or equal
    # __eq__ for ==     - equal
    # __ne__ for !=     - not equal
    # __gt__ for >      - greater than
    # __ge__ for >=     - greater or equal

    class SpecialString:
        def __init__(self, cont):
            self.cont = cont

        def __gt__(self, other):
            for index in range(len(other.cont)+1):
                result = other.cont[:index] + ">" + self.cont
                result += ">" + other.cont[index:]
                print(result)

    spam = SpecialString("spam")
    eggs = SpecialString("eggs")
    spam > eggs

def methods_class_to_container():
    ### Methods to make classes act like containers
    # __len__ for       - len()
    # __getitem__       - indexing
    # __setitem__       - assigning to indexed values
    # __delitem__       - deleting indexed values
    # __iter__          - iteration over objects (e.g., in for loops)
    # __contains__      - in

    import random
    class VagueList:
        def __init__(self, cont):
            self.cont = cont

        def __getitem__(self, index):
            return self.con[index + random.randint(-1, 1)]

        def __len__(self):
            return random.randint(0, len(self.cont)*2)

    vague_list = VagueList(["A", "B", "C", "D", "E"])
    print(len(vague_list))      # uses __len__ method
    print(len(vague_list))      # uses __len__ method
    print(vague_list[2])        # uses __getitem__ method
    print(vague_list[2])        # uses __getitem__ method