import numpy as np
from shapely.geometry import *
from shapely.affinity import *
from env_utils import parse_loc_name, parse_obj_name, get_visible_obj_names, get_loc_names, get_obj_pos, get_loc_pos, get_robot_pos

# a line with 5 points from the robot to the chair with no arms.
start_pos = get_robot_pos()
chair_name = parse_loc_name('the chair with no arms', f'objects = {get_loc_names()}')
end_pos = get_loc_pos(chair_name)
line = make_line(start=start_pos, end=end_pos)
points_3d = interpolate_pts_on_line(line=line, n=2)
ret_val = points_3d
# a point 0.1m left of the bowls.
bowl_names = parse_obj_name('the bowls', f'objects = {get_visible_obj_names()}')
bowl_positions = np.array([get_obj_pos(bowl_name) for bowl_name in bowl_names])
left_obj_pos = bowl_positions[np.argmin(bowl_positions[:, 0])] + [-0.1, 0, 0]
ret_val = left_obj_pos
# a point 0.2m in behind the banana.
banana_name = parse_obj_name('the banana', f'objects = {get_visible_obj_names()}')
ret_val = get_obj_pos(banana_name) + [0, 0.2, 0]
# a 1m square around the table with 4 points.
table_name = parse_loc_name('the table', f'objects = {get_loc_names()}')
table_pos_2d = get_loc_pos(table_name)[:2]
shape_2d = make_square(size=1, center=table_pos_2d)
points_2d = get_points_from_polygon(shape_2d)
points_3d = np.c_[points_2d, np.zeros(len(points_2d))]
ret_val = points_3d
# a 1.5m circle with centered around the lounge chair with 20 points.
lounge_chair_name = parse_loc_name('the lounge chair', f'objects = {get_loc_names()}')
lounge_chair_pos = get_loc_pos(lounge_chair_name)
shape_2d = make_circle(radius=1.5, center=lounge_chair_pos)
points_2d = interpolate_pts_along_exterior(exterior=shape_2d.exterior, n=20)
points_3d = np.c_[points_2d, np.zeros(len(points_2d))]
ret_val = points_3d