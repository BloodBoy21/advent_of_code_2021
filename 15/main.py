import sys
from pprint import pprint
import networkx as nx


def load_data(datafile):
    with open(datafile) as df:
        data = [list(map(int, line.strip())) for line in df.readlines()]
    return data


def gen_nx_graph(data):
    G = nx.DiGraph()
    for y in range(len(data)):
        for x in range(len(data)):
            G.add_node((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x_, y_ = x + dx, y + dy
                if 0 <= x_ < len(data) and 0 <= y_ < len(data):
                    G.add_edge((x, y), (x_, y_), weight=data[y_][x_])

    return G


def _main():
    datafile = "input.txt"

    data = load_data(datafile)
    idx = len(data) - 1

    # Part 1
    G = gen_nx_graph(data)
    print(G)
    path = nx.shortest_path(G, source=(0, 0), target=(idx, idx), weight="weight")
    risk = sum(data[y][x] for x, y in path[1:])
    print(risk)

    # Part 2
    cave = [None] * (5 * len(data))
    for i in range(len(data)):
        for j in range(5):
            cave[len(data) * j + i] = data[i] * 5

    for i in range(5):
        for j in range(5):
            if i == j == 0:
                continue

            for k in range(len(data)):
                for l in range(len(data)):
                    x, y = i * len(data) + k, j * len(data) + l
                    cave[y][x] += i + j
                    if cave[y][x] > 9:
                        cave[y][x] -= 9

    G = gen_nx_graph(cave)
    idx = len(cave) - 1
    print(G)
    path = nx.shortest_path(G, source=(0, 0), target=(idx, idx), weight="weight")
    risk = sum(cave[y][x] for x, y in path[1:])
    print(risk)


if __name__ == "__main__":
    _main()
