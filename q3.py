from decimal import *
def generator():
    result = []
    i = 2
    while i != 6:

        result.append(Decimal(i))
        i += 0.5
    return result

print(generator())