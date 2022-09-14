import numpy as np
from env_utils import does_not_contain_others, bbox_contains_pt, get_bbox, get_segmask, get_obj_pos, get_color_rgb
from utils import get_obj_positions_np, get_box_area, get_segmask_area

objects = ['small blue square', 'small cyan square', 'purple bowl', 'gray bowl', 'brown bowl', 'small pink square', 'small purple square']
# the block closest to the purple bowl.
block_names = ['small blue square', 'small cyan square', 'small purple square']
block_positions = get_obj_positions_np(block_names)
closest_block_idx = get_closest_idx(points=block_positions, point=get_obj_pos('purple bowl'))
closest_block_name = block_names[closest_block_idx]
ret_val = closest_block_name
objects = ['brown bowl', 'small green square', 'small brown square', 'green bowl', 'blue bowl', 'small blue square']
# the left most block.
block_names = ['small green square', 'small brown square', 'small blue square']
block_positions = get_obj_positions_np(block_names)
left_block_idx = np.argmin(block_positions[:, 0])
left_block_name = block_names[left_block_idx]
ret_val = left_block_name
objects = ['brown bowl', 'small green square', 'small brown square', 'green bowl', 'blue bowl', 'small blue square']
# the bowl on near the top.
bowl_names = ['brown bowl', 'green bowl', 'blue bowl']
bowl_positions = get_obj_positions_np(bowl_names)
top_bowl_idx = np.argmax(block_positions[:, 1])
top_bowl_name = bowl_names[top_bowl_idx]
ret_val = top_bowl_name
objects = ['brown bowl', 'banana', 'small brown square', 'apple', 'blue bowl', 'small blue square']
# the largest fruit.
fruit_names = ['banana', 'apple']
fruit_segmasks = [get_segmask(name) for name in fruit_names]
fruit_segmask_areas = [get_segmask_area(segmask) for segmask in fruit_segmasks]
ret_val = fruit_names[np.argmax(fruit_segmask_areas)]
objects = ['brown bowl', 'banana', 'small brown square', 'apple', 'blue bowl', 'small blue square']
# the blocks.
ret_val = ['small brown square', 'small blue square']
objects = ['brown bowl', 'banana', 'small brown square', 'apple', 'blue bowl', 'small blue square']
# the brown objects.
ret_val = ['brown bowl', 'small brown square']
objects = ['brown bowl', 'banana', 'small brown square', 'apple', 'blue bowl', 'small blue square']
# a fruit that's not the apple
fruit_names = ['banana', 'apple']
for fruit_name in fruit_names:
    if fruit_name != 'apple':
        ret_val = fruit_name
objects = ['brown bowl', 'small green square', 'small brown square', 'green bowl', 'blue bowl', 'small blue square']
# the object on the green bowl.
for obj_name in objects:
    if obj_name != 'green bowl':
        if bbox_contains_pt(container_name='green bowl', obj_name=obj_name):
            ret_val = obj_name
            break
objects = ['small blue square', 'small cyan square', 'purple bowl', 'brown bowl', 'small purple square']
# blocks above the brown bowl.
block_names = ['small blue square', 'small cyan square', 'small purple square']
brown_bowl_pos = get_obj_pos('brown bowl')
use_block_names = []
for block_name in block_names:
    if get_obj_pos(block_name)[1] > brown_bowl_pos[1]:
        use_block_names.append(block_name)
ret_val = use_block_names
objects = ['small blue square', 'small cyan square', 'purple bowl', 'brown bowl', 'small purple square']
# the blue block.
ret_val = 'small blue square'
objects = ['lime', 'banana', 'plum', 'apple', 'mango']
# the most sour fruit.
ret_val = 'lime'