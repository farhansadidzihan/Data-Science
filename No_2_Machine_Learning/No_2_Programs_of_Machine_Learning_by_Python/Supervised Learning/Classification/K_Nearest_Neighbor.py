import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Loading Datasets
iris = datasets.load_iris()
features = iris.data[25:]
labels = iris.target[25:]

clf = KNeighborsClassifier()
clf.fit(features, labels)

for _ in range(101):
	prediction = clf.predict([np.random.randint(1, 10, size=4)])
	print(prediction, end="")
