from sys import stdin

file = stdin


def read_line():
    return file.readline().strip()


def read_int():
    return int(read_line())


def string_list_to_int_list(x):
    return [int(e) for e in x]

[n, x] = string_list_to_int_list(read_line().split())
time_list = []
for e in range(n):
    time_list.append(string_list_to_int_list(read_line().split()))

time_list.sort(key=lambda y: y[0])

minutes = 0
current = 1
for e in range(n):
    [start, end] = time_list[e]
    nearest = current + (((start - current)//x) * x)
    #print("current", current)
    minutes += end - nearest + 1
    #print("minutes", minutes)
    current = end + 1

print(minutes)