# pt = input().replace(" ", "")
op = []
pt = "0123456789za"
def rf(pt):
  op = ''
  for i in range(3):
    inv = 3-i
    txt = []
    if i==2:
      txt = [pt[j] for j in range(i,len(pt)+1, 4)]
      op+=''.join(txt)
      print(txt)
    else:
      txt = [pt[j] for j in range(i, len(pt), 2*inv-2)]
      op+=''.join(txt)

  return op
x = rf(pt)