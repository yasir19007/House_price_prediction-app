import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)



def get_location_names():
    try:
        return __locations
    except:
        print("Locations is not loaded")

def load_saved_artifacts():
    print("LOADING SAVED ARTIFACTS ...start")
    global  __data_columns
    global __locations
    global __model

    with open("artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
        print("Data columns loaded successfully.")

    with open('artifacts/house_price_predictions.pickle', 'rb') as f:
        __model = pickle.load(f)
    print("Model loaded successfully.")
    print("LOADING SAVED ARTIFACTS...done")


# if __name__ == '__main__':
#     load_saved_artifacts()
#     print(get_location_names())

#     print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
#     print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))