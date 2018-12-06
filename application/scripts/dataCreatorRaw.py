import random
import copy
import numpy as np

STRETCH_RATE = 0.65

def jitter_data(gestures, JITTER_RATE = 0.0025): #~1,25% of range of input data.
    for gesture in gestures:
        for coordinate in gesture["gestureData"]:
            x_jitter = random.uniform(-JITTER_RATE, JITTER_RATE)
            coordinate["x"] = coordinate["x"] + x_jitter
            y_jitter = random.uniform(-JITTER_RATE, JITTER_RATE)
            coordinate["y"] = coordinate["y"] + y_jitter
            z_jitter = random.uniform(-JITTER_RATE, JITTER_RATE)
            coordinate["z"] = coordinate["z"] + z_jitter
    return gestures

def compress_x(gestures):
    for gesture in gestures:
        for coordinate in gesture["gestureData"]:
            coordinate["x"] = coordinate["x"] * STRETCH_RATE    
    return gestures

def compress_y(gestures):
    for gesture in gestures:
        for coordinate in gesture["gestureData"]:
            coordinate["y"] = coordinate["y"] * STRETCH_RATE    
    return gestures

def compress_z(gestures):
    for gesture in gestures:
        for coordinate in gesture["gestureData"]:
            coordinate["z"] = coordinate["z"] * STRETCH_RATE    
    return gestures

def create_delayed_gestures(gestures):
    #bla
    print("test")
    

def get_augmented_input_data3D(gesture_list):
    augment_data = copy.deepcopy(gesture_list) + compress_x(copy.deepcopy(gesture_list)) + compress_y(copy.deepcopy(gesture_list)) + compress_z(copy.deepcopy(gesture_list))
    augment_data =  augment_data + jitter_data(copy.deepcopy(augment_data))
    return augment_data

def get_augmented_input_data2D(gesture_list):
    augment_data = copy.deepcopy(gesture_list) + compress_x(copy.deepcopy(gesture_list)) + compress_y(copy.deepcopy(gesture_list))
    augment_data =  augment_data + jitter_data(copy.deepcopy(augment_data))
    return augment_data

#Function for the max jitter experiment
def get_max_jittered_data2D(gesture_list):
    return jitter_data(copy.deepcopy(gesture_list), 1.0)

