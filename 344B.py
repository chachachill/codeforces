from functools import reduce
from sys import stdin

file = stdin

def read_line():
    return file.readline().strip()

def read_int():
    return int(read_line())


def string_list_to_int_list(x):
    return [int(e) for e in x]

[x, y, z] = [0, 0, 0]
[a, b, c] = string_list_to_int_list(read_line().split(" "))
total = sum([a, b, c])
if total % 2 != 0:
    print("Impossible")
else:
    y = (total / 2) - a
    z = b - y
    x = c - y
    if len(list(filter(lambda alpha: alpha < 0, [x, y, z]))) > 0:
        print("Impossible")
    else:
        print(str(int(z)) + " " + str(int(y)) + " " + str(int(x)))