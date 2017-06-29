#!/usr/bin/python

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import sys
import string

if len(sys.argv) != 2:
    print "Usage:\t python " + sys.argv[0] + " [nqueens|factorial|fibonacci]"
    sys.exit(1)
if sys.argv[1] == "nqueens" or sys.argv[1] == "factorial" or sys.argv[1] == "fibonacci":
    benchmark = sys.argv[1]
else:
    print "Usage:\t python " + sys.argv[0] + " [nqueens|factorial|fibonacci]"
    sys.exit(1)

mydpi = 300
figname = benchmark+'.png'
nbits = [64, 128, 256, 512, 1024]

data = {
    'nqueens' :     { 'beta16' : [910.39, 2059.405, 4439.46, 12514.24, 38192.405],              'beta24' : [3269.625, 7288.04, 15830.21, 44812.925, 132622.735]         },
    'factorial' :   { 'beta16' : [10.04, 28.86333333, 58.64166667, 150.3016667, 443.0366667],   'beta24' : [21.285, 67.97166667, 128.1783333, 327.3716667, 931.0583333] },
    'fibonacci' :   { 'beta16' : [10.07, 29.11833333, 51.31166667, 152.185, 453.8833333],       'beta24' : [26.55333333, 84.7, 134.5683333, 408.7133333, 1192.681667]   }
}

beta16 = data[benchmark]['beta16']
beta24 = data[benchmark]['beta24']


N = len(beta16)
index = np.arange(N)  # the x locations for the groups
width = 0.42       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(index, beta16, width, color='xkcd:light pink', hatch='xxxx', edgecolor='black', linewidth=1)
rects2 = ax.bar(index + width, beta24, width, color='xkcd:very light blue', hatch='....', edgecolor='black', linewidth=1)

# add some text for labels, title and axes ticks
# ax.set_title(string.capwords(benchmark))
ax.set_yscale('log')
ax.set_ylabel("time (sec.) x e4")
ax.set_xlabel("Security Parameter Size")
ax.set_xticks(index + width / 2)
ax.set_xticklabels(nbits)

ax.legend((rects1[0], rects2[0]), ("beta = 16", "beta = 24"), fontsize=9)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height/10000 > 10:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.1f' % (height/10000), ha='center', va='bottom', fontsize=8)
        else:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.2f' % (height/10000), ha='center', va='bottom', fontsize=8)
        # ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%d' % int(height), ha='center', va='bottom', fontsize=8)

autolabel(rects1)
autolabel(rects2)

plt.show()

# plt.tight_layout()
# plt.savefig("./charts/"+figname,dpi=mydpi, bbox_inches="tight", pad_inches=0)

