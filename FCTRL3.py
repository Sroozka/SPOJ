import numpy
t = int(input()) #number of tests
space = " "

for i in range(t):
    silnia = int(input())
    if silnia == 0: number = "0 1"

    elif silnia <= 3:
        factor = numpy.prod(range(1,silnia+1))
        numbers = str(factor)
        number = "0 " + numbers[-1]

    elif silnia <=9:
        factor = numpy.prod(range(1, silnia + 1))
        numbers = str(factor)
        number = numbers[-2] + space + numbers[-1]

    else: number = "0 0"
    print(number)
