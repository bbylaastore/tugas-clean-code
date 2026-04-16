def h(a, b, c):
    x = a - (a * b / 100)
    
    if c == "yes":
        x = x + 10000
    
    if x > 100000:
        x = 100000
    
    print("hasil akhir:", x)
    return x