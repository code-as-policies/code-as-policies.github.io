# Python 2D robot control script
import numpy as np
from perception_utils import is_obj_visible, get_visible_obj_names, get_loc_names, get_robot_pos_and_angle
from action_utils import goto_pos, goto_loc, pick_obj, place_at_obj, place_at_pos, say
from plan_utils import transform_traj, parse_position, parse_loc_name, parse_obj_name

# make the robot go in a 1m square two times around the current pose.
traj = parse_position('a 1m square around the current pose with 4 points')
say('ok - moving twice in a 1m square around where I am')
for _ in range(2):
  follow_traj(traj, speed=0.5)
# do the same motion but with a bigger square.
traj = transform_traj('make it bigger by 1.5', traj_pts=traj)
say('no problem - making the square bigger by 1.5 times')
follow_traj(traj, speed=0.5)
# do the same motion but faster
say('no problem - go faster')
follow_traj(traj, speed=0.75)
# go in a 1.5m circle around the table.
traj = parse_position('a 1.5m circle around the table with 20 points')
follow_traj(traj, speed=0.5)
# do the same motion but slower
say('no problem - go slower')
follow_traj(traj, speed=0.25)
# do it again but slightly moved to the right.
traj = transform_traj('move to the right by 0.5m', traj_pts=traj)
say('got it - moving the square to the right by 0.5m')
follow_traj(traj, speed=0.5)
# now do it backwards.
traj = transform_traj('reverse it', traj_pts=traj)
say('sure thing - moving backwards through the square')
follow_traj(traj, speed=0.5)
# go to the middle of the chairs as fast as you can.
target_pos = parse_position('a point in the middle of the chairs')
say('ok - going to the middle of the chairs')
goto_pos(target_pos, speed=1)
# take the marker from the cart and put it in the second container from the left on the table.
say('sure - moving the marker on the cart into the second container from the left on the table')
marker_loc = 'cart'
goto_loc(marker_loc); pick_obj('marker')
goto_loc('table'); container_name = parse_obj_name('the second container from the left', f'objects = {get_visible_obj_names()}')
place_at_obj(container_name)
# move the coke can on the table a bit to the left of the mug on the desk.
coke_loc = 'table'
goto_loc(coke_loc); pick_obj('coke can')
mug_loc = 'desk'
goto_loc(mug_loc); target_pos = parse_position('a point 5cm to the left of the mug')
place_at_pos(target_pos)
# is there a coke can on the chair.
goto_loc('chair')
if is_obj_visible('coke can', loc='chair'):
  say('Yes - there is a coke can on the chair')
else:
  say('No - there is no coke can on the chair')
# are there snacks on the countertop.
snacks_loc = 'countertop'
goto_loc(snacks_loc); snack_names = parse_obj_name('the snacks', f'objects = {get_visible_obj_names()}')
if len(snack_names) > 0:
  say('Yes - there are snacks on the countertop')
else:
  say('No - there are no snacks on the countertop')
# move the coke can on the table a bit to the left.
coke_loc = 'table'
goto_loc(coke_loc)
target_pos = parse_position('a point 5cm to the left of the coke can')
goto_loc(coke_loc); pick_obj('coke can')
place_at_pos(target_pos)
# here is my desk.
say('ok')
my_desk_pos, my_desk_angle = get_robot_pos_and_angle()
# get a carbonated drink from the desk and bring it to my desk.
say('sure - bringing a carbonated drink from the desk to your desk')
carbonated_drink_loc = 'desk'
goto_loc(carbonated_drink_loc); carbonated_drink_name = parse_obj_name('a carbonated drink', f'objects = {get_visible_obj_names()}')
goto_loc(carbonated_drink_pos); pick_obj(carbonated_drink_name)
goto_pos(my_desk_pos, angle=my_desk_angle)
# the snacks are on the cart and the plate is on the countertop.
snack_loc = 'cart'
plate_loc = 'countertop'
say('got it')
# put the snacks on the plate.
say('got it - taking the snacks from the cart and putting them in the plate on the countertop')
goto_loc(snack_loc); snack_names = parse_obj_name('the snacks', f'objects = {get_visible_obj_names()}')
for snack_name in snack_names:
  goto_loc(snack_loc); pick_obj(snack_name)
  goto_loc(plate_loc)
  place_at_obj('plate')
# keep looking until you see an apple on the table.
say('ok - I\'ll keep looking for an apple on the table.')
goto_loc('table')
while True:
  if is_obj_visible('apple', loc='table'):
    break
say('I see an apple')
# go in a square around the current position one step at a time.
say('sure - going in a square around where I am one step at a time')
traj = parse_position('a 1m square around the current pose with 4 points')
for pos in traj:
  goto_pos(pos)
# this is the shopping cart.
shopping_cart_pos, shopping_cart_angle = get_robot_pos_and_angle()
shopping_cart_name = 'shopping cart'
say('ok')
# the vegetables are on the shelf.
vegetable_loc = 'shelf'
say('ok')
# put the vegetables on the shopping cart.
say('got it - putting vegetables from the shelf to the shopping cart')
goto_loc(vegetable_loc); vegetable_names = parse_obj_name('the vegetables', f'objects = {get_visible_obj_names()}')
for vegetable_name in vegetable_names:
    goto_loc(vegetable_loc); pick_obj(vegetable_name)
    goto_pos(shopping_cart_pos, angle=shopping_cart_angle)
    place_at_obj(shopping_cart_name)
# keep checking for books on the boookshelf and tell me how many are there each time.
while True:
  goto_loc('boookshelf'); book_names = parse_obj_name('the books', f'objects = {get_visible_obj_names()}')
  say('there are {len(book_names)} books on the bookshelf')