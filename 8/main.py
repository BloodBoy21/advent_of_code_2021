from statistics import Counter
from collections import deque
import numpy as np

data = []
instructions = {}
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        key, value = line.split(" | ")
        instructions[key] = value
    numbers = [line.strip().split(" | ")[1] for line in lines]
    data = [x for num in numbers for x in num.split()]

counter = Counter(data)
numLen = [2, 3, 4, 7]
signals = list(filter(lambda x: len(x) in numLen, counter.keys()))
total = sum([counter[signal] for signal in signals])
print(total)

# part 2
def create_card(signal):
    return np.array(
        deque(Counter(list(signal))[e] for e in ["a", "b", "c", "d", "e", "f", "g"])
    )


def deduction(cards):
    # filter known cards
    one = [c for c in cards if sum(c) == 2][0]
    four = [c for c in cards if sum(c) == 4][0]
    seven = [c for c in cards if sum(c) == 3][0]
    eight = [c for c in cards if sum(c) == 7][0]
    # subset cards
    remaining_l5_cards = [c for c in cards if sum(c) not in [2, 4, 3, 7, 6]]
    remaining_l6_cards = [c for c in cards if sum(c) not in [2, 4, 3, 7, 5]]
    # deduce 3 and 6
    three = [c for c in remaining_l5_cards if len((c + one)[(c + one) == 2]) == 2][0]
    six = [c for c in remaining_l6_cards if len((c + one)[c + one == 2]) == 1][0]
    # subset the subset cards
    last_5s = [c for c in remaining_l5_cards if len((c - three)[c - three == 0]) != 7]
    last_6s = [c for c in remaining_l6_cards if len((c - six)[c - six == 0]) != 7]
    # deduce 2, 5
    five = [c for c in last_5s if len((c + six)[c + six == 2]) == 5][0]
    two = [c for c in last_5s if len((c - five)[c - five == 0]) != 7][0]
    # deduce 0, 9
    nine = [c for c in last_6s if len((c + three)[c + three == 2]) == 5][0]
    zero = [c for c in last_6s if len((c - nine)[c - nine == 0]) != 7][0]

    return [zero, one, two, three, four, five, six, seven, eight, nine]


decoded = []
for k in list(instructions.keys()):
    cards = [create_card(s) for s in k.split(" ")]
    outputs = [create_card(s) for s in instructions[k].split(" ")]
    res = deduction(cards)
    val = []
    for o in outputs:
        for idx, c in enumerate(res):
            if len((c - o)[c - o == 0]) == 7:
                val.append(idx)
    decoded.append(int("".join([str(i) for i in val])))

print(sum(decoded))
