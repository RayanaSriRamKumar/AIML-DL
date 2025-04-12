import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig= plt.figure(figsize=(8,6))
ax= fig.add_subplot(111,projection= '3d')
_x= np.arange(4)
_y= np.arange(3)
_xx, _yy= np.meshgrid(_x, _y)
x, y= _xx.ravel(), _yy.ravel()
z= np.zeros_like(x)
dz= [3,5,1,6,4,2,5,3,2,4,7,6]
ax.bar3d(x,y,z,dx=0.5, dy=0.5, dz=dz, color= 'skyblue', edgecolor='black')
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("z-axis")
ax.set_title("3D bar plot")
plt.tight_layout()
plt.show()