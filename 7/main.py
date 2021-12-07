from collections import Counter
from statistics import median, mean

inputData = open("input.txt", "r").readline().split(",")
inputData = [int(x) for x in inputData]
medianPos = int(median(inputData))
meanPos = int(mean(inputData))
# totalFuel = sum(abs(medianPos - pos) for pos in inputData) #Part 1
totalFuel = sum(abs(pos - meanPos) * (abs(pos - meanPos) + 1) // 2 for pos in inputData)
print(totalFuel)
