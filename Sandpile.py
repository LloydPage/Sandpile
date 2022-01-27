import matplotlib.pyplot as plt
import numpy as np
piles=int(input("Enter the number of piles: "))
leakage=float(input("Enter leakage amount: "))
directions=int(input("Enter the number of directions: "))
map=dict();
for i in range(piles):
  x=int(input("Enter x coordinate of pile "+str(i+1)+" : "))
  y=int(input("Enter y coordinate of pile "+str(i+1)+" : "))
  c=float(input("Enter starting amount of pile "+str(i+1)+" : "))
  map.update({(x,y):c})
#setup initialized
maxx=0
minx=0
maxy=0
miny=0
#computing the sandpile model
four=True
while four:
  four=False
  for key in list(map.keys()):
    if map.get(key)>=directions*leakage:
      four=True
      map.update({key:map.get(key)-(directions*leakage)})
      x=key[0]
      y=key[1]
      c=map.get((x+1,y))
      if c is None:
        map.update({(x+1,y):1})
        maxx=max(maxx,x+1)
      else:
         map.update({(x+1,y):map.get((x+1,y))+1})
      c=map.get((x,y+1))
      if c is None:
        map.update({(x,y+1):1})
        maxy=max(maxy,y+1)
      else:
         map.update({(x,y+1):map.get((x,y+1))+1})
      if directions==4:
        c=map.get((x-1,y))
        if c is None:
         map.update({(x-1,y):1})
         minx=min(minx,x-1)
        else:
          map.update({(x-1,y):map.get((x-1,y))+1})
        c=map.get((x,y-1))
        if c is None:
          map.update({(x,y-1):1})
          miny=min(miny,y-1)
        else:
          map.update({(x,y-1):map.get((x,y-1))+1})
#generate color map
array=np.zeros((maxx-minx+3,maxy-miny+3))
for i in range(minx-1,maxx+2):
  for j in range(miny-1,maxy+2):
    c=map.get((i,j))
    if c is not None:
      array[j-miny+1][i-minx+1]=c
heatmap=plt.pcolormesh(array)
plt.axis('off')
plt.pcolormesh(array)
plt.colorbar(heatmap)
plt.show()
