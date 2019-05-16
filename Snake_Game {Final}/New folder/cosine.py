from numpy import *
import numpy as np
from numpy.linalg import norm

a = np.array([100, 200])
b = np.array([60, 20])
c = np.array([40, 20])

x = b-a
y = b-c

cosine_angle = np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

a = np.arccos(cosine_angle)
angle = np.degrees(a)

print(angle)