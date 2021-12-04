inputData = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    inputData = [line.rstrip() for line in lines]

def getDepth(data):
    aim,depth,pos = 0,0,0   
    for newData in data:
        value = newData.split(' ')
        valueInt = int(value[1])
        if value[0]=='forward':
            pos += valueInt
            depth += aim*valueInt
        elif value[0]=='up':
            aim-=valueInt
        else:
            aim+=valueInt
    return pos*depth
if __name__ == '__main__':
    value = getDepth(inputData)
    print(value)

