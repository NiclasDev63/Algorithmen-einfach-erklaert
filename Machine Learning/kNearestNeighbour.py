import numpy as np
from sklearn.datasets import load_iris
from scipy.stats import mode
from sklearn.metrics import accuracy_score

def eucledianDist(p1,p2):
    dist = np.sqrt(np.sum((p1-p2)**2))
    return dist

def kNearestNeighbour(x_train, y_train, x_test, k):
    op_labels = []
     
    #Loop through the Datapoints to be classified
    for item in x_test: 
         
        #Array to store distances
        point_dist = []
         
        #Loop through each training Data
        for j in range(len(x_train)): 
            dist = eucledianDist(np.array(x_train[j]), item)
            point_dist.append(dist)
        point_dist = np.array(point_dist)

        dist = np.argsort(point_dist)[:k]

        labels = y_train[dist]

        lab = mode(labels)
        lab = lab.mode[0]
        op_labels.append(lab)

    return op_labels


            

iris = load_iris()

X = iris.data
Y = iris.target

accuracy = 0
test = 40
k = 8
for i in range(test):

    #Creating the training Data
    train_idx = np.random.randint(0,150,150)
    X_train = X[train_idx]
    y_train = Y[train_idx]
    
    #Creating the testing Data
    test_idx = np.random.randint(0,150,10)
    X_test = X[test_idx]
    y_test = Y[test_idx]

    y_pred = kNearestNeighbour(X_train, y_train, X_test, k)


    accuracy += accuracy_score(y_test, y_pred)

accuracy_result = accuracy / test
print("Unweighted kNearestNeighbour")
print("k = " + str(k))
print("Testruns: " + str(test))
print("Accuracy: " + str(accuracy_result))


