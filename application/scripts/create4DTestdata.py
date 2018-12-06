import random
import copy
import numpy as np

HOLOLENS_FRAMES_PER_SECOND = 60

def create_slowed_gestures(gestuers):
    return_val = []
    
    for j in range(len(gestuers)):
    
        gesture_data = copy.deepcopy(gestuers[j]['gestureData'])
        gesture_class = gestuers[j]['gestureClass']

        for i in range(5*HOLOLENS_FRAMES_PER_SECOND):

            frame_count = len(gesture_data)
            middle_frame_id = frame_count/2
    
            frame_offset = random.uniform(-frame_count*0.2, frame_count*0.2)
            frame_id_to_be_slowed = int(middle_frame_id + frame_offset)
    
            frame_to_be_slowed = gesture_data[frame_id_to_be_slowed]
            next_frame = gesture_data[frame_id_to_be_slowed + 1]
    
            mid_coordinate = {}
    
            mid_coordinate['x'] = (frame_to_be_slowed['x'] + next_frame['x'])/2 
            mid_coordinate['y'] = (frame_to_be_slowed['y'] + next_frame['y'])/2
            mid_coordinate['z'] = (frame_to_be_slowed['z'] + next_frame['z'])/2
    
            gesture_data.insert(frame_id_to_be_slowed +1 , mid_coordinate)
    
        gesture_slowed = {}
        gesture_slowed['gestureClass'] = np.append([0,0,0,0],gesture_class)
        gesture_slowed['gestureData'] = gesture_data
    
        
        gesture_normal = {}
        gesture_normal['gestureClass'] = np.append(gesture_class,[0,0,0,0])    
        gesture_normal['gestureData'] = gestuers[j]['gestureData']    
        
        return_val.append(gesture_slowed)
        return_val.append(gesture_normal)
        
    return return_val
        
