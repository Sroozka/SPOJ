"""Pociąg z miejscowości A do B jedzie z prędkością v1, a wraca z miejscowości B do A z prędkością v2.
 Obliczyć średnią prędkość na całej trasie. Uwaga: Dane wejściowe będą tak dobrane, aby wynik był liczba całkowitą."""

t = int(input()) #number of tests
sum_of_x = 0
multip_of_x = 1
result = []

for i in range(t):
    for x in input().split():
        sum_of_x += int(x)
        multip_of_x *= int(x)

    vsr = 2*multip_of_x/sum_of_x #mean velocity
    #print(vsr)
    result.append(int(vsr))
    sum_of_x = 0
    multip_of_x = 1

for x in result:
    print(x)

"""
Prędkość średnia
vr = (2*vr1*vr2)/(vr1+vr2)
"""