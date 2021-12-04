dataInput = []
with open('input.txt','r') as f:
    lines= f.readlines()
    dataInput = [line.rstrip() for line in lines]


def getOxygenRate(data,index=0):
    if len(data)<=1 :return data
    bitMap = {0:[],1:[]}
    for byte in data:
        bit = int(byte[index])
        bitMap[bit].append(byte)
    oneIsMax = len(bitMap[1])>len(bitMap[0])
    if oneIsMax or len(bitMap[1]) == len(bitMap[0]):
        return getOxygenRate(bitMap[1],index+1)
    return getOxygenRate(bitMap[0],index+1)

def getCO2Rate(data,index=0):
    if len(data)<=1 :return data
    bitMap = {0:[],1:[]}
    for byte in data:
        bit = int(byte[index])
        bitMap[bit].append(byte)
    oneIsMax = len(bitMap[1])>len(bitMap[0])
    if oneIsMax or len(bitMap[1]) == len(bitMap[0]):
        return getCO2Rate(bitMap[0],index+1)
    return getCO2Rate(bitMap[1],index+1)

if __name__ == "__main__":
    oxygen = getOxygenRate(dataInput)[0]
    co2 = getCO2Rate(dataInput)[0]
    print(oxygen,co2)
    oxygen = int(oxygen,2)
    co2 = int(co2,2)
    print(f"{oxygen}*{co2}={oxygen*co2}")
    
