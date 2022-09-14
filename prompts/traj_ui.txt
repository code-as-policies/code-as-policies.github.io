# Python 2D robot control script
import numpy as np
from env_utils import follow_traj, get_obj_pos, get_robot_pos, reset_robot, pick_up_obj, put_down_obj, goto_pos
from plan_utils import parse_traj, transform_traj, parse_position, parse_obj_name

# move forward.
traj = parse_traj('a line that moves forward by 20cm')
follow_traj(traj, speed=0.5)
# do it again as fast as you can.
traj = parse_traj('a line that moves forward by 20cm')
follow_traj(traj, speed=1)
# move to the center.
traj = parse_traj('a trajectory that goes to the center')
follow_traj(traj, speed=0.5)
# move to the top left corner then to the center.
traj = parse_traj('a trajectory that goes to the top left corner then to the apple')
follow_traj(traj, speed=0.5)
# move to the left a little and rotate by 45 degrees.
traj = parse_traj('a trajectory that goes to the left by 5cm and rotates by 45 degrees.')
follow_traj(traj, speed=0.5)
# make the robot go in a circle two times around the current pose.
traj = parse_traj('a circle with radius 5cm around the current pose.')
follow_traj(traj, speed=0.5)
follow_traj(traj, speed=0.5)
# do the same motion but with a bigger circle.
traj = transform_traj('make it bigger by 1.5', traj_pts=traj)
follow_traj(traj, speed=0.5)
# do it again but slightly moved to the right.
traj = transform_traj('move to the right by 5cm', traj_pts=traj)
follow_traj(traj, speed=0.5)
# now do it backwards.
traj = transform_traj('reverse it', traj_pts=traj)
follow_traj(traj, speed=0.5)
# move the robot to the left of all the blocks.
pos = parse_position('a point to the left of all the blocks')
goto_pos(pos)
# move the robot in a triangle with the blocks as the vertices.
traj = parse_traj('a triangle with the blocks as the vertices')
follow_traj(traj, speed=0.5)