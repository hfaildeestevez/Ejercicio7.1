tuplinha = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tuplinhainversa = (9, 8, 7, 6, 5, 4, 3, 2, 1)


def orden(listao):
    if listao[0] > listao[1]:
        return "De mayor a menor"
    else:
        return "De menor a mayor"


print(orden(tuplinha))
