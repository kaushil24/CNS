import numpy as np

KEY = "thegreatjuhi".replace(" ", "").replace("j", "i")
key = ''
for i in KEY:
  if i in key:
    continue
  key+=i

print(key)

ALPH = "abcdefghiklmnopqrstuvwxyz"
alph = set(list(ALPH)) -   set(key)
alph = ''.join(sorted(alph))
print(alph)

MTX = key+alph

mtx = np.array(list(MTX)).reshape(5,5)
mtx

pt = "datsonill"


div_pt = []
while len(pt)!=0:
  if len(pt)==1:
    nt = pt[-1]+'x'
    div_pt.append(nt)
    break
  nt = ''
  nt = pt[:2]
  pt = pt[2:]
  if nt[0]==nt[1]:
    pt = nt[1]+pt
    nt = nt[0]+'x'
    div_pt.append(nt)
  else:
    div_pt.append(nt)

ct = []
for pair in div_pt:
  r1, c1 = list(np.argwhere(mtx==pair[0])[0])
  r2, c2 = list(np.argwhere(mtx==pair[1])[0])

  if r1==r2:
    if c1==4:
      c1 = -1
    elif c2==4:
      c2 = -1

    newP = mtx[r1][c1+1] + mtx[r2][c2+1]
  
  elif c1==c2:
    if r1==4:
      r1 = -1
    elif r2 == 4:
      r2 = -1

    newP = mtx[r1+1][c1] + mtx[r2+1][c2]

  else:
    newP = mtx[r1][c2] + mtx[r2][c1]

  ct.append(newP)

ct