import matplotlib.pyplot as plt
import numpy as np

i1 = float(input("Enter i component of vector 1: "))
j1 = float(input("Enter j component of vector 1: "))
k1 = float(input("Enter k component of vector 1: "))
i2 = float(input("Enter i component of vector 2: "))
j2 = float(input("Enter j component of vector 2: "))
k2 = float(input("Enter k component of vector 2: "))

origin = [0,0,0]
v1 = [i1, j1, k1]
v2 = [i2, j2, k2]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
if k1 != 0 and k2 != 0:
    ax = plt.axes(projection = '3d')


v1dotv2 = np.vdot(v1,v2)
v1xv2 = np.cross(v1,v2)
v2xv1 = np.cross(v2,v1)
magv1 = np.linalg.norm(v1)
magv2 = np.linalg.norm(v2)

print(f"\nv1 = {v1[0]}i + " + f"{v1[1]}j + " + f"{v1[2]}k, " + f"Magnitude = {magv1}")
print(f"v2 = {v2[0]}i + " + f"{v2[1]}j + " + f"{v2[2]}k, " + f"Magnitude = {magv2}")

print(f'\nv1.v2 = {v1dotv2}')
print(f'v1xv2 = {v1xv2} or ' + f"{v1xv2[0]}i + " + f"{v1xv2[1]}j + " + f"{v1xv2[2]}k")
print(f'v2xv1 = {v2xv1} or ' + f"{v2xv1[0]}i + " + f"{v2xv1[1]}j + " + f"{v2xv1[2]}k")

ax.plot([origin[0], v1[0]],[origin[1],v1[1]], [origin[0], v1[2]], color = 'green', label = 'Vector 1')
ax.plot([origin[0], v2[0]],[origin[1],v2[1]], [origin[0], v2[2]], color = 'orange', label = 'Vector 2')
ax.plot([origin[0], v1[0] + v2[0]],[origin[0], v1[1] + v2[1]], [origin[0], v1[2] + v2[2]], label = "Sum")
ax.plot([v2[0], v1[0] + v2[0]], [v2[1], v1[1] + v2[1]],[v2[2], v1[2] + v2[2]], '--', color = 'green', label = 'Shifted Vector 2')
ax.plot([v1[0], v1[0] + v2[0]], [v1[1], v1[1] + v2[1]], [v1[2], v1[2] + v2[2]],'--', color = 'orange', label = 'Shifted Vector 1')
ax.plot([origin[0], v1xv2[0]], [origin[0], v1xv2[1]],[origin[0], v1xv2[2]], '--', color = 'grey', label = "v1 x v2 Cross Product")

plt.grid()
plt.legend(loc = 'lower right')
plt.title("Visualisation of Any Two 3D or 2D Vectors ")
plt.show()

