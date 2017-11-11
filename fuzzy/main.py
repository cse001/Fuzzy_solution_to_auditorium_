import matplotlib.pyplot as plt
import numpy as np
from matplotlib import collections


class Entry:
    def __init__(self, x1, x2, m, c, region):
        self.x1 = x1
        self.x2 = x2
        self.m = m
        self.c = c
        self.region = region

audience_edges = np.array([[[0, 0], [10, 1], [30, 1], [40, 0]],
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
for i in range(len(audience_edges)):  # iterator for different fuzzy sets
        plt.subplot(111)
        plt.ylim(0, 5)
        x_vals = []
        y_vals = []
        for j in range(len(audience_edges[i])):
                x_vals.append(audience_edges[i][j][0])
                y_vals.append(audience_edges[i][j][1])
        plt.plot(x_vals, y_vals)


plt.figure(2)
for i in range(len(fan_edges)):  # iterator for different fuzzy sets
        plt.subplot(111)
        plt.ylim(0, 5)
        x_vals = []
        y_vals = []
        for j in range(len(fan_edges[i])):
                x_vals.append(fan_edges[i][j][0])
                y_vals.append(fan_edges[i][j][1])
        plt.plot(x_vals, y_vals)


plt.figure(3)
for i in range(len(noise_edges)):  # iterator for different fuzzy sets
        plt.subplot(111)
        plt.ylim(0, 5)
        x_vals = []
        y_vals = []
        for j in range(len(noise_edges[i])):
                x_vals.append(noise_edges[i][j][0])
                y_vals.append(noise_edges[i][j][1])
        plt.plot(x_vals, y_vals)

plt.show()

queries = int(input())

audience_set = list()
fans_set = list()
noise_set = list()
audience_set.append(Entry(10, 20, 4/3, 20, 0))

for q in range(queries):

    audience = int(input())
    no_of_fans = int(input())
    noise_value = int(input)

    fuzzy_set_of_audience = [0, 0, 0]

    for audi in audience_set:
        if audi.x1 <= audience <= audi.x2:
            membership_value = audience*audi.m + audi.c
            fuzzy_set_of_audience[audi.region] = membership_value

    fuzzy_set_of_fans = [0, 0, 0]

    for fan in fans_set:
        if fan.x1 <= no_of_fans <= fan.x2:
            membership_value = no_of_fans*fan.m + fan.c
            fuzzy_set_of_audience[fan.region] = membership_value

    fuzzy_set_of_noise = [0, 0, 0]

    for noise in noise_set:
        if noise.x1 <= noise_value <= noise.x2:
            membership_value = noise_value*noise.m + noise.c
            fuzzy_set_of_audience[noise.region] = membership_value


