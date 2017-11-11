import matplotlib.pyplot as plt
import numpy as np
from matplotlib import collections

audience_edges=np.array([[[0,0],[10,1],[30,1],[40,1]],
                [[30,0],[40,1],[60,1],[70,0]],
                [[60,0],[70,1],[90,1],[100,0]]])

fan_edges=np.array([
                [[1,0],[30,0]],
                [[20,0],[40,1],[60,1],[80,0]],
                [[70,0],[100,1]]
                ])       

noise_edges=np.array([
                [[1,0],[30,0]],
                [[20,0],[40,1],[60,1],[80,0]],
                [[70,0],[100,1]]
                ])   

# print (audience_edges)
for i in range(audience_edges.size):
	# print(i)
	for j in range(audience_edges[i].size):
		print ("{}:{} {}:{} ".format(i,audience_edges.size,j,audience_edges[i].size),end="")
		for k in range(audience_edges[i][j].size):
			print("{} ".format(audience_edges[i][j][k]),end="")
		print("")

# plt.figure(1)
# for i in range(audience_edges.size):  #iterator for different fuzzy sets
# 	plt.subplot(211+i)
# 	x_vals=[]
# 	y_vals=[]
# 	for j in range(audience_edges[i].size): 		
# 		x_vals.append(audience_edges[0][i][j][0])
# 		y_vals.append(audience_edges[0][i][j][1])
# 	plt.plot(x,y)