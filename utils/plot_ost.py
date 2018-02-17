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
    ostids.append(int(words[0]))
    write.append(int(words[1]))
    read.append(int(words[2]))

  print ostids, write, read

# * * * * * * * * * * * * * * * * * * * * * * * *	 plot_	 * * * * * * * * * * * * * * * * * * * * * * * * * *  


def plot_():

 fig = plt.figure() #figsize=(20,15))
 #plt.title ("Write time ordered by start time")

 ax = fig.add_subplot(111)
 p1 = ax.plot (idx, write, 'go-', idx, read, 'bx-', lw=2)
 plt.legend (('Write', 'Read'), loc='upper right')

 #for t in leg.get_texts():
#	plt.setp(t, 'size', 30)
 
 ax.set_xlabel('OST id')
 ax.set_ylabel('Access count')

 #ax.set_xscale('log')
 #ax.set_yscale('log')

 #ax.set_ylim([0.1,700])
 plt.ylim(ymin=0)

 ax.set_xticks(idx) #, rotation=30)
 ax.set_xticklabels(ostids, rotation=30)

 fname = 'ostaccesscounts.png'
 cmd = 'rm ' + fname
 #Popen(cmd, shell=True, stdout=PIPE).communicate()[0]
 #plt.savefig(fname)
 #plt.close()

 plt.show()

# * * * * * * * * * * * * * * * * * * * * * * * *	 startup_	 * * * * * * * * * * * * * * * * * * * * * * * * * *  

def startup_():

  global ostids, idx, write, read
  ostids, idx, write, read = [], [], [], []

  read_()
  idx = range(1, len(ostids)+1)
  plot_()

startup_()

