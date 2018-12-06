import numpy as np

INF = 999999
NEGINF = -999999

#Define size of the border of the gesture data of zeroes
PADDING_FACTOR = 5

def discretize_3D(gesture_list):
    
    cube_x = 29
    cube_y = 29
    cube_z = 29
    #cube size is cube_x + 2*PADDING_FACTOR + 1!!!
    
    cubes = []
    for i in gesture_list:
        gestureData = i['gestureData']
        gestureRange = GestureRange()
        #get maximum and minimum x & y values
        for j in gestureData:
            if(j['x'] > gestureRange.x_max):
                gestureRange.x_max = j['x']
            if(j['x'] < gestureRange.x_min):
                gestureRange.x_min = j['x']
            
            if(j['y'] > gestureRange.y_max):
                gestureRange.y_max = j['y']
            if(j['y'] < gestureRange.y_min):
                gestureRange.y_min = j['y']
                
            if(j['z'] > gestureRange.z_max):
                gestureRange.z_max = j['z']
            if(j['z'] < gestureRange.z_min):
                gestureRange.z_min = j['z']
                
        #get range of x and y data
        x_range = gestureRange.x_max - gestureRange.x_min
        y_range = gestureRange.y_max - gestureRange.y_min
        z_range = gestureRange.z_max - gestureRange.z_min

        #get factor for discretization. Intuition: How many X or Y Values fit in one discretized "step"
        discretization_factor_x  = x_range/cube_x
        discretization_factor_y = y_range/cube_y
        discretization_factor_z = z_range/cube_z
               
        #The bigger factor counts.
        step_max  = max([discretization_factor_x, discretization_factor_y, discretization_factor_z])
        
        #Set data to all 0
        cubeData = np.zeros((cube_x+1,cube_y+1, cube_z+1))
           
        frame_count = 0
        for j in gestureData:
            #zero center data
            x_zeroed = j['x'] - gestureRange.x_min
            y_zeroed = j['y'] - gestureRange.y_min
            z_zeroed = j['z'] - gestureRange.z_min
            
            #get discretized value
            x_discretized = int(x_zeroed / step_max)      
            y_discretized = int(y_zeroed / step_max)
            z_discretized = int(z_zeroed / step_max)
            
            frame_count = frame_count +1
            cubeData[x_discretized,y_discretized,z_discretized] = 1
            
            
        #create padding with zeros
        padded_cube_data = np.lib.pad(cubeData, PADDING_FACTOR, 'minimum')
        
        #wire it all together
        original_cube = []
        original_cube.append(padded_cube_data)
        original_cube.append(i['gestureClass'])
        
        cubes.append(original_cube)
      
    return cubes

def discretize_4D(gesture_list):
    
    cube_x = 29
    cube_y = 29
    cube_z = 29
    #cube size is cube_x + 2*PADDING_FACTOR + 1!!!
    
    cubes = []
    for i in gesture_list:
        gestureData = i['gestureData']
        gestureRange = GestureRange()
        #get maximum and minimum x & y values
        for j in gestureData:
            if(j['x'] > gestureRange.x_max):
                gestureRange.x_max = j['x']
            if(j['x'] < gestureRange.x_min):
                gestureRange.x_min = j['x']
            
            if(j['y'] > gestureRange.y_max):
                gestureRange.y_max = j['y']
            if(j['y'] < gestureRange.y_min):
                gestureRange.y_min = j['y']
                
            if(j['z'] > gestureRange.z_max):
                gestureRange.z_max = j['z']
            if(j['z'] < gestureRange.z_min):
                gestureRange.z_min = j['z']
                
        #get range of x and y data
        x_range = gestureRange.x_max - gestureRange.x_min
        y_range = gestureRange.y_max - gestureRange.y_min
        z_range = gestureRange.z_max - gestureRange.z_min

        #get factor for discretization. Intuition: How many X or Y Values fit in one discretized "step"
        discretization_factor_x  = x_range/cube_x
        discretization_factor_y = y_range/cube_y
        discretization_factor_z = z_range/cube_z
               
        #The bigger factor counts.
        step_max  = max([discretization_factor_x, discretization_factor_y, discretization_factor_z])
        
        #Set data to all 0
        cubeData = np.zeros((cube_x+1,cube_y+1, cube_z+1))
           
        frame_count = 0
        for j in gestureData:
            #zero center data
            x_zeroed = j['x'] - gestureRange.x_min
            y_zeroed = j['y'] - gestureRange.y_min
            z_zeroed = j['z'] - gestureRange.z_min
            
            #get discretized value
            x_discretized = int(x_zeroed / step_max)      
            y_discretized = int(y_zeroed / step_max)
            z_discretized = int(z_zeroed / step_max)
            
            frame_count = frame_count +1
            cubeData[x_discretized,y_discretized,z_discretized] = frame_count
            
            
        #create padding with zeros
        padded_cube_data = np.lib.pad(cubeData, PADDING_FACTOR, 'minimum')
        
        #wire it all together
        original_cube = []
        original_cube.append(padded_cube_data)
        original_cube.append(i['gestureClass'])
        
        cubes.append(original_cube)
      
    return cubes


def discretize_2D(gesture_list):
    
    PADDING_FACTOR = 5
    cube_x = 29
    cube_y = 29
    
    #cube size is cube_y + 2*PADDING_FACTOR + 1!!!
    
    cubes = []
    for i in gesture_list:
        gestureData = i['gestureData']
        gestureRange = GestureRange()
        #get maximum and minimum x & y values
        for j in gestureData:
            if(j['x'] > gestureRange.x_max):
                gestureRange.x_max = j['x']
            if(j['x'] < gestureRange.x_min):
                gestureRange.x_min = j['x']
            
            if(j['y'] > gestureRange.y_max):
                gestureRange.y_max = j['y']
            if(j['y'] < gestureRange.y_min):
                gestureRange.y_min = j['y']
                
        #get range of x and y data
        x_range = gestureRange.x_max - gestureRange.x_min
        y_range = gestureRange.y_max - gestureRange.y_min
        
        #get factor for discretization. Itution: How many X or Y Values fit in one discretized "step"
        discretization_factor_x  = x_range/cube_x
        discretization_factor_y = y_range/cube_y
                
        #The bigger factor counts.
        step_max  = max([discretization_factor_x, discretization_factor_y])
        
        #Set data to all 0
        cubeData = np.zeros((cube_x+1,cube_y+1))
           
        frame_count = 0
        for j in gestureData:
            #zero center data
            x_zeroed = j['x'] - gestureRange.x_min	
            y_zeroed = j['y'] - gestureRange.y_min
            
            #get discretized value
            x_discretized = int(x_zeroed / step_max)      
            y_discretized = int(y_zeroed / step_max)
            
            frame_count = frame_count +1
            cubeData[x_discretized,y_discretized] = 1
            
            
        #create padding with zeros
        padded_cube_data = np.lib.pad(cubeData, PADDING_FACTOR, 'minimum')
        
        #wire it all together
        original_cube = []
        original_cube.append(padded_cube_data)
        original_cube.append(i['gestureClass'])
        
        cubes.append(original_cube)
      
    return cubes

class GestureRange:
    x_min = INF
    x_max = NEGINF
    y_min = INF
    y_max = NEGINF
    z_min = INF
    z_max = NEGINF
    
    
    
