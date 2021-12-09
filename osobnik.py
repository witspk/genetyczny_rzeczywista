from random import randint
import copy


class Osobnik:

    # konstruktor int + str + kopia
    def __init__(self, *args):
        self.chromo = []
        if len(args) == 2:
            for a in args:
                self.chromo.append(float(a))
        if isinstance(args[0], Osobnik):
            self.chromo = copy.deepcopy(args[0].chromo)

    # wypisuje na konsole, na razie do testów
    def print(self):
        print(self.asString())

    # zwraca chromosom w postaci listy 2 string
    def asString(self):
        return str(self.chromo)


