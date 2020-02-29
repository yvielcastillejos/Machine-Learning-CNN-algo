def normalize(dataset_train,dataset_test):
  (dataset_train[0], dataset_train[1]), (dataset_test[0], dataset_test[1]) = (tf.keras.utils.normalize(x_train,axis =1), y_train), (tf.keras.utils.normalize(y_train,axis =1), y_train)
  return dataset_train,dataset_test
