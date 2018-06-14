def power(a, n):
    if(n == 0):
        return 1
    else:
        return a * power(a,n-1)

def facOf(n):
    if(n == 1):
        return 1
    else:
        return n * facOf(n-1)