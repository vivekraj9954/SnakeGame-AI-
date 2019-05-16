from keras.models import load_model
import numpy as np

def predict_direction(Left_B,Front_B,Right_B,Cosine_Angle,Collision,Head_x,Head_y,Food_x,Food_y):
    model = load_model('SNAKE.h5')

    #model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

    data = np.array([[Left_B,Front_B,Right_B,Cosine_Angle,Collision,Head_x,Head_y,Food_x,Food_y]])
    get_data = model.predict(data)

    # Here we are getting prediction for each 1,2,3,4
    # the higher prediction indicates the the probable
    # direction to be followed by snake.

    # returning the index position of maximum value.
    a = get_data[0][0]
    b = get_data[0][1]
    c = get_data[0][2]

    value = [a, b, c]
    maxpos = value.index(max(value))
    return(maxpos + 1)

