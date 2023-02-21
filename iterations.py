import random
import functools

class MyNumbers:
    def __init__(self):
        self.lst = [random.randint(0, 100) for i in range(100)]
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1  # self.count = self.count +1
        if self.count == len(self.lst):
            raise StopIteration()
        return self.lst[self.count]


class MyRange:
    def __init__(self, start, limit):
        self.start = start
        self.limit = limit
        self.count = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1  # self.count = self.count +1
        if self.count == self.limit:
            raise StopIteration()
        return self.count


# lst = MyRange(4, 100)
def double(n):
    return n*2

# lst = [1,2,3]
# doubled = list(map(double, lst))
# print(doubled)
#for i in MyRange(0,10):
 #   for j in MyRange(0,10):
  #      print(i,j)
def even_odd(lst):
    return len((list(filter(lambda x : x % 2 , lst)))), len((list(filter(lambda x : not x % 2 , lst))))
# print(even_odd([1,2,3,4,5,4,654,23]))

def is_string(dict):
    values = dict.items()
    return (list(filter(lambda x : not isinstance(x[1],str),values)))

# print(is_string({0:2,1:'dsf'}))\

def sum(lst):
    return functools.reduce(lambda a, b: a + b, lst)

# print(sum([1,2,3,14]))

