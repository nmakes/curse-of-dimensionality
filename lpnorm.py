'''
    Written by Naveen Venkat
    Final Year Undergraduate Student, Dept. of CSIS
    Birla Institute of Technology and Science, Pilani
    www.naveenvenkat.com | nav.naveenvenkat@gmail.com
'''

import data
from time import time
from tqdm import tqdm
import numpy as np

def runLpNormComparison(n, d, plist, plot=True):

    DS = data.getRandomData(n, d)

    dists = []
    times = []
    P1 = DS[0]
    rest = DS[1:]

    for p in tqdm(plist):
        t1 = time()
        dist = data.getLpNorm(rest - P1, p, axis=1)
        t2 = time()
        times.append(t2 - t1)
        dists.append( np.std(dist) )

    if(plot):
        # Display standard deviation results
        data.plt.figure('Standard deviation of distance')
        data.plt.xlabel('order of norm')
        data.plt.ylabel('standard deviation of distance')
        data.plt.plot(plist, dists)

        # Display running time results
        data.plt.figure('Running time for distance')
        data.plt.xlabel('order of norm')
        data.plt.ylabel('running time for distance calculation (seconds)')
        data.plt.plot(plist, times)

        data.plt.show()

    return (plist, dists, times)

if __name__=='__main__':

    plotList = []

    dims = [10, 20, 30, 40]
    plist = [i/10 for i in range(10, 101, 1)]
    plothandles = []

    for d in dims:
        plotList.append( runLpNormComparison(1000, d, plist, plot=False) )

    for i in range(len(plotList)):

        (plist, dists, times) = plotList[i]
        d = dims[i]

        # Display standard deviation results
        data.plt.figure('Standard deviation of distance')
        data.plt.xlabel('order of norm')
        data.plt.ylabel('standard deviation of distance')
        x, = data.plt.plot(plist, dists, label= str(d) + ' dimensions')
        plothandles.append(x)

    data.plt.legend(handles=plothandles)
    data.plt.show()
