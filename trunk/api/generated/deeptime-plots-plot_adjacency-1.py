import numpy as np
P = np.array([[0.8, 0.15, 0.05, 0.0],
              [0.1, 0.75, 0.05, 0.05],
              [0.05, 0.1, 0.8, 0.0],
              [0.0, 0.2, 0.0, 0.8]])

from deeptime.plots import plot_adjacency
ax = plot_adjacency(P, positions=np.array([[0, 0], [0, 1], [1, 0], [1, 1]]))
ax.set_aspect('equal')