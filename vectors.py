import matplotlib.pyplot as plt
import numpy

i1 = int(input("Enter i component of vector 1: "))
j1 = int(input("Enter j component of vector 1: "))

i2 = int(input("Enter i component of vector 2: "))
j2 = int(input("Enter j component of vector 2: "))

origin = [0,0,0]
v1 = [i1, j1]
v2 = [i2, j2]

print(v1)
print(v2)

plt.plot([origin[0], v1[0]],[origin[1],v1[1]], color = 'green', label = 'Vector 1')
plt.plot([origin[0], v2[0]],[origin[1],v2[1]], color = 'orange', label = 'Vector 2')
plt.plot([origin[0], v1[0] + v2[0]],[origin[0], v1[1] + v2[1]], label = "Sum")#head vector 2, head vector 1
plt.plot([v2[0], v1[0] + v2[0]], [v2[1], v1[1] + v2[1]], '--', color = 'green', label = 'Shifted vector 2')
plt.plot([v1[0], v1[0] + v2[0]], [v1[1], v1[1] + v2[1]], '--', color = 'orange', label = 'Shifted vector 1')
plt.grid()
plt.legend()
plt.show()

