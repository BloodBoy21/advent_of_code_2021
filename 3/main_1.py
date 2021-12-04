inputData = []
with open('input.txt','r') as f:
    lines = f.readlines()
    inputData = [line.rstrip() for line in lines]

def getVars(bits):
    gamma = ''
    epsilon = '' 
    for bit in bits:
        maxBit = max(bits[bit], key = lambda k: bits[bit][k])
        minBit = min(bits[bit], key = lambda k: bits[bit][k])
        gamma += f"{maxBit}"
        epsilon+= f"{minBit}"
    gamma = int(gamma,2)
    epsilon = int(epsilon,2)
    return gamma,epsilon

    

def getPowerConsumption(data):
    bits = {}
    for data_byte in data:
        for bit in range(len(data_byte)):
            value = int(data_byte[bit])
            if bit in bits:
                bits[bit][value] += 1 
            else:
                bits[bit]={0:0,1:0}
                bits[bit][value]=value
    print(bits)
    print(getVars(bits))

if __name__ == '__main__':
    getPowerConsumption(inputData)


