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
    else:
        return lucas(x - 1) + lucas(x - 2)

def sum_series(n, x = 0, y = 1):
    if n < 0:
        return "nope"
    if x != 0 or x != 2 and y != 1:
        z = x + y
        other_series = []
        other_series.append(x)
        other_series.append(y)
        other_series.append(z)
        return other_series
        x = other_series[y]
        y = other_series[z]
        if len(other_series) == 10:
            return len(other_series)
        else:
            return sum_series(x,y)
    if n >= 0:
        return fibonacci(x)
    if x == 2 and y == 1:
        return lucas(x)
