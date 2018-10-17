

def gcd(m: int, n: int) -> int:
    m = abs(m)
    n = abs(n)
    if m == 0 and n == 0:
        raise Exception("Нет общего делителя для двух нулей")

    if m == 0 and n != 0:
        return n
    
    if n == 0 and m != 0:
        return m
  
    if n == 1 or m == 1:
        return 1

    if m == n:
        return m
    
    if m > n:
	    m = m - n
	    return gcd(m, n)
    else:
	    n = n - m
	    return gcd(m, n)



