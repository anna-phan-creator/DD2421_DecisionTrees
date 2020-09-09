import monkdata as m
import numpy as np
from dtree import * 

# Load monk datasets
def load_datasets():
    data = {
        'monk1': m.monk1,
        'monk1t': m.monk1test,
        'monk2': m.monk2,
        'monk2t': m.monk2test,
        'monk3': m.monk3,
        'monk3t': m.monk3test
    }
    
    return data

def load_attributes():
    # Calculate entropy for datasets
    print("Entropy of monk 1: " + str(entropy(data['monk1'])))
    print("Entropy of monk 2: " + str(entropy(data['monk2'])))
    print("Entropy of monk 3: " + str(entropy(data['monk3'])))

    # Create attribute class
    attributes = {
        'a1': m.attributes[0],
        'a2': m.attributes[1],
        'a3': m.attributes[2],
        'a4': m.attributes[3],
        'a5': m.attributes[4],
        'a6': m.attributes[5],
    }

    print("Information gain")
    for dataset in data:
        print(dataset)
        for attribute in attributes:
            print(attribute + ": " + str(averageGain(data[dataset], attributes[attribute])))
    
    return attributes

data = load_datasets()
attributes = load_attributes()

