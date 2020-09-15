import monkdata as m
import numpy as np
import dtree as d 
import drawtree_qt5 as pyqt
import random
import numpy as np
import matplotlib.pyplot as plt

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


def load_partition(fraction):
    (monk1train, monk1val) = partition(datasets['monk1'], fraction)
    (monk2train, monk2val) = partition(datasets['monk2'], fraction)
    (monk3train, monk3val) = partition(datasets['monk3'], fraction)
    
    partitions = {
    'monk1_p': monk1train,
    'monk1t_p': monk1val,
    'monk2_p': monk2train,
    'monk2t_p': monk2val,
    'monk3_p': monk3train,
    'monk3t_p': monk3val,
    }

    return partitions

def pruneTree(train, validation, acc_desired):
    
    t = d.buildTree(train, m.attributes)
    accuracy = d.check(t, validation)
    accuracy_p = accuracy
    #print("Starting accuracy:" + str(accuracy))
    temp = t
    tt = 0
    while(tt < acc_desired):
        tt+=1
        temp = t
        tlist = d.allPruned(t)    
        accuracy_p = 0
        for i in range(0, len(tlist)):
            #print(i)
            accuracy = d.check(tlist[i], validation)
            #print("Pruned tree no " + str(i) + " accuracy: " + str(accuracy))
            #print(accuracy_p)
            if(accuracy >= accuracy_p):
                accuracy_p = accuracy
                #print("Set new accuracy_p: " + str(accuracy_p))
                t = tlist[i]
                
        #print(str(acc_prev_tree) + " " + str(accuracy_p))

    if(d.check(temp, validation) > d.check(t, validation)):
        t = temp
    """ 
    print(t)
    print("Final accuracy: " + str(d.check(t, validation)))
    pyqt.drawTree(t) 
    """
    return t

#print_prunedTree(partitions['monk1_p'], partitions['monk1t_p'], 0.90)
partitions = load_partition(0.6)

#print_prunedTree(m.monk3, m.monk3test, 0.90) 
#pruneTree(partitions['monk3_p'], partitions['monk3t_p'], 0.80)  

def plot_error(end):
    fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    error = np.zeros((len(fractions), end))
    names=['monk1', 'monk3']
    l_mean = []
    l_var = []
    mean = list()
    for s in range(0,2):
        print(s) 
        for l in range(0, len(fractions)):
            train, validation = partition(datasets[names[s]], fractions[l])
            for i in range(0, end):
                t = pruneTree(train, validation, 5)
                error[l,i] = 1 - d.check(t, validation)
            l_mean.append(np.mean(error[l]))
            l_var.append(np.var(error[l]))
        mean.append(l_mean)
        l_mean = []
    print(mean)

    plt.plot(fractions, mean[0], 'r', label='monk1')
    plt.plot(fractions, mean[1], 'b', label='monk3')
    plt.legend()
    plt.ylabel("error")
    plt.xlabel("fractions")
    plt.show()

plot_error(100) 