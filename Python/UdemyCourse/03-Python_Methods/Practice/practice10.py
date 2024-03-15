def myfunc(st):
    s = ''

    for index, value in enumerate(st):
        if is_even(index) == True:
            s += value.lower()
        else:
            s += value.upper()
    return s


def is_even(num):
    return num % 2 == 0

print(myfunc("Anthropomorphism"))

li = [x*y for x in range(1,11) for y in range(1,11)]

print(li)