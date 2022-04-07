import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score


def eucledianDist(p1,p2):
    dist = np.sqrt(np.sum((p1-p2)**2))
    return dist

def kNearestNeighbour(x_train, y_train, x_test, k):
    op_labels = []
     
    #Loop through the Datapoints to be classified
    for item in x_test: 
         
        #Array to store score for each Datapoint
        score = []
         
        #Loop through each training Data
        for j in range(len(x_train)): 
            dist = eucledianDist(np.array(x_train[j]), item)
            if dist == 0:
                score.append(2)
            else:
                aa = (1/dist)
                score.append(aa)

        score = np.array(score)

        dist = np.argsort(score)[::-1][:k]
        score = np.sort(score)[::-1][:k]
        labels = y_train[dist]


        available_labels = set(labels)

        bb = [0 for _ in range(len(labels))]
        for i in available_labels:
            for j in range(len(score)):
                if labels[j] == i:
                    bb[i] += score[j]
  
        bb = np.array(bb)
        bb = np.argsort(bb)[::-1][:k]
        op_labels.append(bb[0])
        

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
    test_idx = np.random.randint(0,150,40)
    X_test = X[test_idx]
    y_test = Y[test_idx]



    y_pred = kNearestNeighbour(X_train, y_train, X_test, k)


    accuracy += accuracy_score(y_test, y_pred)

accuracy_result = accuracy / test
print("Weighted kNearestNeighbour")
print("k = " + str(k))
print("Testruns: " + str(test))
print("Accuracy: " + str(accuracy_result))


