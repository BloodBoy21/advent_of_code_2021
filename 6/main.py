import multiprocessing
dataInput = []

with open('input.txt','r') as f:
    line = f.readline().strip()
    dataInput = [int(x) for x in line.split(',')]

class Sea():
    def __init__(self,fishes=[]):
        self.fishes = fishes
    def day(self):
        fishesNow = len(self.fishes)
        for fish in self.fishes[:fishesNow]:
            fish.dayPast()
    def add(self, fish):
        fish.sea = self
        self.fishes.append(fish)
    def split(self,fishes):
        newSea = self.fishes[:fishes]
        self.fishes = self.fishes[fishes:]
        return newSea
    def updateSea(self):
        for fish in self.fishes:
            fish.sea = self
    def __len__(self):
        return len(self.fishes) 
class Fish():
    def __init__(self,clock=8):
        self.clock = clock
        self.sea = None
    def dayPast(self):
        self.clock-=1
        if self.clock < 0 :
            self.clock = 6
            self.sea.add(Fish())

manager = multiprocessing.Manager()
result = manager.list()
def pastDays(sea):
    for day in range(80):
        sea.day()
    result.append(len(sea))
    print(len(sea))


if __name__ == '__main__':
    seas = [Sea()]
    selectSea = 0
    processes = []
    for age  in dataInput:
        fish = Fish(age)
        seas[selectSea].add(fish)
        if len(seas[selectSea].fishes)>=100:
            newSea = Sea(seas[selectSea].split(50))
            newSea.updateSea()
            seas.append(newSea)
            selectSea+=1
    print([len(sea.fishes) for sea in seas])
    for sea in seas:
        p = multiprocessing.Process(target=pastDays,args=[sea])
        processes.append(p)
        wea = sea
    for i in range (len(processes)):
        processes[i].start()
        print("processes:",i)
        processes[i].join()
    print(sum(result))
