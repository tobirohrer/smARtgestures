import json
import numpy as np
import os
import math
import dataCreatorRaw
import dataCreatorDiscrete
import dataPreprocessor
import dataDiscretizer
import create4DTestdata
import copy

def read_data_from_file(data_path):
    with open(data_path) as data_file:    
        data = json.load(data_file)
        gestureList = data["gestureList"]
        print("imported data of " + repr(len(gestureList)) + " gestures")
        return gestureList
 
def get_discrete2D_data(gesture_list, preprocess, augment):
    
    if(preprocess == True):
        gesture_list = dataPreprocessor.input_data_cleanup(gesture_list) 
        gesture_list = dataPreprocessor.repair_gesture_data(gesture_list)
    
    if(augment == True):
        gesture_list = dataCreatorRaw.get_augmented_input_data2D(gesture_list)
        print("augumented input data "  + repr(len(gesture_list)))
    

    discrete_gestures = dataDiscretizer.discretize_2D(gesture_list)
            
    if(augment == True):
        discrete_gestures = dataCreatorDiscrete.transpose(discrete_gestures)
        discrete_gestures = dataCreatorDiscrete.flip(discrete_gestures,0)
        discrete_gestures = dataCreatorDiscrete.flip(discrete_gestures,1)
        discrete_gestures = dataCreatorDiscrete.shift_discrete_gesture(discrete_gestures)
        discrete_gestures = dataCreatorDiscrete.shift_discrete_gesture_down(discrete_gestures)
    
    print(" ")
    return discrete_gestures

def get_discrete3D_data(gesture_list, preprocess, augment):
    
    if(preprocess == True):
        gesture_list = dataPreprocessor.input_data_cleanup(gesture_list) 
        gesture_list = dataPreprocessor.repair_gesture_data(gesture_list)
    
    if(augment == True):
        gesture_list = dataCreatorRaw.get_augmented_input_data3D(gesture_list)
        print("augumented input data "  + repr(len(gesture_list)))
        
    discrete_gestures = dataDiscretizer.discretize_3D(gesture_list)
    
    if(augment == True):
        discrete_gestures = dataCreatorDiscrete.transpose(discrete_gestures)
        discrete_gestures = dataCreatorDiscrete.flip(discrete_gestures,0)
        discrete_gestures = dataCreatorDiscrete.flip(discrete_gestures,1)
        discrete_gestures = dataCreatorDiscrete.flip(discrete_gestures,2)
        discrete_gestures = dataCreatorDiscrete.shift_discrete_gesture(discrete_gestures)
        discrete_gestures = dataCreatorDiscrete.shift_discrete_gesture_down(discrete_gestures)
        discrete_gestures = dataCreatorDiscrete.shift_discrete_gesture_back(discrete_gestures)
    
    print(" ")
    return compress_3D(discrete_gestures)

def get_discrete4D_data(gesture_list, preprocess, augment):
    
    if(preprocess == True):
        gesture_list = dataPreprocessor.input_data_cleanup(gesture_list) 
        gesture_list = dataPreprocessor.repair_gesture_data(gesture_list)
    
    if(augment == True):
        gesture_list = dataCreatorRaw.get_augmented_input_data3D(gesture_list)
        print("augumented input data "  + repr(len(gesture_list)))
        
    gesture_list = create4DTestdata.create_slowed_gestures(gesture_list)
    print("slowed down gestures... its " + repr(len(gesture_list)) + " now")
        
    discrete_gestures = dataDiscretizer.discretize_4D(gesture_list)
    
    if(augment == True):
        discrete_gestures = dataCreatorDiscrete.transpose(discrete_gestures)
        discrete_gestures = dataCreatorDiscrete.flip(discrete_gestures,0)
        discrete_gestures = dataCreatorDiscrete.flip(discrete_gestures,1)
        discrete_gestures = dataCreatorDiscrete.flip(discrete_gestures,2)
        discrete_gestures = dataCreatorDiscrete.shift_discrete_gesture(discrete_gestures)
        discrete_gestures = dataCreatorDiscrete.shift_discrete_gesture_down(discrete_gestures)
        discrete_gestures = dataCreatorDiscrete.shift_discrete_gesture_back(discrete_gestures)
    
    print(" ")
    return compress_3D(discrete_gestures)


def get_max_jittered_data(gesture_list):

    gesture_list = dataPreprocessor.input_data_cleanup(gesture_list) 
    gesture_list = dataPreprocessor.repair_gesture_data(gesture_list)
    gesture_list = dataCreatorRaw.get_max_jittered_data2D(gesture_list)
        
    discrete_gestures = dataDiscretizer.discretize_2D(gesture_list)
    print(" ")
    return discrete_gestures

def compress_3D(discrete_gestures):
    print("compressing...")
    discrete_gesture_length = len(discrete_gestures)
    compressed_discrete_gesture_list = []
    for j in range (discrete_gesture_length):
        compressed_discrete_gesture = []
        nonzero_indexes = discrete_gestures[j][0].nonzero()
        nonzero_element_count = len(nonzero_indexes[0])
        compressed_data = []
        
        for i in range(nonzero_element_count):
            compressed_data_index = []
            compressed_data_element = []
            compressed_data_index.append(nonzero_indexes[0][i])
            compressed_data_index.append(nonzero_indexes[1][i])
            compressed_data_index.append(nonzero_indexes[2][i])
            compressed_data_element.append(compressed_data_index)
            compressed_data_element.append(discrete_gestures[j][0][compressed_data_index[0]][compressed_data_index[1]][compressed_data_index[2]])
            compressed_data.append(compressed_data_element)
            
        compressed_discrete_gesture.append(compressed_data)
        compressed_discrete_gesture.append(discrete_gestures[j][1])
        compressed_discrete_gesture_list.append(compressed_discrete_gesture)

    return compressed_discrete_gesture_list

def decompress_3D(compressed_gestures):
    compressed_gestures_length = len(compressed_gestures)
    decompressed_data = []
    for j in range(compressed_gestures_length):
        cube_data = np.zeros((40,40,40))
        compressed_data_length = len(compressed_gestures[j][0])
        
        for i in range(compressed_data_length):
            compressed_gestures[j][0][i][0][0]
            cube_data[compressed_gestures[j][0][i][0][0], compressed_gestures[j][0][i][0][1], compressed_gestures[j][0][i][0][2]] = compressed_gestures[j][0][i][1]
        
        gesture = []
        gesture.append(cube_data)
        gesture.append(compressed_gestures[j][1])
        decompressed_data.append(gesture)
        
    return decompressed_data



