#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import string

if len(sys.argv) != 2:
    print "Usage:\t python " + sys.argv[0] + " [primes|tak|isort|psi|mmult]"
    sys.exit(1)
if sys.argv[1] == "primes" or sys.argv[1] == "tak" or sys.argv[1] == "isort" or sys.argv[1] == "psi" or sys.argv[1] == "mmult":
    benchmark = sys.argv[1]
else:
    print "Usage:\t python " + sys.argv[0] + " [primes|tak|isort|psi]"
    sys.exit(1)

mydpi = 300
figname = benchmark+'.png'

if benchmark == "primes":
    pltsize = (6, 2.5) # default (8, 6)
elif benchmark == "tak":
    pltsize = (6, 2.2) # default (8, 6)
elif benchmark == "isort":
    pltsize = (6, 2.2) # default (8, 6)
elif benchmark == "psi":
    pltsize = (6, 2.2) # default (8, 6)
elif benchmark == "mmult":
    pltsize = (6, 2.2) # default (8, 6)
elif benchmark == "permutations":
    pltsize = (6, 2.2) # default (8, 6)

nbits = ['64-bit $\lambda$', '128-bit $\lambda$', '256-bit $\lambda$', '512-bit $\lambda$', '1024-bit $\lambda$']


data = {
    'tak' : { '64' : [347.26, 2838.32, 19559.22], '128' : [631.3, 5143.88, 36096.32], '256' : [1451.3, 11863.95, 83044.28], '512' : [3695.09, 30228.41, 205365.2],  '1024' : [11762.58, 98300.55, 500300.55] },
    'primes' :  { '64' : [80.57, 157.46, 317.46], '128' : [190.43, 366.87, 729.19], '256' : [433.87, 816.97, 1598.71], '512' : [1397.44, 2468.49, 4618.86],  '1024' : [4388.98, 7789.04, 14060.56] },
    'isort' :  { '64' : [152.93, 615.65, 2511.54], '128' : [349.79, 1420.64, 5707.16], '256' : [757.48, 3084.15, 12375.45], '512' : [2171.9, 8734.65, 35494.2],  '1024' : [6777.22, 27367.96, 108343.76] },
    'psi' :  { '64' : [249.25, 968.8, 3845.82], '128' : [379.71, 1462.32, 5786.62], '256' : [828.24, 3127.55, 12225.06], '512' : [2479.54, 9191.15, 36009.76],  '1024' : [7133.17, 27015.24, 108343.76] },

    'mmult' :  { '64' : [45.22, 125.24, 216.41], '128' : [106.13, 322.82, 568.54], '256' : [255.38, 642.45, 1540.36], '512' : [700.67, 2962.81, 5138.3],  '1024' : [2267.09, 11030.12, 19218.85] }

    # 'permutations' :  { '64' : [249.25, 968.8, 3845.82], '128' : [379.71, 1462.32, 5786.62], '256' : [828.24, 3127.55, 12225.06], '512' : [2479.54, 9191.15, 36009.76],  '1024' : [7133.17, 27015.24, 108343.76] }
}

for key, value in data[benchmark].items():
    for i in range(len(value)):
        if benchmark == "tak" or benchmark == "isort" or benchmark == "psi":
            value[i] /= 10000
        elif benchmark == "primes":
            value[i] /= 1000
        elif benchmark == "mmult":
            value[i] /= 1000
    data[benchmark][key] = value


x_axis_labels = {
    'tak' : ("Inputs ($x, y, z$) range", ['[0-3]', '[0-4]', '[0-5]']),
    'primes' : ("Maximum number to compute", [256, 512, 1024]),
    'isort' : ("Number of Array Elements ($N$)", [32, 64, 128]),
    'psi' : ("Number of Each Array Elements ($N \cap N$)", ["$16 \cap 16$", "$32 \cap 32$", "$64 \cap 64$"]),
    
    'mmult' : ("Matrices Size", ['8x8 x 8x8', '12x8 x 8x12', '16x8 x 8x16'])
}

# max_num = [256, 512, 1024]

data64 = data[benchmark]['64']
data128 = data[benchmark]['128']
data256 = data[benchmark]['256']
data512 = data[benchmark]['512']
data1024 = data[benchmark]['1024']


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

# add some text for labels, title and axes ticks
# if benchmark == "tak":
#     ax.set_title("Tak function,  beta = 8")
# elif benchmark == "primes":
#     ax.set_title("Endless Sieve of Eratosthenes,  beta = 16")
# elif benchmark == "isort":
#     ax.set_title("Insertion Sort,  beta = 16")
# else:
#     ax.set_title(string.capwords(benchmark))

ax.set_yscale('log')
if benchmark == "primes":
    ax.set_ylim([0.06, 100])
    ax.set_ylabel("time (sec.) x $10^3$")
elif benchmark == "tak":
    ax.set_ylim([0.02, 120])
    ax.set_ylabel("time (sec.) x $10^4$")
elif benchmark == "isort":
    ax.set_ylim([0.01, 30])
    ax.set_ylabel("time (sec.) x $10^4$")
elif benchmark == "psi":
    ax.set_ylim([0.01, 40])
    ax.set_ylabel("time (sec.) x $10^4$")
elif benchmark == "mmult":
    ax.set_ylim([0.04, 100])
    ax.set_ylabel("time (sec.) x $10^3$")
ax.set_xticks(index)
ax.set_xlabel(x_axis_labels[benchmark][0])
ax.set_xticklabels(x_axis_labels[benchmark][1])
ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), nbits, fontsize=8)

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
