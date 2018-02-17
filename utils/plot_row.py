import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import glob
from subprocess import *
import matplotlib as mpl
from matplotlib import cm
#from statistics import mean

mpl.rcParams['font.size'] = 18


# * * * * * * * * * * * * * * * * * * * * * * * *	 extract_	 * * * * * * * * * * * * * * * * * * * * * * * * * *  

def read_():

  f = open(sys.argv[1], "r")

  while True:

    line = f.readline()
    if not line: break
    words = line.split()
    write.append(float(words[2]))
    read.append(float(words[3]))
    open_.append(float(words[7]))

# * * * * * * * * * * * * * * * * * * * * * * * *	 plot_	 * * * * * * * * * * * * * * * * * * * * * * * * * *  


def plot_():

 fig = plt.figure() #figsize=(20,15))
 #plt.title ("Write time ordered by start time")

 ax = fig.add_subplot(111)
 p1 = ax.plot (idx, open_, 'go-', idx, write, 'bx-', idx, read, 'ms-', lw=1, markersize=2)
 plt.legend (('Open', 'Write', 'Read'), loc='lower right')

 #for t in leg.get_texts():
#	plt.setp(t, 'size', 30)
 
 ax.set_xlabel('Iteration#')
 ax.set_ylabel('Time (seconds)')

 #ax.set_xscale('log')
 ax.set_yscale('log')

 #ax.set_ylim([0.1,700])
 plt.ylim(ymin=0.1)

 #ax.set_xticks(idx) #, rotation=30)
 #ax.set_xticklabels(ostids, rotation=30)

 fname = 'rowtimes.png'
 cmd = 'rm ' + fname
 #Popen(cmd, shell=True, stdout=PIPE).communicate()[0]
 #plt.savefig(fname)
 #plt.close()

 plt.show()

# * * * * * * * * * * * * * * * * * * * * * * * *	 startup_	 * * * * * * * * * * * * * * * * * * * * * * * * * *  

def startup_():

  global ostids, idx, write, read, open_
  ostids, idx, write, read, open_ = [], [], [], [], []

  read_()
  idx = range(1, len(read)+1)
  plot_()

startup_()

