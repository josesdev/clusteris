# -*- coding: utf-8 -*-

from matplotlib import cm
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Plotter(object):

    def __init__(self):
        plt.rcParams['figure.figsize'] = (16, 9)
        plt.rcParams['axes.unicode_minus'] = False
        plt.style.use('ggplot')

        self.pointsMarkers = ['o', 's', '^', 'v', '<', '>', '8', 'x', '+', 'p']
        self.pointSize = 35
        self.centroidSize = 200
        self.centroidColor = 'r'
        self.centroidMarker = '*'

    def _GetColor(self, intColor, maxColor):
        norm = Normalize(0, float(maxColor))
        cmap = cm.get_cmap("Dark2")

        return cmap(norm(float(intColor)))

    def PlotSamples2D(self, dataset, labels, clusters):
        print('DEBUG - Plotter PlotSamples2D.')

        for i in range(clusters):
            points = np.array([dataset[j] for j in range(len(dataset)) if labels[j] == i])
            color = self._GetColor(i, clusters)
            marker = self.pointsMarkers[i]

            plt.scatter(points[:, 0], points[:, 1], s=self.pointSize, c=color, marker=marker)

    def PlotCentroids2D(self, c):
        print('DEBUG - Plotter PlotCentroids2D.')
        plt.scatter(c[:, 0], c[:, 1], marker=self.centroidMarker, c=self.centroidColor, s=self.centroidSize)

    def PlotSamples3D(self, dataset, labels, clusters):
        print('DEBUG - Plotter PlotSamples3D.')

         # 3D Axes for 3D plotting
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig)

        for i in range(clusters):
            points = np.array([dataset[j] for j in range(len(dataset)) if labels[j] == i])
            color = self._GetColor(i, clusters)
            marker = self.pointsMarkers[i]

            self.ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=self.pointSize, c=color, marker=marker)

    def PlotCentroids3D(self, c):
        print('DEBUG - Plotter PlotCentroids3D.')
        self.ax.scatter(c[:, 0], c[:, 1], c[:, 2], marker=self.centroidMarker, c=self.centroidColor, s=self.centroidSize)

    def Show(self):
        plt.show()