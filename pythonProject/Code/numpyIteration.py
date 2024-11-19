import numpy as np
a = np.arange(12).reshape(4,3)
b = np.arange(4).reshape(4,1)
for row in a:
    print(row)
for row in a:
    for cell in row:
        print(cell)
print()
for cell in a.flatten():
    print(cell)
for x in np.nditer(a,order="C"):#print the value in c order
    print(x)
print()
for x in np.nditer(a,order="F"):#print the array values in Fortran
    print(x)
print()
for x,y in np.nditer([a,b]):#iterate through two arrays at once
    print(x,y)