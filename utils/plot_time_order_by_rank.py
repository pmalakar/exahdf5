import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import glob
from subprocess import *
import matplotlib as mpl
from matplotlib import cm
#from statistics import mean

mpl.rcParams['font.size'] = 24

# * * * * * * * * * * * * * * * * * * * * * * * *	 extract_	 * * * * * * * * * * * * * * * * * * * * * * * * * *  

def read_():

  f = open(sys.argv[1], "r")

  while True:

    line = f.readline()
    if not line: break
    words = line.split()
    ranks.append(int(words[0]))
    #index.append()  #float(words[1]))
    start.append(float(words[3]))
    write.append(float(words[4]))

  #print ranks, start, write

# * * * * * * * * * * * * * * * * * * * * * * * *	 plot_  * * * * * * * * * * * * * * * * * * * * * * * * * *  


def plot_():

 fig = plt.figure(figsize=(15,12))
 #plt.title ("Write time ordered by start time")

 ax = fig.add_subplot(111)
 #p1 = ax.plot (start, write, 'go-') 
 index = np.arange(0, len(write))
 p1 = ax.plot (index, write, 'go-') 
 #plt.legend (('Write'), loc='upper right')

 #for t in leg.get_texts():
#	plt.setp(t, 'size', 30)
 
 ax.set_xlabel('Index (rank)')
 ax.set_ylabel('Time per write')

 #ax.set_xscale('log')
 ax.set_yscale('log')

 #ax.set_ylim([0,10])
 #plt.ylim(ymin=0)

 #ax.set_xticks(idx) #, rotation=30)
 #ax.set_xticklabels(start, rotation=30)

 fname = sys.argv[1]+'_order_by_rank.png'
 cmd = 'rm ' + fname
 Popen(cmd, shell=True, stdout=PIPE).communicate()[0]
 plt.savefig(fname)
 plt.close()

 #plt.show()

# * * * * * * * * * * * * * * * * * * * * * * * *	 startup_	 * * * * * * * * * * * * * * * * * * * * * * * * * *  

def startup_():

  global ranks, index, start, write, read
  ranks, index, start, write, read = [], [], [], [], []

  read_()
  idx = range(1, len(ranks)+1)
  plot_()

startup_()

