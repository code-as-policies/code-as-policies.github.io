objects = ['red block', 'green block', 'blue block', 'orange block']
# arrange the blocks in a square around the middle.
say('Ok - arranging the blocks in a square around the middle')
block_names = parse_obj_name('the blocks', f'objects = {get_obj_names()}')
square_pts = parse_position(f'a square with size 10cm around the middle with {len(block_names)} points')
for block_name, pt in zip(block_names, square_pts):
    put_first_on_second(block_name, pt)

objects = ['red block', 'green block', 'blue block', 'orange block']
# the blocks.
ret_val = ['red block', 'green block', 'blue block', 'orange block']

# a square with size 10cm around the middle with 4 points.
polygon = make_square(size=0.1, center=denormalize_xy([0.5, 0.5]))
points = get_points_from_polygon(polygon)
ret_val = points

# define function; polygon = make_square(size=0.1, center=denormalize_xy([0.5, 0.5])).
def make_square(size, center):
    square = Polygon([
        center + [-size/2, -size/2],
        center + [size/2, -size/2], 
        center + [size/2, size/2], 
        center + [-size/2, size/2]
    ])
    return square

# define function; points = get_points_from_polygon(polygon).
def get_points_from_polygon(polygon):
    return np.array(polygon.exterior.coords)