'''
Peter wants to generate some prime numbers for his cryptosystem. Help him!
Your task is to generate all prime numbers between two given numbers!

Input
The input begins with the number t of test cases in a single line (t<=10).
In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000,
n-m<=100000) separated by a space.

Output
For every test case print all prime numbers p such that m <= p <= n, one number per line,
test cases separated by an empty line.
'''
import  math

def porownaj(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            break
    else:
        print(x)

t = int(input()) #number of tests

for i in range(t):
    m, n = map(int, input().split())
    if m % 2 == 0: m = m-1

    for x in range(m, n + 1, 1):
        if x == 1:
            continue
        elif x == 2:
            print(x)
        else:
            if ((x+1)%6 == 0) or ((x-1)%6 == 0):
                porownaj(x)


"""
t = int(input()) #number of tests

for i in range(t):
numbers = input().split()
    m = int(numbers[0])
    n = int(numbers[1])
    for x in range(m, n+1):
        if x == 1: continue
        elif x == 2: print(x)
        elif x == 3: print(x)
        elif (x+1)%6 == 0:
            for y in list:
                if x % y == 0: continue
            print(x)
            list.append(x)

        elif (x-1)%6 == 0:
            for y in list:
                if x % y == 0: continue
            print(x)
            list.append(x)

    print(list)
"""
"""
t = int(input()) #number of tests

for i in range(t):
    numbers = input().split()
    m = int(numbers[0])
    n = int(numbers[1])
    a = 20
    for x in range(m, n+1):
        if ((x + 1) % 6 == 0) or ((x - 1) % 6 == 0):
            if a**(x-1) % x == 1: print(x)
"""