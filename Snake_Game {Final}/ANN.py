# Importing the libraries

import pandas as pd
from sklearn.model_selection import train_test_split
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from keras import optimizers


# Importing the dataset
dataset = pd.read_csv('SNAKE_A.csv')
dataset = dataset.dropna()


X = dataset.iloc[:, 0:9].values
y = dataset.iloc[:, 9].values


# making prediction column as categorical.
ohe = OneHotEncoder(sparse=False)
y = y.reshape(-1, 1)
y = ohe.fit_transform(y)

#print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.7)

#Initializing Neural Network
model = Sequential()

# Adding the input layer and the first hidden layer
model.add(Dense(output_dim = 80, init = 'uniform', activation = 'relu', input_dim = 9))

# Adding the input layer and the second hidden layer
model.add(Dense(output_dim = 50, init = 'uniform', activation = 'relu'))

# Adding the output layer
model.add(Dense(output_dim = 3, init = 'uniform', activation = 'softmax'))

# creating optimizer.
# my_opt = optimizers.SGD(lr = 0.01, decay = 1e-6, momentum = 0.9, nesterov = True)
# my_opt = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)

# Compiling Neural Network.
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Fitting our model
model.fit(X_train, y_train, batch_size = 40, epochs = 1200)

# Evaluate the model
scores = model.evaluate(X_test, y_test)
print("\nAccuracy: %.2f%%" % (scores[1]*100))


# Saving Training model using pickle.
#ANN_model = open("Snake_ANN_Model.pkl", "wb")
#pickle.dump(model, ANN_model)
#ANN_model.close()

model.save('SNAKE_A.h5')
