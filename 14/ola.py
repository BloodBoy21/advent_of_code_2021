from collections import Counter
def main():
  lines = [l.strip() for l in open('input.txt').readlines()]
  start = lines[0]
  rules = {r[0]: r[1] for r in [l.split(' -> ') for l in lines[2:]]}
  
  pairs = {}
  for i in range(len(start)-1):
    couple = start[i] + start[i+1]
    if couple in pairs:
      pairs[couple]+=1
    else:
      pairs[couple]=1
  
  for runs in range(40):
    new_pairs = {}
    for couple,cnt in pairs.items():
      middle = rules[couple[0] + couple[1]]
      left = couple[0] + middle
      right = middle + couple[1]
      if left in new_pairs:
        new_pairs[left]+=cnt
      else:
        new_pairs[left]=cnt
      if right in new_pairs:
        new_pairs[right]+=cnt
      else:
        new_pairs[right]=cnt
    pairs = new_pairs
  
  ttls = Counter()
  for couple, cnt in pairs.items():
    ttls[couple[0]] += cnt
    ttls[couple[1]] += cnt
  ttls[start[0]] += 1
  ttls[start[-1]] += 1
  ttls = Counter({ k: v//2 for k,v in ttls.items()})
  
  
  print(ttls.most_common()[0][1] - ttls.most_common()[-1][1])
main()
