import numpy as np
from shapely.geometry import *
from shapely.affinity import *

# define function: total = get_total(xs=numbers).
def get_total(xs):
    return np.sum(xs)

# define function: y = eval_line(x, slope, y_intercept=0).
def eval_line(x, slope, y_intercept):
    return x * slope + y_intercept

# define function: pt = get_pt_to_the_left(pt, dist).
def get_pt_to_the_left(pt, dist):
    return pt + [-dist, 0, 0]

# define function: pt = get_pt_to_the_back(pt, dist).
def get_pt_to_the_back(pt, dist):
    return pt + [0, dist, 0]

# define function line = make_line_by_length(length=x).
def make_line_by_length(length):
  line = LineString([[0, 0, 0], [length, 0, 0]])
  return line

# example: interpoate a point halfway on a 2m line.
line = make_line_by_length(2)
pt = np.array(line.interpolate(t, normalized=True).coords[0])

# example: scale a 1m line by 3.
line = make_line_by_length(1)
new_shape = scale(line, xfact=3, yfact=3)