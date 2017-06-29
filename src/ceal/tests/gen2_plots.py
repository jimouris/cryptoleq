#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import string

if len(sys.argv) != 2:
    print "Usage:\t python " + sys.argv[0] + " [primes|tak|isort]"
    sys.exit(1)
if sys.argv[1] == "primes" or sys.argv[1] == "tak" or sys.argv[1] == "isort":
    benchmark = sys.argv[1]
else:
    print "Usage:\t python " + sys.argv[0] + " [primes|tak|isort]"
    sys.exit(1)

mydpi = 300
figname = benchmark+'.png'
pltsize = (7, 4) # default (8, 6)
nbits = ['N = 64', 'N = 128', 'N = 256', 'N = 512', 'N = 1024']


data = {
    'tak' : { '64' : [347.26, 2838.32, 19559.22], '128' : [631.3, 5143.88, 36096.32], '256' : [1451.3, 11863.95, 83044.28], '512' : [3695.09, 30228.41, 205365.2],  '1024' : [11762.58, 98300.55, 500300.55] },
    'primes' :  { '64' : [80.57, 157.46, 317.46], '128' : [190.43, 366.87, 729.19], '256' : [433.87, 816.97, 1598.71], '512' : [1397.44, 2468.49, 4618.86],  '1024' : [4388.98, 7789.04, 14060.56] },
    'isort' :  { '64' : [152.93, 615.65, 2511.54], '128' : [349.79, 1420.64, 5707.16], '256' : [757.48, 3084.15, 12375.45], '512' : [2171.9, 8734.65, 35494.2],  '1024' : [6777.22, 27367.96, 108343.76] }
}

x_axis_labels = {
    'tak' : ("Input range", ['[0-3]', '[0-4]', '[0-5]']),
    'primes' : ("Maximum number to compute", [256, 512, 1024]),
    'isort' : ("Array length", [32, 64, 128])
}

max_num = [256, 512, 1024]

data64 = data[benchmark]['64']
data128 = data[benchmark]['128']
data256 = data[benchmark]['256']
data512 = data[benchmark]['512']
data1024 = data[benchmark]['1024']


N = len(data64)
index = np.arange(N)  # the x locations for the groups
width = 0.185       # the width of the bars

fig, ax = plt.subplots(figsize=pltsize)
rects1 = ax.bar(index - 2*width, data64, width, color='xkcd:light pink', hatch='xxxx', edgecolor='black', linewidth=1)
rects2 = ax.bar(index - width, data128, width, color='xkcd:very light blue', hatch='....', edgecolor='black', linewidth=1)
rects3 = ax.bar(index, data256, width, color='xkcd:very light green', hatch='/////', edgecolor='black', linewidth=1)
rects4 = ax.bar(index + width, data512, width, color='xkcd:ecru', hatch='----', edgecolor='black', linewidth=1)
rects5 = ax.bar(index + 2*width, data1024, width, color='xkcd:light peach', hatch='\\\\\\\\\\', edgecolor='black', linewidth=1)

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
# ax.set_ylim([10000, 1000000])
ax.set_ylabel("time (sec.) x e4")
ax.set_xticks(index)
ax.set_xlabel(x_axis_labels[benchmark][0])
ax.set_xticklabels(x_axis_labels[benchmark][1])

ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), nbits, fontsize=9)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height/10000 > 10:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.1f' % (height/10000), ha='center', va='bottom', fontsize=8)
        else:
            ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%2.2f' % (height/10000), ha='center', va='bottom', fontsize=8)
        # ax.text(rect.get_x() + rect.get_width()/2., 1.1*height, '%d' % int(height), ha='center', va='bottom', fontsize=9)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)

plt.show()

# plt.tight_layout()
# plt.savefig("./charts/"+figname,dpi=mydpi, bbox_inches="tight", pad_inches=0)
