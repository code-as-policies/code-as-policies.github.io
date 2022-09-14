import numpy as np
from env_utils import get_obj_pos, get_loc_pos

objects = ['banana', 'plum', 'chips', 'water bottle', 'cookie', 'chair', 'table']
# the banana.
ret_val = 'banana'
objects = ['banana', 'plum', 'chips', 'water bottle', 'cookie', 'chair', 'table']
# the snack closest to the robot.
snack_names = ['banana', 'plum', 'chips', 'cookie']
snack_positions = np.array([get_obj_pos(snack_name) for snack_name in snack_names])
closest_snack_idx = get_closest_idx(points=snack_positions, point=np.zeros(3))
closest_snack_name = snack_names[closest_snack_idx]
ret_val = closest_snack_name
objects = ['countertop', 'cart', 'barstool', 'table', 'swivel chair', 'lawn chair']
# the left most chair.
chair_names = ['barstool', 'swivel chair', 'lawn chair']
chair_positions = np.array([get_loc_pos(chair_name) for chair_name in chair_names])
left_chair_idx = get_left_most_idx(chair_positions)
left_chair_name = chair_names[left_chair_idx]
ret_val = left_chair_name
objects = ['avocado', 'peach', 'coke', 'countertop', 'pear', 'water bottle', 'ramen', 'chair']
# the fruit near the front.
fruit_names = ['avocado', 'peach', 'pear']
fruit_positions = np.array([get_obj_pos(fruit_name) for fruit_name in fruit_names])
front_fruit_idx = get_front_most_idx(fruit_positions)
front_fruit_name = fruit_names[front_fruit_idx]
ret_val = front_fruit_name
objects = ['apple', 'coke', 'banana', 'pear', 'water bottle', 'granola bar']
# a fruit.
fruit_names = ['apple', 'banana', 'pear']
ret_val = np.random.choice(fruit_names)
objects = ['white bowl', 'green bowl', 'sprite can', 'protein bar', 'lemon', 'chocolate bar']
# bars behind the lemon.
bar_names = ['chocolate bar', 'protein bar']
lemon_pos = get_obj_pos('lemon')
use_bar_names = []
for bar_name in bar_names:
    if get_obj_pos(bar_name)[1] > lemon_pos[1]:
        use_bar_names.append(bar_name)
ret_val = use_bar_names
objects = ['white bowl', 'green bowl', 'sprite can', 'protein bar', 'banana', 'water bottle']
# the drinks.
ret_val = ['sprite can', 'water bottle']
objects = ['white bowl', 'green bowl', 'sprite can', 'protein bar', 'banana', 'water bottle']
# the blocks.
ret_val = []