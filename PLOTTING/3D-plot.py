import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig= plt.figure(figsize=(8,6))
ax=fig.add_subplot(111,projection='3d')
t=np.linspace(0,20,500)
x=np.sin(t)
y=np.cos(t)
z=t
ax.plot3D(x,y,z,color='purple', linewidth=2, linestyle='--', label='3D Curve')
ax.set_title(' 3D Line Plot ', fontsize=16, fontweight='bold')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Axis')
ax.legend()
plt.tight_layout()
plt.show()