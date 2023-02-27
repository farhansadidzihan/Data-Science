import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Taking Data
data = keras.datasets.fashion_mnist

# Loading Data
(train_images, train_labels), (test_images, test_labels) = data.load_data()

# Giving the Class Names
class_name = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Cost", "Sandal",
              "Shirt", "Sneaker", "Bag", "Ankle Boot"]

train_images = train_images / 255
test_images = test_images / 255

print(train_images[7])

# Plotting the Data
plt.imshow(train_images[7], cmap=plt.cm.binary)
plt.show()