def maxi(x, y, z):
    if x >= y:
        if x >= z:
            return x
        else:
            return z
    else:
        if y >= z:
            return y
        else:
            return z


print(maxi(50, 15, 10))

