dataInput = []

with open('input.txt','r') as f:
    line = f.readline().strip()
    dataInput = [int(x) for x in line.split(',')]

class Sea():
    def __init__(self):
        self.fishes = []
    def day(self):
        fishesNow = len(self.fishes)
        for fish in self.fishes[:fishesNow]:
            fish.dayPast()
    def add(self, fish):
        fish.sea = self
        self.fishes.append(fish)

class Fish():
    def __init__(self,clock=8):
        self.clock = clock
        self.sea = None
    def dayPast(self):
        self.clock-=1
        if self.clock < 0 :
            self.clock = 6
            self.sea.add(Fish())
if __name__ == '__main__':
    sea = Sea()
    for age  in dataInput:
        fish = Fish(age)
        sea.add(fish)
    for day in range(80):
        sea.day()
    print(len(sea.fishes))
