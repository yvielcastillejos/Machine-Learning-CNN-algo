import matplotlib.pyplot as plt
import numpy as np
import helloworldmi

#save model

#print the accuracy and loss
value_loss, value_acc = model.evaluate(x_test,y_test)
print(value_loss,value_acc) #too much means underfit, too little overfit

model.save("number_reader.model")
new_model = tf.keras.models.load_model("number_reader.model)
predictions = new_model.predict(x_test)

#prints 5 predictions of the images
for i in range(0,5,1):
  print("The prediction is: " + string(np.argmax.predictions[i]))
  print("The image is: ")
  plt.imshow(x_test[i])
