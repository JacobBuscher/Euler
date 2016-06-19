from itertools import izip as zip, count
alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print [x.upper() for x in alpha]
print [i for i, j in zip(count(), alpha) if j == 'baz']
def findNameScore(name,pos):
    global alpha
    score=0
    for key in name:
        score+=int([i for i, j in zip(count(), alpha) if j == key][0])+1
    return score*int(pos)

import ast
with open('input') as f:
    name=sorted(ast.literal_eval(f.read()))

nameLen=len(name)
i=0
totalScore=0
while i<nameLen:
    totalScore+=findNameScore(name[i],i+1)
    i+=1

print totalScore
