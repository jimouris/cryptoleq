#!/usr/bin/python

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import sys
import string


benchmark = "all"

mydpi = 300
figname = benchmark+'.png'
pltsize = (12.4, 1.96) # default (8, 6)
# pltsize = (8 , 4) # default (8, 6)
nbits = ["N-Queens", "Jenkins", "PSI", "Dedup.", "Permutations", "Primes", "Matrix Mult.", "PIR", "Factorial", "Fibonacci"]

# beta 16
data = {
    'all':    { '512' : [44812.925, 6668.12, 2479.54, 4627.48, 3.7, 1397.44, 700.67, 164.62, 150.30, 152.18],  '1024' : [132622.735, 18316.79, 7133.17, 13759.32, 12.16, 4388.98, 2267.09, 488.94, 443.03, 453.88] },
    'allopn': { '512' : [96.81, 31.81, 3.04, 2.76, 3.7, 3.53, 13.56, 2.61, 2.93, 2.25] , '1024' : [132.74, 47.45, 7.98, 7.12, 12.16, 7.81, 22.83, 7.62, 8.91, 7.42] }
}


for key, value in data[benchmark].items():
    for i in range(len(value)):
        value[i] /= 100
    data[benchmark][key] = value

for key, value in data[benchmark+"opn"].items():
    for i in range(len(value)):
        value[i] /= 100
    data[benchmark+"opn"][key] = value

all512 = data[benchmark]['512']
all1024 = data[benchmark]['1024']
all512opn = data[benchmark+"opn"]['512']
all1024opn = data[benchmark+"opn"]['1024']

N = len(all512)
index = np.arange(N)  # the x locations for the groups
width = 0.42       # the width of the bars

fig, ax = plt.subplots(figsize=pltsize)
ax.margins(0.04, 0.04) 
rects1 = ax.bar(index, all512, width, color='xkcd:light pink', hatch='xxx', edgecolor='black', linewidth=1)
rects2 = ax.bar(index + width, all1024, width, color='xkcd:very light blue', hatch='...', edgecolor='black', linewidth=1)

rects1opn = ax.bar(index, all512opn, width, color='xkcd:light pink', edgecolor='black', linewidth=1)
rects2opn = ax.bar(index + width, all1024opn, width, color='xkcd:very light blue', edgecolor='black', linewidth=1)

ax.set_yscale('log')
ax.set_ylim([0.01, 10000])
ax.set_ylabel("time (sec.) x $10^2$")
# ax.set_xlabel("Security Parameter ($\lambda$) bits")
ax.set_xticks(index + width / 2)
ax.set_xticklabels(nbits)
ax.legend((rects1[0], rects2[0]), ("512 $\lambda$ bits", "1024 $\lambda$ bits"), fontsize=9, ncol=2, loc='upper right')


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height > 1000:
            ax.text(rect.get_x() + rect.get_width()/2.2, 1.1*height, '%2.1f' % (height), ha='center', va='bottom', fontsize=8.5)
        elif height > 100:
            ax.text(rect.get_x() + rect.get_width()/2.2, 1.1*height, '%2.2f' % (height), ha='center', va='bottom', fontsize=8.5)
        else:
            ax.text(rect.get_x() + rect.get_width()/2.3, 1.1*height, '%2.3f' % (height), ha='center', va='bottom', fontsize=8.5)

autolabel(rects1)
autolabel(rects2)

# fig.autofmt_xdate()

# plt.show()

plt.tight_layout()
plt.savefig("./charts/"+figname,dpi=mydpi, bbox_inches="tight", pad_inches=0.03)


# data = {
#     'nqueens':    { '512' : 44812.925,  '1024' : 132622.735 },
#     'nqueensopn': { '512' : 96.81 , '1024' : 132.74 },
#     'jenkins':    { '512' : 6668.12, '1024' : 18316.79 },
#     'jenkinsopn': { '512' : 31.81, '1024' : 47.45 },
#     'psi' :  { '512' : 2479.54,  '1024' : 7133.17 },
#     'psiopn' :  { '512' : 3.04,  '1024' : 7.98 },
#     'dedup' :  { '512' : 4627.48,  '1024' : 13759.32 },
#     'dedupopn' :  { '512' : 2.76,  '1024' : 7.12 },
#     'perm' :  { '512' : 3.7,  '1024' : 12.16 },
#     'permopn' :  { '512' : 3.7,  '1024' : 12.16 },
#     'sieve' :  { '512' : 1397.44,  '1024' : 4388.98 },
#     'sieveopn' :  { '512' : 3.53,  '1024' : 7.81 },
#     'mmult' :  { '512' : 700.67,  '1024' : 2267.09 },
#     'mmultopn' :  { '512' : 13.56,  '1024' : 22.83 },
#     'pir' :  { '512' : [90.23, 164.62, 333.57],  '1024' : [250.91, 488.94, 927.02] },
#     'piropn' :  { '512' : [2.37, 2.61, 2.66],  '1024' : [6.89, 7.62, 7.39] },
#     'fact':    { '512' : 150.30, '1024' : 443.03 },
#     'factopn': { '512' : 2.93, '1024' : 8.91 },
#     'fib':    { '512' : 152.18, '1024' : 453.88 },
#     'fibopn': { '512' : 2.25, '1024' : 7.42 }
# }
