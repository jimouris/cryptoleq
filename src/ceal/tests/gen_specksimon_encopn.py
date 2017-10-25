#!/usr/bin/python

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import sys
import string


benchmark = "specksimon"

mydpi = 300
figname = benchmark+'.png'
pltsize = (6.2, 1.96) # default (8, 6)
nbits = [64, 128, 256, 512, 1024]

data = {
    'specksimon':    { 'speck' : [524.21, 1161.62, 2856.46, 7166.51, 20918.06], 'simon' : [1344.56, 3072.08, 7370.68, 18096.62, 53741.72] },
    'specksimonopn': { 'speck' : [36.15, 40.65, 45.81, 56.41, 81.38],           'simon' : [104.49, 112.06, 125.12, 150.01, 208.58] }
}

for key, value in data[benchmark].items():
    for i in range(len(value)):
        value[i] /= 1000
    data[benchmark][key] = value

for key, value in data[benchmark+"opn"].items():
    for i in range(len(value)):
        value[i] /= 1000
    data[benchmark+"opn"][key] = value

speck = data[benchmark]['speck']
simon = data[benchmark]['simon']
speckopn = data[benchmark+"opn"]['speck']
simonopn = data[benchmark+"opn"]['simon']

N = len(speck)
index = np.arange(N)  # the x locations for the groups
width = 0.42       # the width of the bars

fig, ax = plt.subplots(figsize=pltsize)
ax.margins(0.04, 0.04) 
rects1 = ax.bar(index, speck, width, color='xkcd:light pink', hatch='xxx', edgecolor='black', linewidth=1)
rects2 = ax.bar(index + width, simon, width, color='xkcd:very light blue', hatch='...', edgecolor='black', linewidth=1)

rects1opn = ax.bar(index, speckopn, width, color='xkcd:light pink', edgecolor='black', linewidth=1)
rects2opn = ax.bar(index + width, simonopn, width, color='xkcd:very light blue', edgecolor='black', linewidth=1)

ax.set_yscale('log')
ax.set_ylim([0.01, 1000])
ax.set_ylabel("time (sec.) x $10^3$")
ax.set_xlabel("Security Parameter ($\lambda$) bits")
ax.set_xticks(index + width / 2)
ax.set_xticklabels(nbits)
ax.legend((rects1[0], rects2[0]), ("Speck Cipher", "Simon Cipher"), fontsize=9, ncol=2, loc='upper left')


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

