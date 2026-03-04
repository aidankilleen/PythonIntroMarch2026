# matplotlib_investigation.py

import numpy as np

x_values = range(1, 5)
y_values = np.random.randint(1, 20, 5)

# no dependency graph
for y in y_values:
    print ("*" * y)


for i in range(len(x_values)):
    print (f"{x_values[i]:5}", "*" * y_values[i])

# slightly more pythonic way
# use enumerate function

for i, v in enumerate(y_values):

    print (f"{i}", "*" * v)


