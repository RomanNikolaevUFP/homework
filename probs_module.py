from random import randint

def get_random_list(n):
    a = []
    for i in range(n):
        a.append(randint(0, 1))
    return a

def get_prob(data, pattern):
    n = len(pattern)
    c = 0
    for i in range(len(data) - n + 1):
        if data[i: i+n] == pattern:
            c += 1
    return c / (len(data) - n + 1)
