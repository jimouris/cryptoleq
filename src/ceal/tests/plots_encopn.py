#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import string

if len(sys.argv) != 2:
    print "Usage:\t python " + sys.argv[0] + " [tak|isort|psi|sieve|dedup|pir|mmult]"
    sys.exit(1)
if sys.argv[1] == "tak" or sys.argv[1] == "isort" or sys.argv[1] == "psi" or sys.argv[1] == "sieve" or sys.argv[1] == "dedup" or sys.argv[1] == "pir" or sys.argv[1] == "mmult":
    benchmark = sys.argv[1]
else:
    print "Usage:\t python " + sys.argv[0] + " [tak|isort|psi|sieve|dedup|pir|mmult]"
    sys.exit(1)

mydpi = 300
figname = benchmark+'.png'

if benchmark == "sieve" or benchmark == "dedup" or benchmark == "pir" or benchmark == "mmult":
    pltsize = (7.5, 2.2) 
else:
    pltsize = (6.8, 2.1) 

nbits = ['64-bit $\lambda$', '128-bit $\lambda$', '256-bit $\lambda$', '512-bit $\lambda$', '1024-bit $\lambda$']


data = {
    'tak' : { '64' : [347.26, 2838.32, 19559.22], '128' : [631.3, 5143.88, 36096.32], '256' : [1451.3, 11863.95, 83044.28], '512' : [3695.09, 30228.41, 205365.2],  '1024' : [11762.58, 98300.55, 500300.55] },
    'takopn' : { '64' : [3.67, 28.11, 202.78], '128' : [4.53, 31.74, 227.72], '256' : [5.58, 36.32, 251.9], '512' : [7.44, 42.67, 297.36],  '1024' : [14.61, 65.0, 424.36] },
    
    'isort' :  { '64' : [152.93, 615.65, 2511.54], '128' : [349.79, 1420.64, 5707.16], '256' : [757.48, 3084.15, 12375.45], '512' : [2171.9, 8734.65, 35494.2],  '1024' : [6777.22, 27367.96, 108343.76] },
    'isortopn' :  { '64' : [0.3, 0.48, 1.35], '128' : [0.55, 0.8, 1.78], '256' : [1.03, 1.37, 2.17], '512' : [2.66, 2.86, 4.03],  '1024' : [8.08, 8.87, 9.71] },
    
    'psi' :  { '64' : [249.25, 968.8, 3845.82], '128' : [379.71, 1462.32, 5786.62], '256' : [828.24, 3127.55, 12225.06], '512' : [2479.54, 9191.15, 36009.76],  '1024' : [7133.17, 27015.24, 108343.76] },
    'psiopn' :  { '64' : [0.58, 0.81, 1.98], '128' : [0.91, 1.12, 2.31], '256' : [1.51, 1.66, 2.98], '512' : [3.04, 3.1, 5.21],  '1024' : [7.98, 9.23, 12.68] },

    'sieve' :  { '64' : [80.57, 157.46, 317.46], '128' : [190.43, 366.87, 729.19], '256' : [433.87, 816.97, 1598.71], '512' : [1397.44, 2468.49, 4618.86],  '1024' : [4388.98, 7789.04, 14060.56] },
    'sieveopn' :  { '64' : [0.66, 1.25, 2.86], '128' : [1.02, 1.68, 3.53], '256' : [1.36, 2.13, 4.13], '512' : [3.53, 4.39, 6.76],  '1024' : [7.81, 8.99, 12.31] },

    'dedup' :  { '64' : [74.5, 313.2, 1270.59], '128' : [218.7, 909.08, 3717.63], '256' : [370.32, 1569.9, 6255.3], '512' : [1125.22, 4627.48, 18712.79],  '1024' : [3414.63, 13759.32, 56539.16] },
    'dedupopn' :  { '64' : [0.21, 0.26, 0.31], '128' : [0.41, 0.49, 0.63], '256' : [0.98, 1.13, 0.94], '512' : [2.67, 2.76, 2.54],  '1024' : [7.01, 7.12, 7.41] },

    'pir' :  { '64' : [5.32, 10.15, 20.12], '128' : [15.65, 29.69, 57.75], '256' : [30.22, 53.72, 101.16], '512' : [90.23, 164.62, 333.57],  '1024' : [250.91, 488.94, 927.02] },
    'piropn' :  { '64' : [0.21, 0.17, 0.23], '128' : [0.43, 0.38, 0.39], '256' : [0.89, 0.87, 0.94], '512' : [2.37, 2.61, 2.66],  '1024' : [6.89, 7.62, 7.39] },

    'mmult' :  { '64' : [45.22, 125.24, 216.41], '128' : [106.13, 322.82, 568.54], '256' : [255.38, 642.45, 1540.36], '512' : [700.67, 2962.81, 5138.3],  '1024' : [2267.09, 11030.12, 19218.85] },
    'mmultopn' :  { '64' : [7.86, 18.02, 33.12], '128' : [9.05, 20.22, 37.44], '256' : [10.44, 23.42, 42.02], '512' : [13.56, 29.52, 53.23],  '1024' : [22.83, 46.41, 77.25] }
}

for key, value in data[benchmark].items():
    for i in range(len(value)):
        if benchmark == "tak" or benchmark == "isort" or benchmark == "psi":
            value[i] /= 10000
        elif benchmark == "sieve" or benchmark == "dedup" or benchmark == "mmult":
            value[i] /= 1000
        elif benchmark == "pir":
            value[i] /= 100
    data[benchmark][key] = value
for key, value in data[benchmark+"opn"].items():
    for i in range(len(value)):
        if benchmark == "tak" or benchmark == "isort" or benchmark == "psi":
            value[i] /= 10000
        elif benchmark == "sieve" or benchmark == "dedup" or benchmark == "mmult":
            value[i] /= 1000
        elif benchmark == "pir":
            value[i] /= 100
    data[benchmark+"opn"][key] = value

x_axis_labels = {
    'tak' : ("Inputs ($x, y, z$) range", ['[0-3]', '[0-4]', '[0-5]']),
    'isort' : ("Number of Array Elements ($N$)", [32, 64, 128]),
    'psi' : ("Number of Elements in each Set ($N \cap N$)", ["$16 \cap 16$", "$32 \cap 32$", "$64 \cap 64$"]),
    'sieve' : ("Maximum number to compute", [256, 512, 1024]),
    'dedup' : ("Number of Array Elements", [16, 32, 64]),
    'pir' : ("Number of Key-Value pairs", [16, 32, 64]),
    'mmult' : ("Matrices Size", ['$[8 \\times 8] \\times [8 \\times 8]$', '$[12 \\times 8] \\times [8 \\times 12]$', '$[16 \\times 8] \\times [8 \\times 16]$'])
}

data64 = data[benchmark]['64']
data128 = data[benchmark]['128']
data256 = data[benchmark]['256']
data512 = data[benchmark]['512']
data1024 = data[benchmark]['1024']

data64opn = data[benchmark+"opn"]['64']
data128opn = data[benchmark+"opn"]['128']
data256opn = data[benchmark+"opn"]['256']
data512opn = data[benchmark+"opn"]['512']
data1024opn = data[benchmark+"opn"]['1024']

N = len(data64)
index = np.arange(N)  # the x locations for the groups
width = 0.185       # the width of the bars

fig, ax = plt.subplots(figsize=pltsize)

ax.margins(0.03, 0.03)

rects1 = ax.bar(index - 2*width, data64, width, color='xkcd:light pink', hatch='xxx', edgecolor='black', linewidth=1)
rects2 = ax.bar(index - width, data128, width, color='xkcd:very light blue', hatch='...', edgecolor='black', linewidth=1)
rects3 = ax.bar(index, data256, width, color='xkcd:very light green', hatch='////', edgecolor='black', linewidth=1)
rects4 = ax.bar(index + width, data512, width, color='xkcd:ecru', hatch='---', edgecolor='black', linewidth=1)
rects5 = ax.bar(index + 2*width, data1024, width, color='xkcd:light peach', hatch='\\\\\\\\', edgecolor='black', linewidth=1)

rects1opn = ax.bar(index - 2*width, data64opn, width, color='xkcd:light pink', edgecolor='black', linewidth=1,)
rects2opn = ax.bar(index - width, data128opn, width, color='xkcd:very light blue', edgecolor='black', linewidth=1)
rects3opn = ax.bar(index, data256opn, width, color='xkcd:very light green', edgecolor='black', linewidth=1)
rects4opn = ax.bar(index + width, data512opn, width, color='xkcd:ecru', edgecolor='black', linewidth=1)
rects5opn = ax.bar(index + 2*width, data1024opn, width, color='xkcd:light peach', edgecolor='black', linewidth=1)

# rects1opn = ax.bar(index - 2*width, data64opn, width, bottom=data64, color='xkcd:light pink', edgecolor='black', linewidth=1,)
# rects2opn = ax.bar(index - width, data128opn, width, bottom=data128, color='xkcd:very light blue', edgecolor='black', linewidth=1)
# rects3opn = ax.bar(index, data256opn, width, bottom=data256, color='xkcd:very light green', edgecolor='black', linewidth=1)
# rects4opn = ax.bar(index + width, data512opn, width, bottom=data512, color='xkcd:ecru', edgecolor='black', linewidth=1)
# rects5opn = ax.bar(index + 2*width, data1024opn, width, bottom=data1024, color='xkcd:light peach', edgecolor='black', linewidth=1)


ax.set_yscale('log')
if benchmark == "tak":
    ax.set_ylim([0.0001, 100000])
    ax.set_ylabel("time (sec.) x $10^4$")
elif benchmark == "isort":
    ax.set_ylim([0.00001, 10000])
    ax.set_ylabel("time (sec.) x $10^4$")
elif benchmark == "psi":
    ax.set_ylim([0.00001, 10000])
    ax.set_ylabel("time (sec.) x $10^4$")
elif benchmark == "sieve":
    ax.set_ylim([0.0001, 10000])
    ax.set_ylabel("time (sec.) x $10^3$")
elif benchmark == "dedup":
    ax.set_ylim([0.0001, 10000])
    ax.set_ylabel("time (sec.) x $10^3$")
elif benchmark == "pir":
    ax.set_ylim([0.001, 1000])
    ax.set_ylabel("time (sec.) x $10^2$")
elif benchmark == "mmult":
    ax.set_ylim([0.001, 1000])
    ax.set_ylabel("time (sec.) x $10^3$")
ax.set_xticks(index)
ax.set_xlabel(x_axis_labels[benchmark][0])
ax.set_xticklabels(x_axis_labels[benchmark][1])
ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), nbits, fontsize=9, ncol=5, loc='upper center')

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height > 10:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.1f' % (height), ha='center', va='bottom', fontsize=9)
        else:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.2f' % (height), ha='center', va='bottom', fontsize=9)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)

# plt.show()

plt.tight_layout()
plt.savefig("./charts/"+figname,dpi=mydpi, bbox_inches="tight", pad_inches=0.03)
