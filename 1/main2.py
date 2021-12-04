inputData = []
with open('../input.text','r') as f:
    lines = f.readlines()
    inputData = [int(line.rstrip()) for line in lines]


def getSum(data,start,end):
    total = 0
    for i in range(start,end+1):
        total += data[i]
    return total

def getMeasurement(data):
    count = 0
    oldCount = getSum(data,0,2)
    for i in range(3,len(data)):
        currentCount = getSum(data,i-2,i)
        if (currentCount>oldCount):
            count+=1
        oldCount = currentCount
    return count




if __name__ == '__main__':
    count = getMeasurement(inputData)
    print(count)


