from functools import reduce
from sys import stdin

file = stdin

def read_line():
    return file.readline().strip()


def read_int():
    return int(read_line())


def string_list_to_int_list(x):
    return [int(e) for e in x]

cases = read_int()
changes = 0
previous = "00"
for case in range(cases):
    now = read_line()
    if now != previous:
        changes += 1
    previous = now

print(changes)