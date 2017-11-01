#!/usr/bin/python

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import sys
import string


benchmark = "jenkins"

mydpi = 300
figname = benchmark+'.png'
pltsize = (5.5, 2) # default (8, 6)
nbits = [64, 128, 256, 512, 1024]

data = {
    'jenkins':    { 'jenkins' : [892.69, 987.97, 2689.28, 6668.12, 18316.79] },
    'jenkinsopn': { 'jenkins' : [18.97, 22.45, 25.21, 31.81, 47.45] }
}

for key, value in data[benchmark].items():
    for i in range(len(value)):
        value[i] /= 1000
    data[benchmark][key] = value

for key, value in data[benchmark+"opn"].items():
    for i in range(len(value)):
        value[i] /= 1000
    data[benchmark+"opn"][key] = value

jenkins = data[benchmark]['jenkins']
jenkinsopn = data[benchmark+"opn"]['jenkins']

N = len(jenkins)
index = np.arange(N)  # the x locations for the groups
width = 0.6       # the width of the bars

fig, ax = plt.subplots(figsize=pltsize)
ax.margins(0.04, 0.04) 
rects1 = ax.bar(index+width/2, jenkins, width, color='xkcd:light pink', hatch='xxx', edgecolor='black', linewidth=1)
rects1opn = ax.bar(index+width/2, jenkinsopn, width, color='xkcd:light pink', edgecolor='black', linewidth=1)


ax.set_yscale('log')
ax.set_ylim([0.001, 100])
ax.set_ylabel("time (sec.) x $10^3$")
ax.set_xlabel("Security Parameter ($\lambda$) bits")
ax.set_xticks(index + width / 2)
ax.set_xticklabels(nbits)
# ax.legend((rects1[0], rects2[0]), ("jenkins Cipher", "Simon Cipher"), fontsize=9, ncol=2, loc='upper left')


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height > 10:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.2f' % (height), ha='center', va='bottom', fontsize=8.5)
        else:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.3f' % (height), ha='center', va='bottom', fontsize=8.5)

autolabel(rects1)
# autolabel(rects2)

# plt.show()

plt.tight_layout()
plt.savefig("./charts/"+figname,dpi=mydpi, bbox_inches="tight", pad_inches=0.03)

