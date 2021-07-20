import json
import pandas as pd
import os

#데이터 핸들링
file = pd.read_csv(r'C:\Users\user\Desktop\graduate\pos.csv')

data = file.values.tolist()

X_train = [i[:-1] for i in data]
y_train = [i[-1] for i in data]

# 머신러닝
import tensorflow as tf
import numpy as np

y_one_hot = tf.keras.utils.to_categorical(y_train)

learning_rate = 1e-2
learning_epochs = 2000

def get_model():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(10,input_shape = (30,),activation='relu')) # input layer
    model.add(tf.keras.layers.Dense(64,activation='relu')) # hidden layer
    model.add(tf.keras.layers.Dense(64,activation='relu')) # hidden layer
    model.add(tf.keras.layers.Dense(5,activation='softmax')) # output layer
    model.compile(loss='categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])
    return model

model = get_model()
model.summary()

history = model.fit(np.array(X_train),np.array(y_one_hot),epochs=learning_epochs)

import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(history.history['loss'])
plt.show()

for step in range(learning_epochs):
    if step %100 == 0:
        cost_val = history.history['loss'][step]
        acc_val = history.history['accuracy'][step]
        print("%20i %20.5f %20.5f" % (step,cost_val,acc_val))
Input = [232,88,208,136,184,136,160,168,176,168,224,152,224,200,224,240,168,176,168,216,160,280,200,184,216,208,200,272,192,160]
prediction = model.predict(np.array([Input]))
print(prediction[0])

classes = ['Stand','Squat','Lying','LegUp','Plank']
classID = np.argmax(prediction[0])
result = classes[classID]

print(result)

model_json = model.to_json()
with open("model.json","w") as json_file:
    json_file.write(model_json)

model.save('model.h5')