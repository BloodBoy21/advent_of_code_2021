from collections import Counter
fishes = []
with open('input.txt','r') as f:
    line = f.readline().strip()
    fishes = [int(x) for x in line.split(',')]


count = Counter(fishes)

for day in range(80):
    zeros = count[0]
    for fish in range(9):
        if fish == 6:
            count[fish] = count[fish+1]
            count[fish] += zeros
        elif fish==8:
            count[fish] = zeros
        else:
          count[fish] = count[fish+1]
          

print(sum(i for i in count.values())
