
lst = sorted([-1, -2, 1, 2, 3, -11, -1])
negative = [x for x in lst if x < 0]
positive = [y for y in lst if y > 0]


def func(pos: list, neg: list) -> list:
    if len(neg) > 0 and len(pos) > 0:
        return pos[0] if pos[0] <= abs(neg[-1]) else neg[-1]
    elif len(neg) == 0 and len(pos) > 0:
        return pos[0]
    elif len(pos) == 0 and len(neg) > 0:
        return neg[-1]

print(func(positive, negative))
