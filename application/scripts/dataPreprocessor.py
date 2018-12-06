import math

#there should not be more distance than MAX_COORD_DISTANCE between two coordinates of the gesture! difference between max and min values of all coordinates of all gestures is approx. 0.2 !
MAX_COORD_DISTANCE = 0.01

#remove gestures with more than 200 or less then 50 coordinates per gesture
def input_data_cleanup(gesture_list):
    cleanup_count = 0
    print("starting to cleanup gesture Data...")
    data_count = 0
    for gesture in gesture_list:
        gesture_data = gesture['gestureData']
        data_count += len(gesture_data)
        if(len(gesture_data) > 200 or len(gesture_data) < 50):
            gesture_list.remove(gesture)
            cleanup_count += 1
    print("done cleaning up. Removed " + repr(cleanup_count) + " gestures")
    return gesture_list

def repair_gesture_data(gesture_list):
    closed_gap_count = 0
    print("starting to close gaps in gesture coordinate data...")
    for gesture in gesture_list:
        gesture_data = gesture['gestureData']
        
        repeat = True
      
        #Repeat as long as there are no gaps left. Just because there is a new coordinate between the old gap doesnt mean the gap is fixed!
        while repeat==True:
            repeat = False
                     
            for i in range(len(gesture_data)-1):
                from_coordinate = Point()
                from_coordinate.x = gesture_data[i]['x']
                from_coordinate.y = gesture_data[i]['y']
                from_coordinate.z = gesture_data[i]['z']
                
                to_coordinate = Point()
                to_coordinate.x = gesture_data[i+1]['x']
                to_coordinate.y = gesture_data[i+1]['y']
                to_coordinate.z = gesture_data[i+1]['z']
                
                distance = math.sqrt(math.pow(from_coordinate.x - to_coordinate.x, 2) + math.pow(from_coordinate.y - to_coordinate.y, 2) + math.pow(from_coordinate.z - to_coordinate.z, 2))
                
                if(distance > MAX_COORD_DISTANCE):
                    repeat = True
                    closed_gap_count += 1
                    mid_coordinate = Point()
                    mid_coordinate.x = (from_coordinate.x + to_coordinate.x)/2 
                    mid_coordinate.y = (from_coordinate.y + to_coordinate.y)/2
                    mid_coordinate.z = (from_coordinate.z + to_coordinate.z)/2
                    
                    augment_gesture_coordinate = {}
                    augment_gesture_coordinate['x'] = mid_coordinate.x
                    augment_gesture_coordinate['y'] = mid_coordinate.y
                    augment_gesture_coordinate['z'] = mid_coordinate.z
                    
                    gesture_data.insert(i+1, augment_gesture_coordinate) 

    print("done closing gaps... Added " + repr(closed_gap_count) + " coordinates")
    return gesture_list

class Point:
    x = 0
    y = 0
    z = 0