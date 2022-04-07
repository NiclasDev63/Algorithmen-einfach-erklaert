import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.datasets import make_blobs


def elbowMethod(centroids, dataset, dist):
    inertias = []
    for i in range(len(centroids)):
        inertias.append(np.sum([(dataset[x]-centroids[i])**2 for x in range(len(dataset)) if dist[x] == i], axis=0))
    return np.sum(inertias)


def plotData(x_train, centroids, dist, k):
    for j in range(len(dist)):
        if dist[j] == 0:
            plt.scatter(x_train[j][0], x_train[j][1], marker="o", c = "g")
        elif dist[j] == 1:
            plt.scatter(x_train[j][0], x_train[j][1], marker="o", c = "y")
        elif dist[j] == 2:
            plt.scatter(x_train[j][0], x_train[j][1], marker="o", c = "r")
        elif dist[j] == 3:
            plt.scatter(x_train[j][0], x_train[j][1], marker="o", c = "b")
    plt.suptitle('Number of Centroids (k): ' + str(k))
    plt.scatter(centroids[:, 0], centroids[:, 1], marker="X", c = "k")
    plt.show()


def euclidDist(dataset, centroids, dimensions, k):
    dist = []
    for datapoint in dataset:
        dist.append(np.argmin(np.sqrt(np.sum(datapoint.reshape(1, dimensions) - centroids, axis=1)**2)))
    return dist

def kMeans(dist, k, dataset):
    new_centroids = []
    for i in range(k):
        new_centroids.append(np.mean([dataset[x] for x in range(len(dataset)) if dist[x] == i], axis=0))
    return new_centroids

def run(dataset, k, plot_data):
    dimensions = dataset.shape[1]



    #centroids = np.array(np.random.normal(size=(k, int(dimensions))) + np.mean(dataset))
    centroids = [[7.12719551,4.18567991],[4.11272459,2.70458679]]
    centroids = np.array(centroids)

    count = 0
    while True:
        centroids_copy = np.copy(centroids)
        
        dist = euclidDist(dataset, centroids, dimensions, k)
        if plot_data:
            if count == 0:
                plotData(dataset, centroids, dist, k)
        count += 1
        centroids = kMeans(dist, k, dataset)
        new_centroids = np.array(centroids)
        centroids = np.array(new_centroids)
        centroids.reshape(k, dimensions)
        if np.array_equal(centroids_copy,centroids) == True:
            break

    if plot_data:
        plotData(dataset, centroids, dist, k)

    return elbowMethod(centroids, dataset, dist)







if __name__ == "__main__":

    iris = load_iris()
    X = iris.data[:, :2]
    # Y = iris.target

    # random_number = np.random.randint(0, 150, 30)
    # dataset = X[random_number]
    # y_train = Y[random_number]

    # x_train = np.array(dataset)
    # dataset, labels = make_blobs(
    #     n_samples=150,
    #     centers=5,
    #     cluster_std=4,
    #     random_state=12
    # )

    train_idx = range(20)
    dataset = X[train_idx]

    dimensions = dataset.shape[1]

    dataset = np.array(dataset)

    plot_data = True

    k = 2
    # inertias = []
    # k = range(1, 6)
    # for i in k:
    #     print("k = " + str(i))
    #     values = run(dataset, i, plot_data)
    #     inertias.append(values)


    # plt.plot(k, inertias)
    # plt.show()

    run(dataset, k, plot_data)

