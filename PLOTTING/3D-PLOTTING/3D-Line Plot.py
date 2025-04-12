import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')  # corrected 'add_subplots' to 'add_subplot'

t = np.linspace(0, 20, 500)
x = np.sin(t)
y = np.cos(t)
z = t

line, = ax.plot([], [], [], color='blue', lw=2)

ax.set_xlim([-1.2, 1.2])  
ax.set_ylim([-1.2, 1.2])   
ax.set_zlim([0, 20])       

ax.set_title("Animated 3-D Line Plot", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

def update(frame):  # added 'frame' parameter
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, interval=30, blit=True)

plt.tight_layout()
plt.show()
