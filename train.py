import pandas as pd
import os

#데이터 핸들링
file = pd.read_csv('pos.csv')

data = file.values.tolist()

X_train = [i[:-1] for i in data]
y_train = [i[-1] for i in data]

#머신러닝
import tensorflow as tf
import numpy as np

y_one_hot = tf.keras.utils.to_categorical(y_train)

learning_rate = 1e-2
learning_epochs = 1000

sgd =tf.keras.optimizers.SGD(learning_rate=learning_rate)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(2,input_shape = (30,),activation='relu')) # input layer
model.add(tf.keras.layers.Dense(10,activation='relu')) # hidden layer
model.add(tf.keras.layers.Dense(2,activation='softmax')) # output layer
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

model.summary()

history = model.fit(np.array(X_train),np.array(y_one_hot),epochs=learning_epochs)

import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(history.history['loss'])
plt.show()

input = []
result = model.predict(np.array([input]))

classes = ['standUp','Squat']
classID = np.argmax(result[0])
prediction = classes[classID]

print(prediction)
