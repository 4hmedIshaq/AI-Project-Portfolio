   

#Trial 1 
 #import math
def reward_function(params):
       
    # Read input parameters
    #waypoints = params['waypoints']
    #closest_waypoints = ['closest_waypoints']
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    is_offtrack = ['is_offtrack']

       # Give a very low reward by default
    reward = 1e-3

    #next_point = waypoints[closest_waypoints[1]]
    #prev_point = waypoints[closest_waypoints[0]]
    "distance from center of track"
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward+= 5
    elif distance_from_center <= marker_2:
        reward+= 3
    elif distance_from_center <= marker_3:
        reward+= 1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    "All wheels on track ?"
    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward+= 3.0 and  is_offtrack == False
    elif is_offtrack == True and all_wheels_on_track== False:
        reward = reward - 4.0
    
    "Speed"
    MIN_SPEED = 0.5
    MAX_SPEED = 3.0

    if speed <= MIN_SPEED:
        reward += 1e-3  # Minimum reward for very low speed
    else:
        # Linearly scale the reward based on speed
        # Reward scales from 0.5 to 4.0 mph
        speed_reward = (speed - MIN_SPEED) / (MAX_SPEED - MIN_SPEED)  # This will give a value between 0 and 1
        reward += speed_reward * 3  # Max reward of 4 when speed is 4.0 mph

    return float(reward)



    #Trial 2
        #import math
def reward_function(params):
       
    # Read input parameters
    #waypoints = params['waypoints']
    #closest_waypoints = ['closest_waypoints']
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    is_offtrack = ['is_offtrack']

       # Give a very low reward by default
    reward = 1e-3

    #next_point = waypoints[closest_waypoints[1]]
    #prev_point = waypoints[closest_waypoints[0]]
    "distance from center of track"
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward+= 5
    elif distance_from_center <= marker_2:
        reward+= 3
    elif distance_from_center <= marker_3:
        reward+= 1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    "All wheels on track ?"
    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward+= 3.0 and  is_offtrack == False
    elif is_offtrack == True:
        reward = reward - 10
    
    "Speed"
    MIN_SPEED = 0.5
    MAX_SPEED = 3.0

    if speed <= MIN_SPEED:
        reward += 1e-3  # Minimum reward for very low speed
    else:
        # Linearly scale the reward based on speed
        # Reward scales from 0.5 to 3.0 mph
        speed_reward = (speed - MIN_SPEED) / (MAX_SPEED - MIN_SPEED)  # This will give a value between 0 and 1
        reward += speed_reward * 3  # Max reward of 3 when speed is 3.0 mph

    return float(reward)







#Trial 3-1 

    #import math
def reward_function(params):
       
    # Read input parameters
    #waypoints = params['waypoints']
    #closest_waypoints = ['closest_waypoints']
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    is_offtrack = ['is_offtrack']

       # Give a very low reward by default
    reward = 1e-3

    #next_point = waypoints[closest_waypoints[1]]
    #prev_point = waypoints[closest_waypoints[0]]
    "distance from center of track"
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward+=5
    elif distance_from_center <= marker_2:
        reward+=2
    elif distance_from_center <= marker_3:
        reward+= 0.2
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    "All wheels on track ?"
    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward+= 3.0 and  is_offtrack == False
    elif is_offtrack == True:
        reward += 1e-3  #Try with this next
    
    "Speed"
    MIN_SPEED = 0.5
    MAX_SPEED = 3.0

    if speed <= MIN_SPEED:
        reward += 1e-3  # Minimum reward for very low speed
    else:
        # Linearly scale the reward based on speed
        # Reward scales from 0.5 to 3.0 mph
        speed_reward = (speed - MIN_SPEED) / (MAX_SPEED - MIN_SPEED)  # This will give a value between 0 and 1
        reward += speed_reward * 3  # Max reward of 3 when speed is 3.0 mph

    return float(reward)






#Trial 4
    #import math
def reward_function(params):
       
    # Read input parameters
    #waypoints = params['waypoints']
    #closest_waypoints = params['closest_waypoints']
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    is_offtrack = ['is_offtrack']
    steps = params['steps']
    progress = params['progress']

       # Give a very low reward by default
    reward = 1e-3
    "waypoints"
    
    # waypionts  isnt working right now. trying to see what needs to be change.
    
    "Steps and progress"
    NUM_STEPS = 300

    # Initialize the reward with typical value
    reward = 0.5
    # Give additional reward if the car pass every 100 steps faster than expected
    if (steps % 100) == 0 and progress > (steps / NUM_STEPS) * 100 :
        reward += 10.0

    "distance from center of track"
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward+=5
    elif distance_from_center <= marker_2:
        reward+=2
    elif distance_from_center <= marker_3:
        reward+= 0.2
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    "All wheels on track ?"
    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward+= 3.0 and  is_offtrack == False
    elif is_offtrack == True:
        reward += 1e-3  #Try with this next
    
    "Speed"
    MIN_SPEED = 0.5
    MAX_SPEED = 3.0

    if speed <= MIN_SPEED:
        reward += 1e-3  # Minimum reward for very low speed
    else:
        # Linearly scale the reward based on speed
        # Reward scales from 0.5 to 3.0 mph
        speed_reward = (speed - MIN_SPEED) / (MAX_SPEED - MIN_SPEED)  # This will give a value between 0 and 1
        reward += speed_reward * 3  # Max reward of 3 when speed is 3.0 mph

    return float(reward)









#MK1 with waypoints
#import math
def reward_function(params):
       
    # Read input parameters
    #waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    is_offtrack = ['is_offtrack']
    is_left_of_center = params["is_left_of_center"]
    steps = params['steps']
    progress = params['progress']

    # Give a very low reward by default
    reward = 1
    "waypoints"    
    center_variance = distance_from_center / track_width
    #racing line
    left_lane = [10,11,12,13,14,15,16,17,18,19,84,85,86,87,88,89,90,91,92,119,120,121,122,123,124,125,126,127,128,129,146,147,148,149,150,151,152,153,154,155,156,184,185,186,187,188,189,190,201,202,203,204,205,206]#Fill in the waypoints for left lane
    
    center_lane = [0,1,2,3,4,5,6,7,8,9,20,21,22,23,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,130,131,132,133,144,145,157,158,159,160,160,177,178,179,180,181,182,183,191,192,193,194,195,195,196,197,198,199,200,207,208,209,210,211,21,213,214,215,216,217,218,219,220,221,222]#Fill in the waypoints for center lane
    
    right_lane = [24,25,26,27,28,46,47,48,49,50,51,52,53,134,135,139,140,141,142,143,161,162,163,164,165,166,167,168,169,170,171,173,174,175,176]#Fill in the waypoints for right lane
    #Speed
    fast = [1,2,3,4,5,6,7,8,9,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,54,55,56,57,58,59,60,61,62,63,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,15,157,158,159,177,178,179,180,181,182,183,191,192,193,194,195,195,196,197,207,208,209,210,211,21,213,214,215,216,217,218,219,220,221,222,223]#Fill in the waypoints, speed = 3m/s
    slow = [10,11,12,13,14,16,17,18,19,44,46,47,48,49,50,51,52,53,64,65,66,67,68,84,85,86,87,88,89,90,91,92,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,184,185,186,187,188,189,190,198,199,200,201,202,203,204,205,206,212]#Fill in the waypoints, 1m/s


    "All wheels on track ?"
    # Give a high reward if no wheels go off the track and
    # The agent is somewhere in between the track borders
    if all_wheels_on_track :
        reward+= 3.0 and  is_offtrack == False
    elif is_offtrack == True:
        reward += 1e-3
    

    if closest_waypoints[1] in left_lane and is_left_of_center:
        reward += 10
    elif closest_waypoints[1] in right_lane and not is_left_of_center:
        reward += 10
    elif closest_waypoints[1] in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10

    NUM_STEPS = 200

    expected_progress = (steps / NUM_STEPS) * 100
    if steps % 100 == 0:
        if progress > expected_progress:
            reward += 10.0 * ((progress - expected_progress) / 100)  # scaled bonus based on how far ahead
        else:
            reward = 1e-3 * (1 + (expected_progress - progress) / 100)  # scaled penalty
    else:
        reward = 0.1  

    #Speed 
    if closest_waypoints[1] in fast:
        if speed == 2 :
            reward += 10
        else:
            reward -= 10
    elif closest_waypoints[1] in slow:
        if speed <=1 :
            reward += 10
        else:
            reward -= 10
    
    return float(reward)



#MK1 optimized

#import math
def reward_function(params):
       
    # Read input parameters
    #waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    is_offtrack = ['is_offtrack']
    is_left_of_center = params["is_left_of_center"]
    steps = params['steps']
    progress = params['progress']

    # Give a very low reward by default
    reward = 1
    "waypoints"    
    center_variance = distance_from_center / track_width
    #racing line
    left_lane = [10,11,12,13,14,15,16,17,18,19,84,85,86,87,88,89,90,91,92,119,120,121,122,123,124,125,126,127,128,129,146,147,148,149,150,151,152,153,154,155,156,184,185,186,187,188,189,190,201,202,203,204,205,206]#Fill in the waypoints for left lane
    
    center_lane = [0,1,2,3,4,5,6,7,8,9,20,21,22,23,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,130,131,132,133,144,145,157,158,159,160,160,177,178,179,180,181,182,183,191,192,193,194,195,195,196,197,198,199,200,207,208,209,210,211,21,213,214,215,216,217,218,219,220,221,222]#Fill in the waypoints for center lane
    
    right_lane = [24,25,26,27,28,46,47,48,49,50,51,52,53,134,135,139,140,141,142,143,161,162,163,164,165,166,167,168,169,170,171,173,174,175,176]#Fill in the waypoints for right lane
    #Speed
    fast = [1,2,3,4,5,6,7,8,9,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,54,55,56,57,58,59,60,61,62,63,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,15,157,158,159,177,178,179,180,181,182,183,191,192,193,194,195,195,196,197,207,208,209,210,211,21,213,214,215,216,217,218,219,220,221,222,223]#Fill in the waypoints, speed = 3m/s
    slow = [10,11,12,13,14,16,17,18,19,44,46,47,48,49,50,51,52,53,64,65,66,67,68,84,85,86,87,88,89,90,91,92,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,184,185,186,187,188,189,190,198,199,200,201,202,203,204,205,206,212]#Fill in the waypoints, 1m/s


    "All wheels on track ?"
    # Give a high reward if no wheels go off the track and
    # The agent is somewhere in between the track borders
    if all_wheels_on_track :
        reward+= 3.0 and  is_offtrack == False
    elif is_offtrack == True:
        reward += 1e-3
    

    if closest_waypoints[1] in left_lane and is_left_of_center:
        reward += 10
    elif closest_waypoints[1] in right_lane and not is_left_of_center:
        reward += 10
    elif closest_waypoints[1] in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10

    NUM_STEPS = 200

    expected_progress = (steps / NUM_STEPS) * 100
    if steps % 100 == 0:
        if progress > expected_progress:
            reward += 10.0 * ((progress - expected_progress) / 100)  # scaled bonus based on how far ahead
        else:
            reward = 1e-3 * (1 + (expected_progress - progress) / 100)  # scaled penalty
    else:
        reward = 0.1  

    #Speed 
    if closest_waypoints[1] in fast:
        if speed == 2 :
            reward += 10
        else:
            reward -= 10
    elif closest_waypoints[1] in slow:
        if speed <=1 :
            reward += 10
        else:
            reward -= 10
    
    return float(reward)






#MK2

def reward_function(params):
       
    # Read input parameters
    #waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    #is_offtrack = ['is_offtrack']
    is_left_of_center = params["is_left_of_center"]
    #steps = params['steps']
    progress = params['progress']

    # Give a very low reward by default
    reward = 1
    "waypoints"    
    center_variance = distance_from_center / track_width
    #racing line
    left_lane = [10,11,12,13,14,15,16,17,18,19,84,85,86,87,88,89,90,91,92,119,120,121,122,123,124,125,126,127,128,129,146,147,148,149,150,151,152,153,154,155,156,184,185,186,187,188,189,190,201,202,203,204,205,206]#Fill in the waypoints for left lane
    
    center_lane = [0,1,2,3,4,5,6,7,8,9,20,21,22,23,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,130,131,132,133,144,145,157,158,159,160,160,177,178,179,180,181,182,183,191,192,193,194,195,195,196,197,198,199,200,207,208,209,210,211,21,213,214,215,216,217,218,219,220,221,222]#Fill in the waypoints for center lane
    
    right_lane = [24,25,26,27,28,46,47,48,49,50,51,52,53,134,135,139,140,141,142,143,161,162,163,164,165,166,167,168,169,170,171,173,174,175,176]#Fill in the waypoints for right lane
    #Speed
    fast = [1,2,3,4,5,6,7,8,9,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,54,55,56,57,58,59,60,61,62,63,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,15,157,158,159,177,178,179,180,181,182,183,191,192,193,194,195,195,196,197,207,208,209,210,211,21,213,214,215,216,217,218,219,220,221,222,223]#Fill in the waypoints, speed = 3m/s
    slow = [10,11,12,13,14,16,17,18,19,44,46,47,48,49,50,51,52,53,64,65,66,67,68,84,85,86,87,88,89,90,91,92,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,184,185,186,187,188,189,190,198,199,200,201,202,203,204,205,206,212]#Fill in the waypoints, 1m/s

    if all_wheels_on_track and progress:
        reward +10
    if closest_waypoints[1] in left_lane and is_left_of_center:
        reward += 10
    elif closest_waypoints[1] in right_lane and not is_left_of_center:
        reward += 10
    elif closest_waypoints[1] in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10

    #Speed 
    if closest_waypoints[1] in fast:
        if speed == 2 :
            reward += 10
        else:
            reward -= 10
    elif closest_waypoints[1] in slow:
        if speed <=1 :
            reward += 10
        else:
            reward -= 10
    
    return float(reward)




#MK3
import math
def reward_function(params):
       
    # Read input parameters
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    is_offtrack = ['is_offtrack']
    is_left_of_center = params["is_left_of_center"]
    heading= params['heading']
    progress = params['progress']

    # Give a very low reward by default
    reward = 30
    "waypoints"    
    center_variance = distance_from_center / track_width
    #racing line
    left_lane = [10,11,12,13,14,15,16,17,18,19,84,85,86,87,88,89,90,91,92,119,120,121,122,123,124,125,126,127,128,129,146,147,148,149,150,151,152,153,154,155,156,184,185,186,187,188,189,190,201,202,203,204,205,206]#Fill in the waypoints for left lane
    
    center_lane = [0,1,2,3,4,5,6,7,8,9,20,21,22,23,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,130,131,132,133,144,145,157,158,159,160,160,177,178,179,180,181,182,183,191,192,193,194,195,195,196,197,198,199,200,207,208,209,210,211,21,213,214,215,216,217,218,219,220,221,222]#Fill in the waypoints for center lane
    
    right_lane = [24,25,26,27,28,46,47,48,49,50,51,52,53,134,135,139,140,141,142,143,161,162,163,164,165,166,167,168,169,170,171,173,174,175,176]#Fill in the waypoints for right lane
    #Speed
    fast = [1,2,3,4,5,6,7,8,9,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,54,55,56,57,58,59,60,61,62,63,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,15,157,158,159,177,178,179,180,181,182,183,191,192,193,194,195,195,196,197,207,208,209,210,211,21,213,214,215,216,217,218,219,220,221,222,223]#Fill in the waypoints, speed = 2m/s
    slow = [10,11,12,13,14,16,17,18,19,44,46,47,48,49,50,51,52,53,64,65,66,67,68,84,85,86,87,88,89,90,91,92,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,184,185,186,187,188,189,190,198,199,200,201,202,203,204,205,206,212]#Fill in the waypoints, 1m/s

    if all_wheels_on_track and progress:
        reward +10 and is_offtrack ==False
    else:
        reward -= 5 and is_offtrack ==True
    if closest_waypoints[1] in left_lane and is_left_of_center:
        reward += 10
    elif closest_waypoints[1] in right_lane and not is_left_of_center:
        reward += 10
    elif closest_waypoints[1] in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10
        
        
        


    # Heading penalty/reward
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the track direction in radians and convert to degrees
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)
    
    # Calculate the difference between the track direction and the car's heading
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize if the car is not facing the correct direction
    if direction_diff > 30:  # Threshold for penalizing
        reward -= 10
    else:
        reward += 10

    #Speed 
    if closest_waypoints[1] in fast:
        if speed == 2 :
            reward += 10
        else:
            reward -= 10
    elif closest_waypoints[1] in slow:
        if speed <=1 :
            reward += 10
        else:
            reward -= 10
    
    return float(reward)






#MK5

import math
def reward_function(params):
       
    # Read input parameters
    waypoints = params['waypoints']
    closest_waypoints = params ['closest_waypoints']
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    is_offtrack = ['is_offtrack']
    #steps = params['steps']
    #progress = params['progress']
    heading = params['heading']
       
    # Give a very low reward by default
    reward = 1e-3
    
    "waypoints"
    # Heading penalty/reward
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the track direction in radians and convert to degrees
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)
    
    # Calculate the difference between the track direction and the car's heading
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize if the car is not facing the correct direction
    if direction_diff > 30:  # Threshold for penalizing
        reward -= 10
    else:
        reward += 10
   
    "All wheels on track ?"
    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05 and not is_offtrack:
        reward += 3.0
    elif is_offtrack == True:
        reward -=5  #Try with this next
    
    "Speed"
    if closest_waypoints[1]:
        if speed == 2 :
            reward += 10
        else:
            reward -= 10
    elif closest_waypoints[1]:
        if speed <=1 :
            reward += 10
        else:
            reward -= 10

    return float(reward)



#MK6
# changed speed reward function
import math
def reward_function(params):
       
    # Read input parameters
    waypoints = params['waypoints']
    closest_waypoints = params ['closest_waypoints']
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    is_offtrack = ['is_offtrack']
    #steps = params['steps']
    #progress = params['progress']
    heading = params['heading']
       
    # Give a very low reward by default
    reward = 1e-3
    
    "waypoints"
    # Heading penalty/reward
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the track direction in radians and convert to degrees
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)
    
    # Calculate the difference between the track direction and the car's heading
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize if the car is not facing the correct direction
    if direction_diff > 30:  # Threshold for penalizing
        reward -= 10
    else:
        reward += 10
   
    "All wheels on track ?"
    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05 and not is_offtrack:
        reward += 3.0
    elif is_offtrack == True:
        reward -=5  #Try with this next
    
    "Speed"
    
    if speed == 2 :
        reward += 10
    else:
        reward -= 10
    if speed <=1 :
        reward += 10
    else:
        reward += 1e-3

    return float(reward)




