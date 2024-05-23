def inteiros(a, b):
    y = 0
    if b < 10000 and a < b:  
        for x in range(a, b + 1):
            if x % 2 == 1:
                y += x
        return y
    else:
        return “valores errados”