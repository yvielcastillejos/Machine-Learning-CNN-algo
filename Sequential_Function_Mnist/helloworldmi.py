import tensorflow as tf
import keras
from keras import layers
import sequential_function

# get data set using Mnist
data1 = tf.keras.datasets.mnist
(x_train, y_train),(x_test,y_test) = data1.load_data() # unpacks the data set into train sets and test sets since there are four files
dataset_train = (x_train, y_train)
dataset_test = (x_test,y_test)

# We want to scale the data 0-1
(x_train, y_train),(x_test,y_test) = normalize(dataset_train, dataset_test)

model = tf.keras.models.Sequential() # Uses the sequential Function
model.add(tf.keras.layers.Flatten()) # Flattens the inputs
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy']
model.fit(x_train,y_train,epochs=3)
