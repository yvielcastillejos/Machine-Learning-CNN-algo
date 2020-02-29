import matplotlib.pyplot as plt
import helloworldmi

i = 0
# shows the training set for up to 5 images
for i in range(0,5,1):
  plt.imshow(x_train[i], cmap = plt.cm.winter)
  plt.show()

# shows the testing set
for i in range(0,5,1):
  plt.imshow(x_test[i], cmap = plt.cm.winter)
  plt.show()
