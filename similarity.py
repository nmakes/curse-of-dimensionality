'''
    Written by Naveen Venkat
    Final Year Undergraduate Student, Dept. of CSIS
    Birla Institute of Technology and Science, Pilani
    www.naveenvenkat.com | nav.naveenvenkat@gmail.com
'''

import data
import numpy as np
from time import time
from tqdm import tqdm

def getSimComparison(n, d):

    DS = data.getRandomData(n, d)
    p1 = DS[0]

    sims = np.zeros((n-1,d))

    i = -1
    for p2 in DS[1:]:
        i+=1
        sims[i] = np.dot(p1, p2) / ( np.linalg.norm(p1) * np.linalg.norm(p2) )

    return (np.mean(sims), np.std(sims))

def runSimComparison(n, dlist):

    sims = []
    times = []
    for d in tqdm(dlist):
        t1 = time()
        sims.append( getSimComparison(n,d) )
        t2 = time()
        times.append(t2 - t1)

    simsMean = [m for m,s in sims]
    simsStd = [s for m,s in sims]

    # Display standard deviation results
    data.plt.figure('Standard deviation of cosine similarity')
    data.plt.xlabel('number of dimensions')
    data.plt.ylabel('standard deviation of similarity')
    data.plt.plot(dlist, simsStd)

    # Display running time results
    data.plt.figure('Running time for cosine similarity')
    data.plt.xlabel('number of dimensions')
    data.plt.ylabel('running time for cosine similarity (seconds)')
    data.plt.plot(times)

    data.plt.show()


if __name__=='__main__':

    runSimComparison(1000, range(10, 1001, 10))
