import matplotlib.pyplot as plt
import deeptime

ftraj = deeptime.data.position_based_fluids(n_burn_in=150).run(300)
f, axes = plt.subplots(3, 2, figsize=(15, 10))
for i, ax in enumerate(axes.flat):
    ax.scatter(*(ftraj[i*50].reshape(-1, 2).T))
    ax.set_title("t = {}".format(i*50))
    ax.grid()
f.suptitle(r'PBF dataset observations.')
plt.show()