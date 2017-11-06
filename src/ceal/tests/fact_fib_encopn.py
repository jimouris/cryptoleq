#!/usr/bin/python

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import sys
import string


benchmark = "fact"

if len(sys.argv) != 2:
    print "Usage:\t python " + sys.argv[0] + " [fact|fib]"
    sys.exit(1)
if sys.argv[1] == "fact" or sys.argv[1] == "fib":
    benchmark = sys.argv[1]
else:
    print "Usage:\t python " + sys.argv[0] + " [fact|fib]"
    sys.exit(1)

mydpi = 300
figname = benchmark+'.png'
pltsize = (6.2, 1.95) # default (8, 6)
nbits = [64, 128, 256, 512, 1024]

data = {
    'fact':    { 'beta16' : [10.04, 28.86, 58.64, 150.30, 443.03],  'beta24' : [21.28, 67.97, 128.17, 327.37, 931.05] },
    'factopn': { 'beta16' : [0.62, 0.91, 1.39, 2.93, 8.91],  'beta24' : [1.13, 1.47, 2.02, 3.69, 9.87] },

    'fib':    { 'beta16' : [10.07, 29.11, 51.31, 152.18, 453.88],  'beta24' : [26.55, 84.71, 134.56, 408.71, 1192.68] },
    'fibopn': { 'beta16' : [0.21, 0.45, 0.77, 2.25, 7.42],  'beta24' : [0.21, 0.47, 0.85, 2.25, 7.49] }
}

for key, value in data[benchmark].items():
    for i in range(len(value)):
        if benchmark == "fact":
            value[i] /= 100
        else:
            value[i] /= 1000
    data[benchmark][key] = value

for key, value in data[benchmark+"opn"].items():
    for i in range(len(value)):
        if benchmark == "fact":
            value[i] /= 100
        else:
            value[i] /= 1000
    data[benchmark+"opn"][key] = value

beta16 = data[benchmark]['beta16']
beta24 = data[benchmark]['beta24']
beta16opn = data[benchmark+"opn"]['beta16']
beta24opn = data[benchmark+"opn"]['beta24']

N = len(beta16)
index = np.arange(N)  # the x locations for the groups
width = 0.42       # the width of the bars

fig, ax = plt.subplots(figsize=pltsize)
ax.margins(0.04, 0.04) 
rects1 = ax.bar(index, beta16, width, color='xkcd:light pink', hatch='xxx', edgecolor='black', linewidth=1)
rects2 = ax.bar(index + width, beta24, width, color='xkcd:very light blue', hatch='...', edgecolor='black', linewidth=1)

rects1opn = ax.bar(index, beta16opn, width, color='xkcd:light pink', edgecolor='black', linewidth=1)
rects2opn = ax.bar(index + width, beta24opn, width, color='xkcd:very light blue', edgecolor='black', linewidth=1)

ax.set_yscale('log')
if benchmark == "fact":
    ax.set_ylim([0.001, 100])
    ax.set_ylabel("time (sec.) x $10^2$")
else:
    ax.set_ylim([0.0001, 10])
    ax.set_ylabel("time (sec.) x $10^3$")
ax.set_xlabel("Security Parameter ($\lambda$) bits")
ax.set_xticks(index + width / 2)
ax.set_xticklabels(nbits)
ax.legend((rects1[0], rects2[0]), ("$\\beta$ = 16", "$\\beta$ = 24"), fontsize=9, ncol=2, loc='upper left')


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height > 10:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.2f' % (height), ha='center', va='bottom', fontsize=8.5)
        else:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.3f' % (height), ha='center', va='bottom', fontsize=8.5)

autolabel(rects1)
autolabel(rects2)

# plt.show()

plt.tight_layout()
plt.savefig("./charts/"+figname,dpi=mydpi, bbox_inches="tight", pad_inches=0.03)

