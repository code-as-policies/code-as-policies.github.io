from utils import get_obj_pos, get_obj_names, parse_obj_name, bbox_contains_pt, is_obj_visible

objects = ['yellow bowl', 'small blue square', 'small yellow square', 'blue bowl', 'fruit', 'small green square', 'black bowl']
# is the blue block to the right of the yellow bowl?
ret_val = get_obj_pos('blue block')[0] > get_obj_pos('yellow bowl')[0]
objects = ['yellow bowl', 'small blue square', 'small yellow square', 'blue bowl', 'fruit', 'small green square', 'black bowl']
# how many yellow objects are there?
yellow_object_names = parse_obj_name('the yellow objects', f'objects = {get_obj_names()}')
ret_val = len(yellow_object_names)
objects = ['small pink square', 'small green square', 'pink bowl', 'small blue square', 'blue bowl', 'green bowl']
# is the pink block on the green bowl?
ret_val = bbox_contains_pt(container_name='green bowl', obj_name='small pink square')
objects = ['small pink square', 'small green square', 'pink bowl', 'small blue square', 'blue bowl', 'green bowl']
# what are the blocks left of the green bowl?
block_names = parse_obj_name('the blocks', f'objects = {get_obj_names()}')
green_bowl_pos = get_obj_pos('green bowl')
left_block_names = []
for block_name in block_names:
  if get_obj_pos(block_name)[0] < green_bowl_pos:
    left_block_names.append(block_name)
ret_val = left_block_names
objects = ['small pink square', 'small green square', 'pink bowl', 'small blue square', 'blue bowl', 'green bowl']
