import numpy as np
from shapely.geometry import *
from shapely.affinity import *
from env_utils import denormalize_xy, parse_obj_name, get_obj_names, get_obj_pos

# a horizontal line in the middle with 3 points.
start_pos = denormalize_xy([0.1, 0.5])
end_pos = denormalize_xy([0.9, 0.5])
line = make_line(start=start_pos, end=end_pos)
points = interpolate_pts_on_line(line=line, n=3)
ret_val = points
# a diagonal line.
start_pos = denormalize_xy([0.1, 0.5])
end_pos = denormalize_xy([0.9, 0.5])
line = rotate(make_line(start=start_pos, end=end_pos), 45)
points = interpolate_pts_on_line(line=line, n=4)
ret_val = points
# a square with 4 points.
square = make_square(size=1)
points = get_points_from_polygon(polygon=square)
ret_val = points
# a point between the cyan block and purple bowl.
block_name = parse_obj_name('cyan block', f'objects = {get_obj_names()}')
bowl_name = parse_obj_name('purple bowl', f'objects = {get_obj_names()}')
pts = [get_obj_pos(block_name), get_obj_pos(bowl_name)]
pos = get_center_np(pts=pts)
ret_val = pos
# the corner closest to the sun colored block.
block_name = parse_obj_name('the sun colored block', f'objects = {get_obj_names()}')
corner_positions = get_corner_positions()
closest_corner_idx = get_closest_idx(points=corner_positions, point=get_obj_pos(block_name))
closest_corner_pos = corner_positions[closest_corner_idx]
ret_val = closest_corner_pos
# the side closest to the brown bowl.
bowl_name = parse_obj_name('brown bowl', f'objects = {get_obj_names()}')
side_positions = get_side_positions()
closest_side_idx = get_closest_idx(points=side_positions, point=get_obj_pos(bowl_name))
closest_side_pos = side_positions[closest_side_idx]
ret_val = closest_side_pos
# the top right corner.
top_left_pos_normalized = [0, 1]
top_left_pos = denormalize_xy(top_left_pos_normalized)
ret_val = top_left_pos
# the bottom side.
bottom_pos_normalized = [0.5, 0]
bottom_pos = denormalize_xy(bottom_pos_normalized)
ret_val = bottom_pos
# a point left of the bowls.
bowl_names = parse_obj_name('the bowls', f'objects = {get_obj_names()}')
bowl_positions = get_all_object_positions_np(obj_names=bowl_names)
left_obj_pos = bowl_positions[np.argmin(bowl_positions[:, 0])] + [-0.1, 0]
ret_val = left_obj_pos