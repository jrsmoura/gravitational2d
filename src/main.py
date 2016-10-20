#-*-coding:utf8-*-

import numpy as np
from Physics import initial as init

config = []

n = 50

x = np.zeros(n)
y = np.zeros(n)
px = np.zeros(n)
py = np.zeros(n)

config = init.waterbag(n, x, y, py, py)

