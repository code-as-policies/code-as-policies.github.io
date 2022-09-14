import numpy as np
# make it bigger by 1.5.
new_traj_pts = scale_pts_around_centroid_np(traj_pts, scale_x=1.5, scale_y=1.5, scale_z=1)
# move it to the right by 10cm.
new_traj_pts = translate_pts_np(traj_pts, delta=[0.1, 0, 0])
# move it to the front by 20cm.
new_traj_pts = translate_pts_np(traj_pts, delta=[0, -0.2, 0])
# rotate it clockwise by 40 degrees.
new_traj_pts = rotate_3d_pts_around_centroid_np(traj_pts, angle_z=-np.deg2rad(40))
# rotate by 30 degrees and make it slightly smaller
temp_traj_pts = rotate_3d_pts_around_centroid_np(traj_pts, angle_z=np.deg2rad(30))
new_traj_pts = scale_pts_around_centroid_np(temp_traj_pts, scale_x=0.7, scale_y=0.7, scale_z=1)