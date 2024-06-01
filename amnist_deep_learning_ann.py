# -*- coding: utf-8 -*-
"""Amnist_Deep_Learning_ANN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nqpnMILCbE77MK2gTzdle_XHOdztpWuO
"""

import numpy as np
import matplotlib.pyplot as plt
import keras

from keras.datasets import mnist

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import to_categorical
import random

np.random.seed(0)

(X_train,y_train),(X_test,y_test)=mnist.load_data()

print(X_train.shape)
print(X_test.shape)
print(y_test.shape)

X_train

y_test

set(y_train)

plt.imshow(X_train[y_train==4][1000])   #1000--->Index Position
plt.axis('off')
plt.show()

plt.imshow(X_train[y_train==4][5841],cmap='gray')   #1000--->Index Position
plt.axis('off')
plt.show()

for i in range(0,10):
  print(i,':',len(X_train[y_train==i]))

for i in range(0,10):
   plt.imshow(X_train[y_train==i][np.random.randint(0,5000)],cmap='gray')
   plt.title(str(i))
   plt.axis('off')
   plt.show()

y_train=to_categorical(y_train,10)
y_test=to_categorical(y_test,10)

X_train=X_train/255
X_test=X_test/255

X_train

X_train.shape

y_train

num_pixels=784
X_train=X_train.reshape(X_train.shape[0],num_pixels)
X_test=X_test.reshape(X_test.shape[0],num_pixels)

X_train

X_train.shape

def create_model():
  model=Sequential()

  #Input Layer
  model.add(Dense(10,input_dim=num_pixels,activation='relu'))

  #Hidden Layers
  model.add(Dense(30,activation='relu'))
  model.add(Dense(10,activation='relu'))

  #Output Layer
  model.add(Dense(10,activation='softmax'))
  model.compile(Adam(learning_rate=0.01),loss='categorical_crossentropy',metrics=['accuracy'])
  return model

model=create_model()
print(model.summary())

h=model.fit(X_train,y_train,validation_split=0.1,epochs=10,verbose=1)

plt.plot(h.history['accuracy'])
plt.plot(h.history['val_accuracy'])
plt.legend(['accuracy','val_accuracy'])
plt.title('Accuracy')
plt.xlabel('epoch')
plt.show()

plt.plot(h.history['loss'])
plt.plot(h.history['val_loss'])
plt.legend(['loss','val_loss'])
plt.title('Loss')
plt.xlabel('epoch')
plt.show()

from google.colab import files
upload=files.upload()

d=list(upload.keys())[0]
print(d)

import cv2
a=np.fromstring(upload[d],np.uint8)
b=cv2.imdecode(a,cv2.IMREAD_COLOR)
print(a)

plt.imshow(b,cmap=plt.get_cmap("gray"))
plt.show()

b=cv2.resize(b,(28,28))
b=cv2.cvtColor(b,cv2.COLOR_BGR2GRAY)
b=cv2.bitwise_not(b)
plt.imshow(b,cmap=plt.get_cmap("gray"))
plt.show()

b=b/255
b=b.reshape(1,784)
prediction=model.predict(b)

prediction

p=np.argmax(prediction,axis=1)
p

print(str(p))

