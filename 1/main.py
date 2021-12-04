import os 
inputData = []
with open('../input.text','r') as f:
    lines = f.readlines()
    inputData = [int(line.rstrip()) for line in lines]

def getMeasurements(data):
    count = 0
    for i in range(1,len(data)):
        if(data[i]>data[i-1]):
            count+=1
    return count
if __name__ == '__main__':
    count = getMeasurements(inputData)
    print(count)
