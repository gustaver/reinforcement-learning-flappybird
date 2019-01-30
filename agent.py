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
        self.flap_perc = 0.01

        classifier = Sequential()
        classifier.add(Dense(4, kernel_initializer='uniform', activation='relu', input_shape=(4,)))
        classifier.add(Dense(4, kernel_initializer='uniform', activation='relu'))
        classifier.add(Dense(4, kernel_initializer='uniform', activation='relu'))
        classifier.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
        classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        self.model = classifier
    
    def add_sample(self, sample):
        self.data_tmp.append(sample)
        
    def save_tmp_data(self):
        self.data.extend(self.data_tmp)
        del self.data_tmp[:]

    def discard_tmp_data(self):
        del self.data_tmp[:]

    def switch_reinforcement(self):
        self.reinforcement = True if self.reinforcement == False else False
    
    def switch_autonomous(self):
        self.autonomous = True if self.autonomous == False else False

    def train(self):
        data = np.array(self.data)
        X = data[:, :4]
        y = data[:, -1]
        self.model.fit(X, y, epochs = 100)
        self.flap_perc = (data[:, -1] == 1).mean()
        
    def flap(self, sample):
        return True if self.model.predict(np.array([sample]))[0] > self.flap_perc else False

    def print_state(self):
        data = np.array(self.data)
        print('Number of training datapoints = ', data.shape[0])
        print('Percentage of 1s = ', (data[:, -1] == 1).mean())
        print('Percentage of 0s = ', (data[:, -1] == 0).mean())
