from numpy import *
from numpy.linalg import norm

a = array([100, 200])
b = array([60, 20])
c = array([40, 20])

f = b-a
e = b-c

print (f)

abVec = norm(f)
bcVec = norm(e)

print (abVec)

abNorm = f / abVec
bcNorm = e / bcVec

res = abNorm[0] * bcNorm[0] + abNorm[1] * bcNorm[1]
print(res)
angle = arccos(res)*180.0/ pi

print(angle)