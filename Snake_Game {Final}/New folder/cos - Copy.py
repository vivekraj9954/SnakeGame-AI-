import numpy as np
""""
a = np.array([32.49, -39.96,-3.86])
b = np.array([31.39, -39.28, -4.66])
c = np.array([31.14, -38.09,-4.49])

ba = a - b
bc = c - b

cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))


body = [[120, 60, 'RIGHT'], [80, 60, 'RIGHT'], [60, 60, 'RIGHT']]

print(body[0][0:2])"""

from numpy import *
import numpy as np
from numpy.linalg import norm

y = np.array([[2, 3], [5, 6]])
x = np.array([5, 6])

cosine_angle = np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

a = np.arccos(cosine_angle)
angle = np.degrees(a)

print(y[0][1:2])