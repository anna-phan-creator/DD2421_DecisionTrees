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
    # Create attribute class
    attributes = {
        'a1': m.attributes[0],
        'a2': m.attributes[1],
        'a3': m.attributes[2],
        'a4': m.attributes[3],
        'a5': m.attributes[4],
        'a6': m.attributes[5],
    }

    return attributes

def print_average_gain(datasets, attributes):
    # Calculate average gain for datasets
    print("Information gain")
    for data in datasets:
        print("For " + data + " the:")
        for attribute in attributes:
            print("information gain for " + attribute + " was: " + str(averageGain(datasets[data], attributes[attribute])))
   
def print_entropy(datasets):
    # Calculate entropy for datasets
    for dataset in datasets:
        print("Entropy of " + dataset + ": "  + str(entropy(datasets[dataset])))



datasets = load_datasets()
attributes = load_attributes()
#print_average_gain(datasets, attributes)
print_entropy(datasets)


 
# Based on the results of information gain (use the highest) for each dataset
# monk1 use attribute 5
splits = {
    'm1split1': select(datasets['monk1'], attributes['a5'], 1),
    'm1split2': select(datasets['monk1'], attributes['a5'], 2),
    'm1split3': select(datasets['monk1'], attributes['a5'], 3),
    'm1split4': select(datasets['monk1'], attributes['a5'], 4),
    'm2split1': select(datasets['monk2'], attributes['a5'], 1),
    'm2split2': select(datasets['monk2'], attributes['a5'], 2),
    'm2split3': select(datasets['monk2'], attributes['a5'], 3),
    'm2split4': select(datasets['monk2'], attributes['a5'], 4),
}

print_entropy(splits)
# monk2 use attribute 5
# monk3 use attribute 2





