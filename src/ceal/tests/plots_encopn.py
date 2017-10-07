#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import string

if len(sys.argv) != 2:
    print "Usage:\t python " + sys.argv[0] + " [tak|isort|psi]"
    sys.exit(1)
if sys.argv[1] == "tak" or sys.argv[1] == "isort" or sys.argv[1] == "psi":
    benchmark = sys.argv[1]
else:
    print "Usage:\t python " + sys.argv[0] + " [tak|isort|psi]"
    sys.exit(1)

mydpi = 300
figname = benchmark+'.png'

pltsize = (6.7, 2) 

nbits = ['64-bit $\lambda$', '128-bit $\lambda$', '256-bit $\lambda$', '512-bit $\lambda$', '1024-bit $\lambda$']


data = {
    'tak' : { '64' : [347.26, 2838.32, 19559.22], '128' : [631.3, 5143.88, 36096.32], '256' : [1451.3, 11863.95, 83044.28], '512' : [3695.09, 30228.41, 205365.2],  '1024' : [11762.58, 98300.55, 500300.55] },
    'takopn' : { '64' : [3.67, 28.11, 202.78], '128' : [4.53, 31.74, 227.72], '256' : [5.58, 36.32, 251.9], '512' : [7.44, 42.67, 297.36],  '1024' : [14.61, 65.0, 424.36] },
    
    'isort' :  { '64' : [152.93, 615.65, 2511.54], '128' : [349.79, 1420.64, 5707.16], '256' : [757.48, 3084.15, 12375.45], '512' : [2171.9, 8734.65, 35494.2],  '1024' : [6777.22, 27367.96, 108343.76] },
    'isortopn' :  { '64' : [0.3, 0.48, 1.35], '128' : [0.55, 0.8, 1.78], '256' : [1.03, 1.37, 2.17], '512' : [2.66, 2.86, 4.03],  '1024' : [8.08, 8.87, 9.71] },
    
    'psi' :  { '64' : [249.25, 968.8, 3845.82], '128' : [379.71, 1462.32, 5786.62], '256' : [828.24, 3127.55, 12225.06], '512' : [2479.54, 9191.15, 36009.76],  '1024' : [7133.17, 27015.24, 108343.76] },
    'psiopn' :  { '64' : [0.58, 0.81, 1.98], '128' : [0.91, 1.12, 2.31], '256' : [1.51, 1.66, 2.98], '512' : [3.04, 3.1, 5.21],  '1024' : [7.98, 9.23, 12.68] }
}

for key, value in data[benchmark].items():
    for i in range(len(value)):
        if benchmark == "tak" or benchmark == "isort" or benchmark == "psi":
            value[i] /= 10000
    data[benchmark][key] = value
for key, value in data[benchmark+"opn"].items():
    for i in range(len(value)):
        if benchmark == "tak" or benchmark == "isort" or benchmark == "psi":
            value[i] /= 10000
    data[benchmark+"opn"][key] = value

x_axis_labels = {
    'tak' : ("Inputs ($x, y, z$) range", ['[0-3]', '[0-4]', '[0-5]']),
    'isort' : ("Number of Array Elements ($N$)", [32, 64, 128]),
    'psi' : ("Number of Elements in each Set ($N \cap N$)", ["$16 \cap 16$", "$32 \cap 32$", "$64 \cap 64$"]),
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
ax.set_xticks(index)
ax.set_xlabel(x_axis_labels[benchmark][0])
ax.set_xticklabels(x_axis_labels[benchmark][1])
ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), nbits, fontsize=8, ncol=5)

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
autolabel(rects5)

# plt.show()

plt.tight_layout()
plt.savefig("./charts/"+figname,dpi=mydpi, bbox_inches="tight", pad_inches=0.03)
