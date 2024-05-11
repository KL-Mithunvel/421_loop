def calc(a):
    if a % 2 == 0:
        return even(a)
    else:
        odd(a)


def even(a):
    op = a*2
    return op


def odd(a):
    op = (3*a)+1
    return op
