import numpy as np
import deeptime as dt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

system = dt.data.abc_flow(n_steps=100)
scatters = [np.random.uniform(np.pi-.5, np.pi+.5, size=(200, 3))]
for _ in range(12):
    scatters.append(system(scatters[-1], n_jobs=8))

f = plt.figure(figsize=(18, 18))
f.suptitle('Evolution of test points in the ABC flowfield')
for i in range(4):
    for j in range(3):
        ix = j + i*3
        ax = f.add_subplot(4, 3, ix+1, projection='3d')
        ax.set_title(f"T={ix*system.n_steps*system.h:.2f}")
        ax.scatter(*scatters[ix].T, c=np.linspace(0, 1, num=200))
        ax.set_xlim([0, 2*np.pi])
        ax.set_ylim([0, 2*np.pi])
        ax.set_zlim([0, 2*np.pi])
plt.show()