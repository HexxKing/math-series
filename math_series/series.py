def fibonacci(n):
    if n < 0:
        print("doesn't work, pick a different number")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def lucas(n):
    if (n == 0) : 
        return 2
    if (n == 1) : 
        return 1 
    return lucas(n - 1) + lucas(n - 2)

def sum_series(n, )