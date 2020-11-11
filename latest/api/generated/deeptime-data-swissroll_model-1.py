import matplotlib.pyplot as plt
from matplotlib import animation
from deeptime.data import swissroll_model

n_samples = 15000
dtraj, traj = swissroll_model(n_samples)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*traj.T, marker='o', s=20, c=dtraj, alpha=0.6)