'''
Back in the day, people had fun turning "recipes" into surprise images using typewriters.

Use the provided recipe to create a recognizable image.

Chunks in the recipe are separated by a space.
Each chunk will tell you either
nl meaning NewLine (aka Carriage Return)
~or~
how many of the character and what character

For example:
4z means zzzz
1{ means {
10= means ==========
5bS means \\\\\ (see Abbreviations list below)
27 means 77
123 means 333333333333
(If a chunk is composed only of numbers, the character is the last digit.)

Abbreviations used:
sp = space
bS = backSlash \
sQ = singleQuote '
and
nl = NewLine
'''
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

b = input().split()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

dop = {'sp': ' ', 'bS': '\\', 'sQ': "'", 'nl': '\n'}
result = ''
res1 = ''
for i in b:
    if i.isdigit():
        result += int(i[:-1]) * i[-1]
    else:
        for k, j in enumerate(i):
            if j.isdigit():
                res1 += j
                continue
            else:
                if i[k:] in dop and len(res1) > 0:
                    result += int(res1) * dop[i[k:]]
                    res1 = ''
                    break
                elif len(res1) > 0:
                    result += int(res1) * i[k:]
                    res1 = ''
                    break
                elif i[k:] in dop and len(res1) == 0:
                    result += dop[i[k:]]
                    res1 = ''
                    break
                else:
                    result += i[k:]
print(result)
