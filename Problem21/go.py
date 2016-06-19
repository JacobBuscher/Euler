def divisors(n):
    return {x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x}

def amicable(n):
    a=sum(divisors(n))
    if sum(divisors(a)) == n and n != a:
        return True

depth=list(xrange(10001))
friendly=[]
for key in depth:
    if amicable(key):
        friendly.append(key)

print sum(friendly)
