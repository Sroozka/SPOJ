"""
https://www.spoj.com/problems/STRHH/
Given a sequence of 2*k characters, please print every second character from the first half of the sequence.
Start printing with the first character.
"""

t = int(input())
for i in range(t):
    x = input()
    half = int(len(x)/2)
    print(x[0:half:2])