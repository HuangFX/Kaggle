
#!/usr/bin/env python
# encoding: utf-8

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x_list = [[3,3,2],[4,3,1],[1,2,3],[1,1,2],[2,1,2]]
fig = plt.figure()
ax = fig.gca(projection='3d')
for x in x_list:
    ax.scatter(x[0],x[1],x[2],c='r')
plt.show()
