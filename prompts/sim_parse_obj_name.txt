import numpy as np
from env_utils import get_obj_pos, get_color
from utils import get_obj_positions_np, get_box_area

objects = ['blue block', 'cyan block', 'purple bowl', 'gray bowl', 'brown bowl', 'pink block', 'purple block']
# the block closest to the purple bowl.
block_names = ['blue block', 'cyan block', 'purple block']
block_positions = get_obj_positions_np(block_names)
closest_block_idx = get_closest_idx(points=block_positions, point=get_obj_pos('purple bowl'))
closest_block_name = block_names[closest_block_idx]
ret_val = closest_block_name
objects = ['brown bowl', 'green block', 'brown block', 'green bowl', 'blue bowl', 'blue block']
# the left most block.
block_names = ['green block', 'brown block', 'blue block']
block_positions = get_obj_positions_np(block_names)
left_block_idx = np.argsort(block_positions[:, 0])[0]
left_block_name = block_names[left_block_idx]
ret_val = left_block_name
objects = ['brown bowl', 'green block', 'brown block', 'green bowl', 'blue bowl', 'blue block']
# the third bowl from the top.
bowl_names = ['brown bowl', 'green bowl', 'blue bowl']
bowl_positions = get_obj_positions_np(bowl_names)
top_bowl_idx = np.argsort(bowl_positions[:, 1])[-3]
top_bowl_name = bowl_names[top_bowl_idx]
ret_val = top_bowl_name
objects = ['brown bowl', 'banana', 'brown block', 'apple', 'blue bowl', 'blue block']
# the largest fruit.
fruit_names = ['banana', 'apple']
fruit_bbox = [get_bbox(name) for name in fruit_names]
fruit_sizes = [get_box_area(bbox) for bbox in fruit_bbox]
ret_val = fruit_names[np.argmax(fruit_sizes)]
objects = ['brown bowl', 'banana', 'brown block', 'apple', 'blue bowl', 'blue block']
# the blocks.
ret_val = ['brown block', 'blue block']
objects = ['brown bowl', 'banana', 'brown block', 'apple', 'blue bowl', 'blue block']
# a fruit that's not the apple
fruit_names = ['banana', 'apple']
for fruit_name in fruit_names:
    if fruit_name != 'apple':
        ret_val = fruit_name
objects = ['brown bowl', 'green block', 'brown block', 'green bowl', 'blue bowl', 'blue block']
# the object on the green bowl.
for obj_name in objects:
    if obj_name != 'green bowl':
        if np.linalg.norm(get_obj_pos('green bowl') - get_obj_pos(obj_name)) < 0.05:
            ret_val = obj_name
            break
objects = ['brown bowl', 'green block', 'brown block', 'green bowl', 'blue bowl', 'blue block']
# the brown block.
ret_val = 'brown block'