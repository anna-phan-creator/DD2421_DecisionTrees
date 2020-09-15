import monkdata as m
import numpy as np
import dtree as d 
import drawtree_qt5 as pyqt
import random

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
            print("information gain for " + attribute + " was: " + str(d.averageGain(datasets[data], attributes[attribute])))
   
def print_entropy(datasets):
    # Calculate entropy for datasets
    for dataset in datasets:
        print("Entropy of " + dataset + ": "  + str(d.entropy(datasets[dataset])))

datasets = load_datasets()
attributes = load_attributes()
#print_average_gain(datasets, attributes)
#print_entropy(datasets)

# Based on the results of information gain (use the highest) for each dataset
# monk1 use attribute 5
# monk2 use attribute 5
# monk3 use attribute 2
splits = {
    'm1split1': d.select(datasets['monk1'], attributes['a5'], 1),
    'm1split2': d.select(datasets['monk1'], attributes['a5'], 2),
    'm1split3': d.select(datasets['monk1'], attributes['a5'], 3),
    'm1split4': d.select(datasets['monk1'], attributes['a5'], 4),
    'm2split1': d.select(datasets['monk2'], attributes['a5'], 1),
    'm2split2': d.select(datasets['monk2'], attributes['a5'], 2),
    'm2split3': d.select(datasets['monk2'], attributes['a5'], 3),
    'm2split4': d.select(datasets['monk2'], attributes['a5'], 4),
    'm3split1': d.select(datasets['monk3'], attributes['a2'], 1),
    'm3split2': d.select(datasets['monk3'], attributes['a2'], 2),
    'm3split3': d.select(datasets['monk3'], attributes['a2'], 3),
}
#print_entropy(splits)

# Assignment 5
def a5():
    t1 = d.buildTree(m.monk1, m.attributes)
    pyqt.drawTree(t1)
    print(d.check(t1, m.monk1test))
    t2 = d.buildTree(m.monk2, m.attributes)
    pyqt.drawTree(t2)
    print(d.check(t2, m.monk2test))
    t3 = d.buildTree(m.monk3, m.attributes)
    pyqt.drawTree(t3)
    print(d.check(t3, m.monk3test))

# Assignment 6
# Shuffle dataset, partition from start to breakpoint and breakpoint to end
def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


def load_partition():
    (monk1train, monk1val) = partition(datasets['monk1']+datasets['monk1t'], 0.6)
    (monk2train, monk2val) = partition(datasets['monk2']+datasets['monk2t'], 0.6)
    (monk3train, monk3val) = partition(datasets['monk3']+datasets['monk3t'], 0.6)
    
    partitions = {
    'monk1_p': monk1train,
    'monk1t_p': monk1val,
    'monk2_p': monk2train,
    'monk2t_p': monk2val,
    'monk3_p': monk3train,
    'monk3t_p': monk3val,
    }

    return partitions

partitions = load_partition()

"""
while acc > 0.86
    tlist = d.allpruned(tlist[save])
    for i in range len tlist
        acc = check(tlist[i], monk1t_p)
        if acc > acc_previous
            acc_previous = acc
            save = i
            print(acc_previous)       
"""

t = d.buildTree(partitions['monk1_p'], m.attributes)
e = d.check(t, partitions['monk1t_p'])

tlist = d.allPruned(t)

def print_prunedTree(train, validation):
    t = d.buildTree(train, m.attributes)
    accuracy = d.check(t, validation)
    accuracy_p = accuracy
    acc_prev_tree = accuracy_p
    print("Starting accuracy:" + str(accuracy))
    
    while(accuracy_p >= acc_prev_tree):
        tlist = d.allPruned(t)
        acc_prev_tree = accuracy_p
        for i in range(0, len(tlist)):
            print(i)
            accuracy = d.check(t, validation)
            print("Pruned tree no" + i + "accuracy:" + str(accuracy))
            #print(accuracy_p)
            if(accuracy >= accuracy_p):
                accuracy_p = accuracy
                print("Set new accuracy_p:" + str(accuracy_p)
                #t = tlist[i]
            else:
                accuracy_p = accuracy
        #print(str(acc_prev_tree) + " " + str(accuracy_p))
        
    print(t)
    pyqt.drawTree(t)


t = d.buildTree(partitions['monk1_p'], m.attributes)
print(d.check(t, partitions['monk1t_p']))
tlist = d.allPruned(t)
for i in range(0, len(tlist)):
    print(d.check(tlist[i], partitions['monk1t_p']))
print("--------------")
print_prunedTree(partitions['monk1_p'], partitions['monk1t_p'])

#print_prunedTree(partitions['monk1_p'], partitions['monk1t_p'])       
#print_prunedTree(partitions['monk1_p'], partitions['monk1t_p'])       
#print_prunedTree(partitions['monk1_p'], partitions['monk1t_p'])       
#print_prunedTree(partitions['monk1_p'], partitions['monk1t_p'])       
#print_prunedTree(partitions['monk1_p'], partitions['monk1t_p'])       
#print_prunedTree(partitions['monk1_p'], partitions['monk1t_p'])       