#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

mydpi = 300
figname = 'CHOOSENAME-HERE.png'

# data = ((10, 21), (28, 67), (58, 128), (150, 327), (443, 931)) # fib
# data = ((10.04, 21.285), (28.86333333, 67.97166667), (58.64166667, 128.1783333), (150.3016667, 327.3716667), (443.0366667, 931.0583333)) # factorial
data = ((910.39, 3269.625), (2059.405, 7288.04), (4439.46, 15830.21), (12514.24, 44812.925), (38192.405, 132622.735)) # Nqueens

nbits = [64, 128, 256, 512, 1024]
labels = ["beta = 16", "beta = 24"]

plt.xlabel("N bits")
plt.ylabel("time (sec.)")
plt.title("Average")
plt.yscale('log')

dim = len(data[0])
w = 0.75
dimw = w / dim

x = np.arange(len(data))
for i in range(len(data[0])):
    y = [d[i] for d in data]
    b = plt.bar(x + i * dimw, y, dimw, bottom=0, label=labels[i%2])

plt.xticks(x + dimw / 2, map(str, nbits))


legend = plt.legend(loc='upper left', shadow=False)
frame = legend.get_frame()

plt.show()
# plt.tight_layout()
# plt.savefig(figname,dpi=mydpi)

