#!/usr/bin/python

with open('input') as f:
    content = f.readlines()

i=0
while i<len(content):
    content[i]=content[i].translate(None, '\n').split()
    i+=1
print content

#85 59 93
def findLarge(x):
    xLen=len(x)
    i=0
    result=[]
    while i<xLen:
        if i!=xLen-1:
            result.append([x[i],x[i+1]])
        i+=1
    resultLen=len(result)
    i=0
    while i<resultLen:        
        if int(result[i][0])>int(result[i][1]):
            result[i]=result[i][0]
        else:
            result[i]=result[i][1]
        i+=1
    return result
#print findLarge([10, 13, 15])
#exit()

contentLen=len(content)-1
i=0
lastP=findLarge(content[-1])
while i<=contentLen:
    content[contentLen-i]
    i+=1
    nextP=findLarge(content[contentLen-i])
    if nextP==lastP:
        continue
    j=0
    cShortLen=len(content[contentLen-i])
    while j<cShortLen:
        #print 'fire'
        #print content[contentLen-i]
        #print nextP
        #print lastP
        content[contentLen-i][j]=int(content[contentLen-i][j])+int(lastP[j])
        print content[0]
        j+=1
    content[contentLen-i+1]=content[contentLen-i]
    #print content
    lastP=findLarge(content[contentLen-i])
