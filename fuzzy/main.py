import matplotlib.pyplot as plt
import numpy as np
from matplotlib import collections



audience_edges = np.array([[[0, 0], [10, 1], [30, 1], [40, 1]],
                           [[30, 0], [40, 1], [60, 1], [70, 0]],
                           [[60, 0], [70, 1], [90, 1], [100, 0]]])

fan_edges = np.array([
    [[1, 1], [30, 0]],
    [[20, 0], [40, 1], [60, 1], [80, 0]],
    [[70, 0], [100, 1]]
])

noise_edges = np.array([
    [[1, 1], [30, 0]],
    [[20, 0], [40, 1], [60, 1], [80, 0]],
    [[70, 0], [100, 1]]
])


plt.axis([0, 105, 0, 1.2])

plt.figure(1)
for i in range(len(audience_edges)):  #iterator for different fuzzy sets
        plt.subplot(111)
        plt.ylim(0,5)
        x_vals=[]
        y_vals=[]
        for j in range(len(audience_edges[i])):                 
                x_vals.append(audience_edges[i][j][0])
                y_vals.append(audience_edges[i][j][1])
        plt.plot(x_vals,y_vals)

plt.figure(2)
for i in range(len(fan_edges)):  #iterator for different fuzzy sets
        plt.subplot(111)
        plt.ylim(0, 5)
        x_vals=[]
        y_vals=[]
        for j in range(len(fan_edges[i])):                 
                x_vals.append(fan_edges[i][j][0])
                y_vals.append(fan_edges[i][j][1])
        plt.plot(x_vals,y_vals)


plt.figure(3)
for i in range(len(noise_edges)):  #iterator for different fuzzy sets
        plt.subplot(111)
        plt.ylim(0, 5)
        x_vals=[]
        y_vals=[]
        for j in range(len(noise_edges[i])):                 
                x_vals.append(noise_edges[i][j][0])
                y_vals.append(noise_edges[i][j][1])
        plt.plot(x_vals,y_vals)

plt.show()


op=np.empty(27).reshape(3, 3, 3)
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i+j+k<=1:
                op[i][j][k]=0
            elif i+j+k<=4:
                op[i][j][k] = 1
            else:
                op[i][j][k] = 2


audience_line_segment=[]
fan_edges_line_segment=[]
noise_line_segment=[]
for i in range(3):
    temp=[]
    if(i==0):
        temp=audience_edges
    elif i==1:
        temp=fan_edges
    else:
        temp=noise_edges
    for j in range(len(temp)):
        for k in range(len(temp[j]) - 1):
            seg_details = []
            slope = ((temp[j][k + 1][1] - temp[j][k + 1][0]) * 1.0) / (
            (temp[j][k][1] - temp[j][k][0]))
            intercept = temp[j][k + 1][1] - slope * temp[j][k + 1][1]
            seg_details.append(Entry(temp[j][k][0], temp[j][k + 1][0], slope, intercept,j))

q=int(input().strip())
for qq in range(q):
    crowd_ct, fan_val, distrb_val=input().strip().split(" ")


