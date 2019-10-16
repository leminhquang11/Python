
# Stept 1: import Thu vien
from keras import layers, models, optimizers, metrics, losses
from keras.datasets import mnist
import matplotlib.pyplot as plt
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# step 2: Format Data	
	ori_train_images = train_images.copy()
	ori_train_labels = train_labels.copy()

	ori_test_images = test_images.copy()
	ori_test_labels = test_labels.copy()
from keras.utils import to_categorical
	train_images = ori_train_images.copy()

	train_images = train_images.reshape((60000, 28, 28, 1))
	train_images = train_images.astype('float32') / 255
	train_labels = to_categorical(ori_train_labels.copy())

	test_images = ori_test_images.copy()
	test_images = test_images.reshape((10000, 28, 28, 1))
	test_images = test_images.astype('float32') / 255
	test_labels = to_categorical(ori_test_labels.copy())

#step 3: Design Model

	net = models.Sequential()
	net.add(layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1))) # need 4D tensor so we need (batch, 28, 28, 1)
	net.add(layers.MaxPooling2D((2, 2)))        
	net.add(layers.Conv2D(64, kernel_size=(3, 3), activation='relu'))
	net.add(layers.MaxPooling2D(pool_size=(2, 2)))
	net.add(layers.Conv2D(64, kernel_size=(3, 3), activation='relu'))
	net.add(layers.Flatten())
	net.add(layers.Dense(64, activation='relu'))
	net.add(layers.Dense(10, activation='softmax'))
	        
	net.summary()

# Step 4: Training Data
net.compile(optimizer=optimizers.Adam(), 
            loss=losses.categorical_crossentropy,
            metrics=[metrics.categorical_accuracy])
history = net.fit(train_images, 
                  train_labels, 
                  epochs=10,
                  batch_size=64,
                  validation_data=(test_images, test_labels))
# Stept 5: In ra bieu do

history_dict = history.history

train_acc = history_dict['categorical_accuracy']
train_loss = history_dict['loss']
val_acc = history_dict['val_categorical_accuracy']
val_loss = history_dict['val_loss']

epochs = range(1, len(train_acc) + 1)

plt.plot(epochs, train_loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation losses')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.figure()

plt.plot(epochs, train_acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()

