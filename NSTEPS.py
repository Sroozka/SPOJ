"""
https://www.spoj.com/problems/NSTEPS/
Starting from point (0,0) on a plane, we have written all non-negative integers 0, 1, 2,... as shown in the figure.
For example, 1, 2, and 3 has been written at points (1,1), (2,0), and (3, 1) respectively and this pattern has
continued.
You are to write a program that reads the coordinates of a point (x, y), and writes the number (if any) that
has been written at that point. (x, y) coordinates in the input are in the range 0...10000.
"""
t =int(input())

for i in range(t):
    list = input().split()
    num1 = int(list[0])
    num2 = int(list[1])
    if num1 == num2:
        if num1 % 2 == 0:
            print(num1 * 2)
        else:
            print((num1-1) * 2 + 1)
    elif num1 == num2 + 2:
        if num1 % 2 == 0:
            print(num1 + num2)
        else:
            print((num1 -1) + (num2-1) + 1)
    else:
        print("No Number")
    list =[]


