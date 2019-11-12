import numpy as np
pt = [ord(i)-97 for i in input()]
key = [ord(i)-97 for i in input()]

if len(key)<len(pt):
  dif = len(pt)-len(key)
  [key.append(0) for i in range(dif)]
elif len(pt)<len(key):
  dif = len(key)-len(pt)
  [pt.append(0) for i in range(dif)]

ct = [pt[i]+key[i] for i in range(len(pt))]
for i in range(len(ct)):
  if ct[i]>26:
    ct[i]-=26
  
  ct[i]+=97

ct = ''.join([chr(i) for i in ct])

ct