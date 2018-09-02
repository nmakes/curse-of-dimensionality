import matplotlib.pyplot as plt
from math import pi, gamma

def vs(d, r=1):
	return (pi**(d/2))*(r**d) / (gamma(d/2 + 1))

def vc(d, r=2):
	return r**d

a = [vs(d) / vc(d) for d in range(1, 100)]

plt.plot(a)
plt.xlabel('number of dimensions')
plt.ylabel('ratio of volume of hypersphere to hypercube')
plt.show()
