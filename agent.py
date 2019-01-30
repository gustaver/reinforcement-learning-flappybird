import numpy as np
import keras as k
from keras.models import Sequential
from keras.layers import Dense

class Agent:
    def __init__(self):
        self.autonomous = False
        self.reinforcement = False
        self.data = []
        self.data_tmp = []

        classifier = Sequential()
        classifier.add(Dense(7, kernel_initializer='uniform', activation='relu', input_shape=(7,)))
        classifier.add(Dense(14, kernel_initializer='uniform', activation='relu'))
        classifier.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
        classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        self.model = classifier
    
    def add_sample(self, sample):
        self.data_tmp.append(sample)
        
    def save_tmp_data(self):
        self.data.extend(self.data_temp)
        del self.data_tmp[:]

    def discard_tmp_data(self):
        del self.data_tmp[:]

    def train(self):
        data = np.array(self.data)
        X = data[:, :7]
        y = data[:, -1]
        self.model.fit(X, y, epochs = 100)
        
    def flap(self, sample):
        return True if self.model.predict(np.array([sample]))[0] > 0.5 else False
