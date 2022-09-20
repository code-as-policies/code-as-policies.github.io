objects = ['red block', 'green block', 'blue block', 'orange block']
# move the sky color block in between the red block and the second block from the left.
say('Ok - putting the blue block in between the red block and the second block from the left')
target_pos = parse_position('a point in the middle between the red block and the second block from the left')
put_first_on_second('blue block', target_pos)

# a point in the middle between the red block and the second block from the left.
red_block_name = parse_obj_name('the red block', f'objects = {get_obj_names()}')
second_block_name = parse_obj_name('the second block from the left', f'objects = {get_obj_names()}')
red_block_pos = get_obj_pos(red_block_name)
second_block_pos = get_obj_pos(second_block_name)
ret_val = (red_block_pos + second_block_pos) / 2

objects = ['red block', 'green block', 'blue block', 'orange block']
# the red block.
ret_val = 'red block'

objects = ['red block', 'green block', 'blue block', 'orange block']
# the second block from the left.
block_names = ['red block', 'green block', 'blue block', 'orange block']
block_positions = get_obj_positions_np(block_names)
left_block_idx = np.argsort(block_positions[:, 0])[1]
left_block_name = block_names[left_block_idx]
ret_val = left_block_name

# define function: block_positions = get_obj_positions_np(block_names).
def get_obj_positions_np(obj_names):
    obj_positions = []
    for obj_name in obj_names:
        obj_positions.append(get_obj_pos(obj_name))
    return np.array(obj_positions)