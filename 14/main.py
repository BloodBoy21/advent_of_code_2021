from collections import Counter 
with open('input.txt','r') as f:
    lines = f.readlines()
    formule = lines.pop(0).strip()
    elements = [[elemet  for elemet in line.strip().split(' -> ') ] for line in lines]
    rules={element[0]:element[1] for element in elements} 

def checkDict(dict,key,value):
    if key in dict:
        dict[key]+=value
    else: 
        dict[key]=value
    return dict


def polymerization(formule,days=10):
    pairs = {}
    for c in range(len(formule)-1):
        couple = formule[c]+formule[c+1]
        if couple in pairs:
            pairs[couple]+=1
        else:
            pairs[couple]=1
    for _ in range(days):
        newPairs = {}
        for couple,cnt in pairs.items():
            middle = rules[couple[0]+couple[1]]
            left = couple[0]+middle
            right = middle+couple[1]
            newPairs = checkDict(newPairs,left,cnt)
            newPairs = checkDict(newPairs,right,cnt)
        pairs = newPairs
    counter = Counter()
    for couple,cnt in pairs.items():
        counter[couple[0]]+=cnt
        counter[couple[1]]+=cnt
    counter[formule[0]]+=1
    counter[formule[-1]]+=1
    counter = Counter({k:v//2 for k,v in counter.items()})
    return max(counter.values())-min(counter.values()) 
print(polymerization(formule,40))


