def f(x):
    return abs(x**2+10*x-1.5**x)
import numpy as np
x = np.linspace(-15, 15, num = 100)
y = f(x)
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()