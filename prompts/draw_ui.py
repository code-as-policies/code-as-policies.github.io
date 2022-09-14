# Python 2D robot control script
import numpy as np
from env_utils import draw, erase
from plan_utils import parse_shape_pts, get_obj_names, parse_obj_name, say, transform_shape_pts

# draw a circle in the middle.
say('sure - drawing a 5cm circle around the middle')
circle_shape_pts = parse_shape_pts('a circle with radius 5cm around the middle with 16 pts')
draw(circle_shape_pts)
# make it smaller.
say('ok - making the circle smaller by half')
erase(circle_shape_pts)
circle_shape_pts = transform_shape_pts('scale it by 0.5x', shape_pts=circle_shape_pts)
draw(circle_shape_pts)
# draw a triangle around banana.
say('got it - drawing a triangle around the banana')
triangle_shape_pts = parse_shape_pts('a triangle with size 10cm around the banana')
draw(triangle_shape_pts)
# draw another triangle above the banana.
say('no problem - drawing another triangle above the bananas')
another_triangle_shape_pts = transform_shape_pts('move it up by 10cm', shape_pts=triangle_shape_pts)
draw(another_triangle_shape_pts)
# erase both triangles.
say('sure - erasing both triangles')
pts_to_erase = np.r_[triangle_shape_pts, another_triangle_shape_pts]
erase(pts_to_erase)
# draw squares around the bottles.
say('ok - drawing a square around each bottle')
bottle_names = parse_obj_name('the bottles', f'objects = {get_obj_names()}')
bottle_square_shape_pts = []
for bottle_name in bottle_names:
  bottle_square_shape_pts.append(parse_shape_pts(f'a 10cm square around the {bottle_name}'))
for shape_pts in bottle_square_shape_pts:
  draw(shape_pts)
# draw a vertical line across the middle.
say('ok - drawing a vertical line across the middle')
line_pts = parse_shape_pts('a vertical line with length 20cm across the middle')
draw(line_pts)