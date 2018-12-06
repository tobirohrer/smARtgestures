import numpy as np
import copy
import scipy
from scipy.ndimage.interpolation import shift

MAX_DISCRETE_PIXEL_LOSS_BY_SHIFT = 10
SHIFT_RATE = 5

def transpose(discrete_gestures):
    print("starting to transpose " + repr(len(discrete_gestures)) + " discrete gestures")
    transposed_discrete_gestures = []
    
    for gesture in discrete_gestures:    
        transposed_gesture = []
        transposed_gesture.append(np.transpose(copy.deepcopy(gesture[0])))
        transposed_gesture.append(gesture[1])
        
        transposed_discrete_gestures.append(gesture)
        transposed_discrete_gestures.append(transposed_gesture)
    
    print("having " + repr(len(transposed_discrete_gestures)) + " gestures now")
    return transposed_discrete_gestures

def transpose_data_experiment(discrete_gestures):
    print("starting to transpose " + repr(len(discrete_gestures)) + " discrete gestures")
    transposed_discrete_gestures = []
    
    for gesture in discrete_gestures:    
        transposed_gesture1 = []
        transposed_gesture1.append(np.transpose(copy.deepcopy(gesture[0]), (1,2,0)))
        transposed_gesture1.append(gesture[1])
        
        transposed_gesture2 = []
        transposed_gesture2.append(np.transpose(copy.deepcopy(gesture[0]), (1,0,2)))
        transposed_gesture2.append(gesture[1])
        
        transposed_gesture3 = []
        transposed_gesture3.append(np.transpose(copy.deepcopy(gesture[0]), (0,2,1)))
        transposed_gesture3.append(gesture[1])
        
        transposed_gesture4 = []
        transposed_gesture4.append(np.transpose(copy.deepcopy(gesture[0]), (2,1,0)))
        transposed_gesture4.append(gesture[1])
        
        transposed_gesture5 = []
        transposed_gesture5.append(np.transpose(copy.deepcopy(gesture[0]), (2,0,1)))
        transposed_gesture5.append(gesture[1])
          
        transposed_discrete_gestures.append(gesture)
        transposed_discrete_gestures.append(transposed_gesture1)
        transposed_discrete_gestures.append(transposed_gesture2)
        transposed_discrete_gestures.append(transposed_gesture3)
        transposed_discrete_gestures.append(transposed_gesture4)
        transposed_discrete_gestures.append(transposed_gesture5)
    
    print("having " + repr(len(transposed_discrete_gestures)) + " gestures now")
    return transposed_discrete_gestures    
    
def flip(discrete_gestures, axis_Index):
    print("starting to flip " + repr(len(discrete_gestures)) + " discrete gestures on axis " + repr(axis_Index))
    flipped_discrete_gestures = []
    
    for gesture in discrete_gestures:    
        flipped_gesture = []
        flipped_gesture.append(np.flip(copy.deepcopy(gesture[0]),axis_Index))
        flipped_gesture.append(gesture[1])
        
        flipped_discrete_gestures.append(gesture)
        flipped_discrete_gestures.append(flipped_gesture)
        
    print("having " + repr(len(flipped_discrete_gestures)) + " gestures now")
    return flipped_discrete_gestures
    

def shift_discrete_gesture(discrete_gestures):
    print("starting to shift " + repr(len(discrete_gestures)) + " gestures")
    augment_shifted_gestures =  []
    for gesture in discrete_gestures:
        augment_shifted_gestures.append(copy.deepcopy(gesture))
        gesture[0] = np.roll(copy.deepcopy(gesture[0]), SHIFT_RATE, axis=1)
        augment_shifted_gestures.append(gesture)
    print("having " + repr(len(augment_shifted_gestures)) + " now")        
    return augment_shifted_gestures
        
def shift_discrete_gesture_down(discrete_gestures):
    print("starting to shift down " + repr(len(discrete_gestures)) + " gestures")
    augment_shifted_gestures =  []
    for gesture in discrete_gestures:
        augment_shifted_gestures.append(copy.deepcopy(gesture))
        gesture[0] = np.roll(copy.deepcopy(gesture[0]), SHIFT_RATE, axis=0) 
        augment_shifted_gestures.append(gesture)
    print("having " + repr(len(augment_shifted_gestures)) + " now")        
    return augment_shifted_gestures

def shift_discrete_gesture_back(discrete_gestures):
    print("starting to shift back " + repr(len(discrete_gestures)) + " gestures")
    augment_shifted_gestures =  []
    for gesture in discrete_gestures:
        augment_shifted_gestures.append(copy.deepcopy(gesture))
        gesture[0] = np.roll(copy.deepcopy(gesture[0]), SHIFT_RATE, axis=2) 
        augment_shifted_gestures.append(gesture)
    print("having " + repr(len(augment_shifted_gestures)) + " now")        
    return augment_shifted_gestures
