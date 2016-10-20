import numpy.random as ran

def waterbag(n, x, y, px, py):
    for i in range(n):
        x[i] = ran.uniform(-1,1)
        y[i] = ran.uniform(-1, 1)
        px[i] = ran.uniform(-1, 1)
        py[i] = ran.uniform(-1,1)
    return x, y, px, py
