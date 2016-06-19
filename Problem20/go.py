def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

numbers=[]
for key in str(factorial(100)):
    numbers.append(int(key))

print sum(numbers)
