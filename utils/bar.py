#!/usr/bin/env python
import numpy as np
import sys
from subprocess import *
import matplotlib.mlab as mlab
import matplotlib as mpl
import matplotlib.pyplot as plt

size = 30
mpl.rcParams['font.size'] = size
mpl.rcParams['xtick.labelsize'] = size
mpl.rcParams['ytick.labelsize'] = size

h_0 = []

f = open(sys.argv[1], "r")
while True:
 line = f.readline()
 if not line: break
 words = line.split()
 h_0.append(float(words[5]))

fig = plt.figure(figsize=(20,15))
title = '64 Theta nodes (2048 ranks)' 
plt.title (title)
ax = fig.add_subplot(111)

ind = np.arange(len(h_0))
width = 0.5
p1 = ax.bar(ind, h_0, width, color='g')

#n, bins, patches = plt.hist(h_0, int(sys.argv[2]), normed=1, facecolor='g', alpha=0.75)
#print bins

plt.xlabel('Writes')
plt.ylabel('Time (seconds)')
plt.grid(True)

fname = sys.argv[1]+'_bar.png'
cmd = 'rm ' + fname
Popen(cmd, shell=True, stdout=PIPE).communicate()[0]
plt.savefig(fname)
plt.close()

#plt.show()
