#!/usr/bin/python

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import sys
import string


benchmark = "nqueens"

mydpi = 300
figname = benchmark+'.png'
pltsize = (6.2, 1.9) # default (8, 6)
nbits = [64, 128, 256, 512, 1024]

data = {
    'nqueens':    { 'beta8' : [910.39, 2059.405, 4439.46, 12514.24, 38192.405],  'beta16' : [3269.625, 7288.04, 15830.21, 44812.925, 132622.735] },
    'nqueensopn': { 'beta8' : [19.48, 21.87, 24.59, 31.48, 46.52],              'beta16' : [61.88, 69.37, 78.29, 96.81, 132.74] }
}

for key, value in data[benchmark].items():
    for i in range(len(value)):
        value[i] /= 10000
    data[benchmark][key] = value

for key, value in data[benchmark+"opn"].items():
    for i in range(len(value)):
        value[i] /= 10000
    data[benchmark+"opn"][key] = value

beta8 = data[benchmark]['beta8']
beta16 = data[benchmark]['beta16']
beta8opn = data[benchmark+"opn"]['beta8']
beta16opn = data[benchmark+"opn"]['beta16']

N = len(beta8)
index = np.arange(N)  # the x locations for the groups
width = 0.42       # the width of the bars

fig, ax = plt.subplots(figsize=pltsize)
ax.margins(0.04, 0.04) 
rects1 = ax.bar(index, beta8, width, color='xkcd:light pink', hatch='xxx', edgecolor='black', linewidth=1)
rects2 = ax.bar(index + width, beta16, width, color='xkcd:very light blue', hatch='...', edgecolor='black', linewidth=1)

rects1opn = ax.bar(index, beta8opn, width, color='xkcd:light pink', edgecolor='black', linewidth=1)
rects2opn = ax.bar(index + width, beta16opn, width, color='xkcd:very light blue', edgecolor='black', linewidth=1)

ax.set_yscale('log')
ax.set_ylim([0.0001, 1000])
ax.set_ylabel("time (sec.) x $10^4$")
ax.set_xlabel("Security Parameter ($\lambda$) bits")
ax.set_xticks(index + width / 2)
ax.set_xticklabels(nbits)
ax.legend((rects1[0], rects2[0]), ("$\\beta$ = 8", "$\\beta$ = 16"), fontsize=8, ncol=2, loc='upper left')


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height > 10:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.2f' % (height), ha='center', va='bottom', fontsize=8)
        else:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.3f' % (height), ha='center', va='bottom', fontsize=8)

autolabel(rects1)
autolabel(rects2)

# plt.show()

plt.tight_layout()
plt.savefig("./charts/"+figname,dpi=mydpi, bbox_inches="tight", pad_inches=0.03)

