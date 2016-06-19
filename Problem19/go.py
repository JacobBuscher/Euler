september=april=june=november=29
january=march=may=july=august=october=december=30
february=27
leapFeb=28
week=['Monday','Tuesday','Wednessday','Thursday','Friday','Saturday','Sunday']
yearNum=1901

year=[january,february,march,april,may,june,july,august,september,october,november,december]
print year
print len(year)
print sum(year)

def getNextMonth(currentWeek,currentMonth):
    global week, year, yearNum
    currentMonthNum=year[currentMonth]
    if currentMonth+1==2:
        if yearNum%4==0:
            print 'leap!!!'
            currentMonthNum=leapFeb
    if currentMonth<len(year)-1:
        yearKey=currentMonth+1
        nextMonth=year[yearKey]
    else:
        yearNum+=1
        yearKey=0
        nextMonth=year[yearKey]
    print currentMonthNum
    left=currentMonthNum+1%7
    left=left+currentWeek
    return [left%7, yearKey, yearNum]


depth=1200
i=0
j=0
start=[1,0]
while i<depth:
    start=getNextMonth(start[0], start[1])
    print str(week[start[0]])+' '+str(start[1]+1)+' '+str(yearNum)
    if start[0]==6:
        j+=1
    i+=1
    #sam=raw_input()
print j
