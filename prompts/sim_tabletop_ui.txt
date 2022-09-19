# Python 2D robot control script
import numpy as np
from env_utils import get_obj_pos, detect_obj, get_obj_names
from plan_utils import parse_position, parse_obj_name
from ctrl_utils import put_first_on_second, stack_objects_in_order, point_gripper_to

objects = ['cyan block', 'yellow block', 'brown block', 'green bowl']
# put the yellow one the green thing.
put_first_on_second('yellow block', 'green bowl')
objects = ['pink block', 'graNy block', 'orange block']
# move the pinkish colored block on the bottom side.
bottom_side_pos = parse_position('the bottom side')
put_first_on_second('pink block', bottom_side_pos)
objects = ['orange bowl', 'red block', 'purple bowl', 'blue block', 'blue bowl', 'orange block', 'purple block', 'red bowl']
# put the blocks into bowls with matching colors.
# put_first_on_second('orange block', 'orange bowl')
# put_first_on_second('red block', 'red bowl')
# put_first_on_second('purple block', 'purple bowl')
# put_first_on_second('blue block', 'blue bowl')
objects = ['orange bowl', 'red block',  'purple block', 'orange block', 'purple bowl', 'red bowl']
# point gripper to any three points in a horizontal line in the middle
n_points = 3
place_positions = parse_position(f'a horizontal line in the middle with {n_points} points')
for line_position in place_positions:
    point_gripper_to(line_position)
objects = ['orange bowl', 'red block',  'purple block', 'orange block', 'purple bowl', 'red bowl']
# point gripper to k points in a diagonal line, where k is the number of bowls
bowl_names = parse_obj_name('the bowls', f'objects = {get_obj_names()}')
k = len(bowl_names)
place_positions = parse_position(f'a diagonal line with {k} points')
for line_position in place_positions:
    point_gripper_to(line_position)
objects = ['purple block', 'cyan bowl', 'blue block', 'cyan block', 'purple bowl', 'blue bowl']
# move the blue block in between the cyan block and purple bowl.
target_pos = parse_position('a point between the cyan block and purple bowl')
put_first_on_second('blue block', target_pos)
objects = ['purple block', 'cyan bowl', 'blue block', 'cyan block', 'purple bowl', 'blue bowl']
# move the block closest to the purple bowl to the cyan bowl.
closest_block_name = parse_obj_name('the block closest to the purple bowl', f'objects = {get_obj_names()}')
put_first_on_second(closest_block_name, 'cyan bowl')
objects = ['yellow bowl', 'blue block', 'yellow block', 'blue bowl']
# point gripper to the corner closest to the yellow block.
closest_corner_pos = parse_position('the corner closest to the yellow block')
point_gripper_to(closest_corner_pos)
objects = ['brown bowl', 'green block', 'brown block', 'green bowl', 'blue bowl', 'blue block']
# move the left most block to the green bowl.
left_block_name = parse_obj_name('left most block', f'objects = {get_obj_names()}')
put_first_on_second(left_block_name, 'green bowl')
objects = ['brown bowl', 'green block', 'brown block', 'blue bowl', 'blue block', 'green bowl']
# move the brown bowl to the closest side.
closest_side_position = parse_position('the side closest to the brown bowl')
put_first_on_second('brown bowl', closest_side_position)
objects = ['brown bowl', 'green block', 'brown block', 'green bowl', 'blue bowl', 'blue block']
# place the green block in the bowl closest to the middle.
middle_bowl_name = parse_obj_name('the bowl closest to the middle', f'objects = {get_obj_names()}')
put_first_on_second('green block', middle_bowl_name)
objects = ['brown bowl', 'green block', 'brown block', 'blue bowl', 'blue block', 'green bowl']
# place the blue block in the empty bowl.
empty_bowl_name = parse_obj_name('the empty bowl', f'objects = {get_obj_names()}')
put_first_on_second('blue block', empty_bowl_name)
objects = ['brown bowl', 'blue bowl', 'blue block', 'red block', 'brown block', 'red bowl']
# stack the blocks that are close to the red bowl.
close_block_names = parse_obj_name('blocks that are close to the red bowl', f'objects = {get_obj_names()}')
stack_objects_in_order(object_names=close_block_names)
objects = ['red block', 'red bowl', 'blue bowl', 'blue block']
# stack the blocks on the top most bowl.
bowl_name = parse_obj_name('top most bowl', f'objects = {get_obj_names()}')
block_names = parse_obj_name('the blocks', f'objects = {get_obj_names()}')
object_names = [bowl_name] + block_names
stack_objects_in_order(object_names=object_names)
objects = ['yellow bowl', 'red block', 'yellow block', 'red bowl', 'green plate', 'orange plate']
# move objects from the green plate to the red bowl.
object_names = parse_obj_name('objects from the green plate', f'objects = {get_obj_names()}')
for object_name in object_names:
    put_first_on_second(object_name, 'red bowl')
objects = ['yellow bowl', 'red block', 'yellow block', 'red bowl', 'green plate', 'orange plate']
# move the red bowl the left of the blocks.
left_pos = parse_position('a point left of the blocks')
put_first_on_second('red bowl', left_pos)