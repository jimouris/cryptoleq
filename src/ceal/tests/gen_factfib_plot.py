#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import string

benchmark='factfib'

mydpi = 200
figname = benchmark+'.png'
# pltsize = (9, 3) # default (8, 6)
# pltsize = (6, 2.2) # default (8, 6)
pltsize = (6.7, 2.43) # default (8, 6)
nbits = [64, 128, 256, 512, 1024]


data = {
    'factorial' :   { 'beta16' : [10.04, 28.86333333, 58.64166667, 150.3016667, 443.0366667],   'beta24' : [21.285, 67.97166667, 128.1783333, 327.3716667, 931.0583333] },
    'fibonacci' :   { 'beta16' : [10.07, 29.11833333, 51.31166667, 152.185, 453.8833333],       'beta24' : [26.55333333, 84.7, 134.5683333, 408.7133333, 1192.681667]}
}

for key, value in data["factorial"].items():
    for i in range(len(value)):
        value[i] /= 100
    data["factorial"][key] = value
for key, value in data["fibonacci"].items():
    for i in range(len(value)):
        value[i] /= 100
    data["fibonacci"][key] = value


factbeta16 = data['factorial']['beta16']
factbeta24 = data['factorial']['beta24']
fibbeta16 = data['fibonacci']['beta16']
fibbeta24 = data['fibonacci']['beta24']

N = len(factbeta16)
index = np.arange(N)  # the x locations for the groups
width = 0.23       # the width of the bars

fig, ax = plt.subplots(figsize=pltsize)

rects1 = ax.bar(index - 1.5*width, factbeta16, width, color='xkcd:light pink', hatch='xxx', edgecolor='black', linewidth=1)
rects2 = ax.bar(index - 0.5*width, factbeta24, width, color='xkcd:very light blue', hatch='...', edgecolor='black', linewidth=1)
rects3 = ax.bar(index + 0.5*width, fibbeta16, width, color='xkcd:very light green', hatch='////', edgecolor='black', linewidth=1)
rects4 = ax.bar(index + 1.5*width, fibbeta24, width, color='xkcd:ecru', hatch='---', edgecolor='black', linewidth=1)

# add some text for labels, title and axes ticks
# ax.set_title(string.capwords("Factorial & Fibonacci"))

ax.margins(0.02, 0.02)  

ax.set_yscale('log')
ax.set_ylim([0.05, 40])
ax.set_ylabel("time (sec.) x $10^2$")
ax.set_xticks(index)
ax.set_xlabel("Security Parameter Size")
ax.set_xticklabels(nbits)
ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ("Factorial $\\beta$ = 16", "Factorial $\\beta$ = 24", "Fibonacci $\\beta$ = 16", "Fibonacci $\\beta$ = 24"), ncol=2, fontsize=9)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height > 10:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.1f' % (height), ha='center', va='bottom', fontsize=8)
        else:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.2f' % (height), ha='center', va='bottom', fontsize=8)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

# plt.show()

plt.tight_layout()
plt.savefig("./charts/"+figname,dpi=mydpi, bbox_inches="tight", pad_inches=0.03)

