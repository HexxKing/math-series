def fibonacci(n):
    if n < 0:
        print("doesn't work, pick a different number")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def lucas(x):
    if (x == 0) : 
        return 2
    if (x == 1) : 
        return 1 
    return lucas(x - 1) + lucas(x - 2)

def sum_series(n, x = 0, y = 1):
    if n < 0:
        return "nope"
    if n == 0:
        return fibonacci(x)
    if n > 0:
        return sum_series(n-1) + sum_series(n-2)
    if x == 2:
        return lucas(x)
    if x != 2 and y != 1:
        other_series = ()
        other_series.append(x, y)
        z = x + y
        other_series.append(z)
        x = other_series[y]
        y = other_series[z]
        if len(other_series) == 10:
            return len(other_series)
        else:
            return sum_series(x,y)
