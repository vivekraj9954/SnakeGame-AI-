import numpy as np
""""
a = np.array([32.49, -39.96,-3.86])
b = np.array([31.39, -39.28, -4.66])
c = np.array([31.14, -38.09,-4.49])

ba = a - b
bc = c - b

cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
"""

a = np.array([4, 2])
b = np.array([4, 4])

def angleCal(x , y):

    cosine_angle = np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
    a = np.arccos(cosine_angle)
    angle = np.degrees(a)
    angle = int(round(angle))

    move = 0

    if (angle == 90):
        move = 0  # move straight

    if (angle > 91 and angle < 270):
        move = -1  # move left

    if (angle > 270 and angle <= 361 or angle >= 0 and angle < 90):
        move = 1  # move right

    return(move)

print(angleCal(a ,b))