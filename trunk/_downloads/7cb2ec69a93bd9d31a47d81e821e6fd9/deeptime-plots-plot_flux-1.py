import numpy as np
P = np.array([[0.8, 0.15, 0.05, 0.0, 0.0],
             [0.1, 0.75, 0.05, 0.05, 0.05],
             [0.05, 0.1, 0.8, 0.0, 0.05],
             [0.0, 0.2, 0.0, 0.8, 0.0],
             [0.0, 0.02, 0.02, 0.0, 0.96]])

from deeptime.markov.msm import MarkovStateModel
flux = MarkovStateModel(P).reactive_flux([2], [3])

from deeptime.plots import plot_flux
ax, pos = plot_flux(flux, flux_scale=100)
ax.set_aspect('equal')