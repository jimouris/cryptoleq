#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import string

benchmark='factfib'

mydpi = 300
figname = benchmark+'.png'
nbits = [64, 128, 256, 512, 1024]


data = {
    'tak' : { '64' : [347.26, 2838.32, 19559.22], '128' : [631.3, 5143.88, 36096.32], '256' : [1451.3, 11863.95, 83044.28], '512' : [3695.09, 30228.41, 205365.2],  '1024' : [11762.58, 98300.55, 500300.55] },

    'factorial' :   { 'data16' : [10.04, 28.86333333, 58.64166667, 150.3016667, 443.0366667],   'data24' : [21.285, 67.97166667, 128.1783333, 327.3716667, 931.0583333] },
    'fibonacci' :   { 'data16' : [10.07, 29.11833333, 51.31166667, 152.185, 453.8833333],       'data24' : [26.55333333, 84.7, 134.5683333, 408.7133333, 1192.681667]}
}

factdata16 = data['factorial']['data16']
factdata24 = data['factorial']['data24']
fibdata16 = data['fibonacci']['data16']
fibdata24 = data['fibonacci']['data24']

N = len(factdata16)
index = np.arange(N)  # the x locations for the groups
width = 0.22       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(index - 1.5*width, factdata16, width, color='steelblue')
rects2 = ax.bar(index - 0.5*width, factdata24, width, color='firebrick')
rects3 = ax.bar(index + 0.5*width, fibdata16, width, color='darkorange')
rects4 = ax.bar(index + 1.5*width, fibdata24, width, color='forestgreen')


# add some text for labels, title and axes ticks
ax.set_title(string.capwords("Factorial & Fibonacci"))
ax.set_yscale('log')
ax.set_ylabel("time (sec.)")
ax.set_xticks(index)
ax.set_xlabel("N bits")
ax.set_xticklabels(nbits)

ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ("Factorial beta = 16", "Factorial beta = 24", "Fibonacci beta = 16", "Fibonacci beta = 24"), fontsize=9)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%d' % int(height), ha='center', va='bottom', fontsize=8)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

plt.show()

# plt.tight_layout()
# plt.savefig("./charts/"+figname,dpi=mydpi)
