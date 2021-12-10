from collections import Counter

bracketInput = open("input.txt", "r").readlines()

bracketsMatch = {")": "(", "}": "{", "]": "[", ">": "<"}
bracketsPoints = {")": 3, "}": 1197, "]": 57, ">": 25137}
noMatch = []

for line in bracketInput:
    stack = []
    for bracket in line.strip():
        if bracket in bracketsMatch:
            bracketPair = stack.pop()
            if bracketPair != bracketsMatch[bracket]:
                noMatch.append(bracket)
                stack = []
                break
        else:
            stack.append(bracket)

bracketsCount = Counter(noMatch)
total = sum([bracketsCount[key] * bracketsPoints[key] for key in bracketsCount.keys()])
print(total)
# part 2

score_map = {"(": 1, "[": 2, "{": 3, "<": 4}


def get_completion_score(line):
    stack = []
    for ch in line.strip():
        if ch in score_map:
            stack.append(ch)
        else:
            top = stack.pop() if stack else None
            if top != bracketsMatch[ch]:
                return 0
    score = 0
    for ch in reversed(stack):
        score *= 5
        score += score_map[ch]
    return score


line_scores = [get_completion_score(line) for line in bracketInput]
incomplete_scores = sorted([score for score in line_scores if score != 0])
print(incomplete_scores[len(incomplete_scores) >> 1])
