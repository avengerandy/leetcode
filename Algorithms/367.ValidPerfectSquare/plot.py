import numpy as np
import matplotlib.pyplot as plt

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

x = np.arange(0, 100, 1)
y = np.log2(x)
plt.plot(x, y, 'b', label='log2')

x = np.arange(0, 100, 1)
y = np.sqrt(x)
plt.plot(x, y, 'r', label='sqrt')

plt.legend(loc='upper right')
plt.show()
