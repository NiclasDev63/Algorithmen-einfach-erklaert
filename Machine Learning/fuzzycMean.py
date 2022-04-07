import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


def plotData(dataset, centroids, memDegrees, c):
    for i in range(len(dataset)):
        belonging_centroid = np.argmax([memDegrees[j][i] for j in range(c)])
        if belonging_centroid == 0:
            plt.scatter(dataset[i][0], dataset[i][1], marker="o", c = "g")
        elif belonging_centroid == 1:
            plt.scatter(dataset[i][0], dataset[i][1], marker="o", c = "y")
        elif belonging_centroid == 2:
            plt.scatter(dataset[i][0], dataset[i][1], marker="o", c = "r")
        elif belonging_centroid == 3:
            plt.scatter(dataset[i][0], dataset[i][1], marker="o", c = "b")

    plt.suptitle('Number of Centroids (c): ' + str(c))
    plt.scatter(centroids[:, 0], centroids[:, 1], marker="X", c = "k")
    plt.show()

def euclidDist(datapoint, centroid):
    return np.sqrt(np.sum(datapoint - centroid)**2)

def calculateMembershipDegress(dataset, c, centroids, m):
    membershipDegress = [[0 for _ in range(len(dataset))]for _ in range(c)]

    for i in range(c):
        for j in range(len(dataset)):
            denominator = np.sum([(euclidDist(dataset[j], centroids[i])) / (euclidDist(dataset[j], centroids[x])) for x in range(c)])
            membershipDegress[i][j]  = 1 / (denominator **(2/(m-1)))

    return membershipDegress

def calculateCentroids(dataset, c, m, memDegrees):
    memDegrees = np.array(memDegrees)
    new_centroids = []
    numerator = []
    denominator = []
    for i in range(c):
        numerator .append(np.sum([(memDegrees[i][j]**m)  * dataset[j] for j in range(len(dataset))], axis = 0))
        denominator.append(np.sum([(memDegrees[i][j]**m) for j in range(len(dataset))], axis = 0))

    numerator = np.array(numerator)
    denominator = np.array(denominator)

    for i in range(c):

        new_centroids.append(numerator[i] / denominator[i])

    return new_centroids

        



iris = load_iris()

X = iris.data[:, :2]



random_number = np.random.randint(0, 150, 80)
dataset = X[random_number]
dimensions = dataset.shape[1]

c = 2
m = 2
treshold =  0.0003


centroids = np.random.normal(size=(c, int(dimensions))) + np.mean(dataset)
centroids = np.array(centroids)

count = 0
while True:
    centroids_copy = np.copy(centroids)
    memDegrees  = calculateMembershipDegress(dataset, c, centroids, m)

    memDegrees = np.array(memDegrees)
    if count == 0:
        plotData(dataset, centroids, memDegrees, c)
    count += 1
    centroids = calculateCentroids(dataset, c, m, memDegrees)
    centroids = np.array(centroids)
    if euclidDist(centroids, centroids_copy) < treshold:
        break


plotData(dataset, centroids, memDegrees, c)


