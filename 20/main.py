L = open("input.txt").read()
M = [c == "#" for c in L[:512]]
C = {
    (x, y): c == "#" for y, l in enumerate(L.splitlines()[2:]) for x, c in enumerate(l)
}
Z = [-1, 0, 1]
v = lambda C, x, y, z: M[
    sum(C.get((x + a, y + b), z) * 2 ** (4 - 3 * b - a) for b in Z for a in Z)
]


def F(C, i, z=0):
    for _ in range(i):
        p, q = [range(a - 2, b + 2) for a, b in zip(min(C), max(C))]
        C = {(x, y): v(C, x, y, z) for x in p for y in q}
        z = M[2 ** (9 * z) - 1]
    return sum(C.values())


print("Part 1: {:d}".format(F(C, 2)))
print("Part 2: {:d}".format(F(C, 50)))
