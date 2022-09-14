# Python 2D shapes
import numpy as np
from shapely.geometry import *
from shapely.affinity import *
from utils import denormalize_xy, get_obj_pos, parse_obj_name, get_obj_names

# a circle with radius 20cm around the middle with 16 pts.
center_pos = denormalize_xy([0.5, 0.5])
circle_shape = make_circle(radius=0.2, center=center_pos)
circle_shape_pts = interpolate_pts_2d_along_exterior(exterior=circle_shape.exterior, n=16)
ret_val = circle_shape_pts
# make it bigger by 1.5x.
circle_shape = scale(circle_shape, xfact=1.5, yfact=1.5)
circle_shape_pts = interpolate_pts_2d_along_exterior(exterior=circle_shape.exterior, n=16)
ret_val = circle_shape_pts
# a triangle with size 5cm around the banana.
banana_name = parse_obj_name('the banana', f'objects = {get_obj_names()}')
banana_pos = get_obj_pos(banana_name)
triangle_shape = make_triangle(size=0.05, center=banana_pos)
triangle_shape_pts = get_points_from_polygon(triangle_shape)
ret_val = triangle_shape_pts
# a triangle with size 5cm above the banana.
banana_name = parse_obj_name('the banana', f'objects = {get_obj_names()}')
banana_pos = get_obj_pos(banana_name)
another_triangle_shape = make_triangle(size=0.05, center=banana_pos + [0, 0.05])
another_triangle_shape_pts = get_points_from_polygon(another_triangle_shape)
ret_val = another_triangle_shape_pts
# move the first triangle to the left by 5cm.
triangle_shape = translate(triangle_shape, xoff=-0.05, yoff=0)
triangle_shape_pts = get_points_from_polygon(triangle_shape)
ret_val = triangle_shape_pts
# a square with size 10cm around the largest fruit.
large_fruit_name = parse_obj_name('the largest fruit', f'objects = {get_obj_names()}')
large_fruit_pos = get_obj_pos(large_fruit_name)
square_shape = make_square(size=0.1, center=large_fruit_pos)
square_shape_pts = get_points_from_polygon(square_shape)
ret_val = square_shape_pts
# a horizontal line with length 30cm at the top with 2 pts.
top_side = denormalize_xy([0, 0.5])
start_pos = top_side + [-0.15, 0]
end_pos = top_side + [0.15, 0]
top_line_pts = np.array([start_pos, end_pos])
ret_val = top_line_pts
# a line from the top left to the bottom right.
top_left_corner = denormalize_xy([0, 1])
bottom_rirght_corner = denormalize_xy([1, 0])
line_pts = np.array([top_left_corner, bottom_right_corner])
ret_val = line_pts
# a line from the top side to the right side.
top_side = denormalize_xy([0.5, 1])
right_side = denormalize_xy([1, 0.5])
line_pts = np.array([top_side, right_side])
ret_val = line_pts