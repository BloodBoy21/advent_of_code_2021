inputData = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    inpData = [line.rstrip() for line in lines]

def getDepth(data):
    keyMap = {'up':0,'down':0,'forward':0}
    for newData in data:
        values = newData.split(' ')
        valueInt = int(values[1])
        keyMap[values[0]] +=valueInt
    print(keyMap)
    return (keyMap['down']-keyMap['up'])*keyMap['forward']

if __name__ == '__main__':
    value = getDepth(inpData)
    print(value)

