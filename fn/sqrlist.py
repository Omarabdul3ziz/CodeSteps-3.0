def sqr(x):
    return x * x


def sqrlist(sequence):
    l = []
    for i in sequence:
        sqrd = sqr(i)
        l.append(sqrd)
    return l


print(sqrlist([1, 2, 3]))

