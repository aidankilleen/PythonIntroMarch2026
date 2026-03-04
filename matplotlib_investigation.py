# matplotlib_investigation.py

from matplotlib import pyplot as plt
import numpy as np


x_values = range (1, 101)
y_values = np.random.randint(1, 100, 100)

plt.plot(x_values, y_values)

plt.show()