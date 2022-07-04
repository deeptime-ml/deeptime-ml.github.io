import numpy as np
P = np.array([[0.8, 0.15, 0.05, 0.0, 0.0],
              [0.1, 0.75, 0.05, 0.05, 0.05],
              [0.05, 0.1, 0.8, 0.0, 0.05],
              [0.0, 0.2, 0.0, 0.8, 0.0],
              [1e-7, 0.02 - 1e-7, 0.02, 0.0, 0.96]])

from deeptime.plots import plot_markov_model
ax, pos = plot_markov_model(P)
ax.set_aspect('equal')