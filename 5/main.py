inputData = []

with open('input.txt','r') as f:
    lines = f.readlines()
    inputData = [line.strip().split(' -> ') for line in lines]
    inputData = [[[int(x) for x in num.split(',')] for num in line] for line in inputData]


class Cloud():
    def __init__(self,coordinates):
        self.coordinates = coordinates
        self.points = []
        self.commountPoint = 0
        self.endPoint = 0
        self.__createPoints()
    def __createPoints(self):
        self.__orderCoordinates()
        firstCoordinate = self.coordinates[0]
        secondCoordinate = self.coordinates[1]
        for i in range(2):
            if i  == self.endPoint:
                for point in range(firstCoordinate[i],secondCoordinate[i]+1):
                    newPoint = [0]*2
                    newPoint[i] = point
                    newPoint[self.commountPoint] = firstCoordinate[self.commountPoint]
                    self.points.append(newPoint)

    def __orderCoordinates(self):
        firstCoordinate = self.coordinates[0]
        secondCoordinate = self.coordinates[1]
        for i in range(2):
            p1,p2 = firstCoordinate[i],secondCoordinate[i]
            if p1 == p2:
                self.commountPoint = i 
            else:
                self.endPoint  = i
                p1,p2 = (p2,p1) if p1>p2 else (p1,p2)
                self.coordinates[0][i]=p1
                self.coordinates[1][i]=p2

class HashMap():
    def __init__(self,data={}):
        self.dataDict = data
    def __hashKey(self,value):
        return  f"{value[0]}-{value[1]}"
    def add(self,value,data):
        key =  self.__hashKey(value)
        if not (key in self.dataDict):
            self.dataDict[key] = [data]
        else:
            self.dataDict[key].append(data)
    def filterBySizeUp(self,size):
        count = 0
        for _,lists in self.dataDict.items():
            if len(lists) >= size:
                count += 1
        return count

def filterClouds(clouds):
    newClouds = []
    for cloud in clouds:
        x1,x2 = cloud[0][1],cloud[1][1]
        y1,y2 = cloud[0][0],cloud[1][0]
        if x1 == x2 or y1 == y2:
            newClouds.append(Cloud(cloud))
    return newClouds

def getWarningPoints(cloudsData):
    points= HashMap()
    clouds = filterClouds(cloudsData)
    for cloud in clouds:
        for point in cloud.points:
            points.add(point,1)
    print(points.filterBySizeUp(2))

getWarningPoints(inputData)
 
