'''
    Written by Naveen Venkat
    Final Year Undergraduate Student, Dept. of CSIS
    Birla Institute of Technology and Science, Pilani
    www.naveenvenkat.com | nav.naveenvenkat@gmail.com
'''

import numpy as np
import matplotlib.pyplot as plt

def getRandomData(n, d):
    # n data points of d dimensions
    return np.random.rand(n,d)

def getSim(x1, x2):
    return np.dot(x1, x2)

def getLpNorm(v, p):
    return np.linalg.norm(v, ord=p)
