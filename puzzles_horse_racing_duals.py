'''
Casablanca’s hippodrome is organizing a new type of horse racing: duals. During a dual, only two horses will participate in the race. In order for the race to be interesting, it is necessary to try to select two horses with similar strength.

Write a program which, using a given number of strengths, identifies the two closest strengths and shows their difference with an integer (≥ 0).
'''
lst = []
lst1 = []
n = int(input())
for i in range(n):
    pi = int(input())
    lst.append(pi)
lst = sorted(lst)
for i in range(len(lst)+1):
    if i+1 < len(lst):
        lst1.append(lst[i+1]-lst[i])
print(min(lst1))
