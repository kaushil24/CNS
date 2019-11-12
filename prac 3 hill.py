import numpy as np
pt = input().replace(" ", "")
pt = pt+"x"*(3 - len(pt)%3)
ptM = []
for i in range(0,len(pt),3):
  ptM.append(pt[i:i+3])

KEY = input()
key = [ord(i) for i in KEY]
key = np.array(key).reshape(3,3)

mtx = np.zeros((len(ptM), 3), dtype=int)

for i, txt in enumerate(ptM):
  mtx[i][0], mtx[i][1], mtx[i][2] = [ord(a) for a in txt]
  
key, mtx = key-97, mtx-97
op = []
for i in mtx:
  op.append(list((np.matmul(key, i)%26)+97))

ct = ''
for i in op:
  ct = ct+''.join([chr(j) for j in i])

ct