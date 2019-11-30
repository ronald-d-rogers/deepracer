def reward_function(params):

    import math
    from shapely.geometry import Point

    # Read input parameters
    x = float(params['x'])
    y = float(params['y'])
    point = Point(x, y)
    
    distance_from_center = float(params['distance_from_center'])
    track_width = float(params['track_width'])
    steering = float(params['steering_angle'])
    speed = int(params['speed'])
    progress = float(params['progress'] /100.0)

    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    reward = 0.0
    reward = abs((track_width/2.0)-distance_from_center) +1.0

    return reward
