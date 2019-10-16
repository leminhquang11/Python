from keras import layers, models, optimizers, metrics, losses
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
	print("train_images.shape", train_images.shape)
	print("image shape", train_images[0].shape)
	print("train_labels.shape", train_labels.shape)
	print("len(train_labels)", len(train_labels))
	print("test_images.shape", test_images.shape)
	print("image shape", test_images[0].shape)
	print("test_labels.shape", test_labels.shape)
	print("len(test_labels)", len(test_labels))
	print("train_labels[5:15]", train_labels[5:15])
import matplotlib.pyplot as plt
	plt.imshow(train_images[1000], cmap='gray')
	plt.show()

