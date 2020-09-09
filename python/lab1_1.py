import monkdata as m
import numpy as np
from dtree import * 

# Load monk datasets
def load_datasets():
    monk1 = m.monk1
    monk1test = m.monk1test
    monk2 = m.monk2
    monk2test = m.monk2test
    monk3 = m.monk3
    monk3test = m.monk3test

    data = {
        'monk1': monk1,
        'monk1t': monk1test,
        'monk2': monk2,
        'monk2t': monk2test,
        'monk3': monk3,
        'monk3t': monk3test
    }
    
    return data

data = load_datasets()

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
