'''
Your program must read the data from the standard input and write the result on the standard output.
Input:
Line 1: N, the number of temperatures to analyze
Line 2: A string with the N temperatures expressed as integers ranging from -273 to 5526
Output:
Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0.
Constraints
0 ≤ N < 10000
'''

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())  # the number of temperatures to analyse
lst = sorted(list(map(int, input().split())))


negative = [x for x in lst if x < 0]
positive = [y for y in lst if y > 0]


def get_number(pos: list[int], neg: list[int], n: int) -> list[int]:
    if n == 0:
        return 0
    if len(neg) > 0 and len(pos) > 0:
        return pos[0] if pos[0] <= abs(neg[-1]) else neg[-1]
    elif len(neg) == 0 and len(pos) > 0:
        return pos[0]
    elif len(pos) == 0 and len(neg) > 0:
        return neg[-1]


print(get_number(positive, negative, n))
