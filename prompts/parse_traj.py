import numpy as np
from shapely.geometry import *
from env_utils import get_obj_pos, get_robot_pos, get_obj_names, plan_path
from plan_utils import parse_position, parse_obj_name

# a line that moves forward by 20 centimeters.
current_robot_pos = get_robot_pos()
target_robot_pos = current_robot_pos + [0.2, 0]
pts = interpolate_pts_np(current_robot_pos, target_robot_pos, 20)
ret_val = np.array(pts)
# a circle with radius 10cm arount the current robot pose.
curr_robot_pos = get_robot_pos()
circle = make_circle(radius=0.1, center=curr_robot_pos)
pts_coords = interpolate_pts_along_exterior(exterior=circle.exterior, n=20)
ret_val = np.array(pts_coords)
# a trajectory that goes to the small red square then to its farthest corner.
waypoints = [
  get_obj_pos('small red square'),
  parse_position('the corner farthest from the small red square')
]
ret_val = np.array(waypoints)
# a trajectory from the small green square to the top right corner that avoids the small blue square.
green_square_pos = get_obj_pos('small green square')
corner_pos = parse_position('top right corner')
blue_square_pos = parse_position('small blue square')
blue_square_footprint = make_circle(center=blue_square_pos, radius=0.05)
waypoints = plan_path(start_pos=green_square_pos, goal_pos=corner_pos, avoid_regions=[blue_square_footprint])
ret_val = np.array(waypoints)
# a trajectory that makes a loop through all the blocks.
block_names = parse_obj_name('the blocks', f'objects = {get_obj_names()}')
block_positions = get_obj_positions_np(block_names)
ret_val = np.r_[block_positions, [block_positions[0]]]