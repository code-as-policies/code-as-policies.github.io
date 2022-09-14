def get_obj_positions_np(obj_names):
    obj_positions = []
    for obj_name in obj_names:
        obj_positions.append(get_obj_pos(obj_name))
    return np.array(obj_positions)

def get_left_most_idx(points):
    return np.argmin(points[:, 0])

def get_right_most_idx(points):
    return np.argmax(points[:, 0])

def get_top_most_idx(points):
    return np.argmax(points[:, 1])

def get_bottom_most_idx(points):
    return np.argmin(points[:, 1])

def get_farthest_idx(points, point):
    dists = np.linalg.norm(points - point, axis=1)
    return np.argmax(dists)

def get_closest_idx(points, point):
    return np.argmin(np.linalg.norm(points - point, axis=1))

def get_closest_point(points, point):
    closest_point = points[np.argmin(np.linalg.norm(points - point, axis=1))]
    return closest_point

def get_farthest_point(points, point):
    closest_point = points[np.argmax(np.linalg.norm(points - point, axis=1))]
    return closest_point

def get_corner_positions():
    unit_square = box(0, 0, 1, 1)
    normalized_corners = np.array(list(unit_square.exterior.coords))[:4]
    corners = np.array(([denormalize_xy(corner) for corner in normalized_corners]))
    return corners

def get_side_positions():
    side_xs = np.array([0, 0.5, 0.5, 1])
    side_ys = np.array([0.5, 0, 1, 0.5])
    normalized_side_positions = np.c_[side_xs, side_ys]
    side_positions = np.array(([denormalize_xy(corner) for corner in normalized_side_positions]))
    return side_positions

def stack_objects_in_order(object_names):
    for i in range(len(object_names) - 1):
        put_first_on_second(object_names[i + 1], object_names[i])

def get_box_area(bbox):
    return (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])

def does_not_contain_others(bowl_name):
    obj_names = get_obj_names()
    for obj_name in obj_names:
        if obj_name != bowl_name:
            if contains(bowl_name, obj_name):
                return False
    return True

def contains(bowl_name, obj_name):
    obj_pt = get_obj_pos(obj_name)
    bowl_bbox = get_bbox(bowl_name)
    return bbox_xyxy_contains_pt(bbox=bowl_bbox, pt=obj_pt)

def bbox_xyxy_contains_pt(bbox, pt):
    xmin, ymin, xmax, ymax = bbox
    x, y = pt
    return xmin <= x <= xmax and ymin <= y <= ymax

def bbox_contains_pt(container_name, obj_name):
    container_bbox = get_bbox(container_name)
    obj_pos = get_obj_pos(obj_name)
    return container_bbox[0] <= obj_pos[0] <= container_bbox[2] and container_bbox[1] <= obj_pos[1] <= container_bbox[3]

def interpolate_pts_on_line(line, n):
    pts = []
    for i in range(n):
        t = i / (n - 1)
        pt = interpolate_line(line, t)
        pts.append(pt)
    return np.array(pts)

def interpolate_line(line, t):
    pt = line.interpolate(t, normalized=True)
    return np.array(pt.coords[0])

def get_points_from_polygon(shape):
    return np.array(shape.exterior.coords)

def make_square(size, center):
    square = Polygon([
        center + [-size/2, -size/2],
        center + [size/2, -size/2], 
        center + [size/2, size/2], 
        center + [-size/2, size/2]
    ])
    return square

def make_circle(radius, center):
  circle = Point(center).buffer(radius)
  return circle

def normalize_vector(vector):
    direction = vector / np.linalg.norm(vector)
    return direction

def get_orthogonal_vector_from_line_to_point(line, point):
    # get the line's vector.
    line_vector = np.array(line.coords[1]) - np.array(line.coords[0])
    # get the point's vector.
    point_vector = np.array(point) - np.array(line.coords[0])
    # get the orthogonal vector.
    orthogonal_vector = np.array([-line_vector[1], line_vector[0]])
    # get the dot product.
    dot_product = np.dot(point_vector, orthogonal_vector)
    # if the dot product is negative, reverse the orthogonal vector.
    if dot_product < 0:
        orthogonal_vector = -orthogonal_vector
    # return the orthogonal vector.
    return orthogonal_vector

def interpolate_pts_between_wps_np(wps, n):
  pts = np.zeros((n, 2))
  for i in range(len(wps) - 1):
    pts[i * n // (len(wps) - 1):(i + 1) * n // (len(wps) - 1), :] = np.linspace(wps[i], wps[i + 1], n // (len(wps) - 1), endpoint=False)
  return pts

def interpolate_pts_np(start, end, n):
  pts = np.linspace(start, end, n)
  return pts

def interpolate_poly_traj_from_2d_wps(wps, n, deg):
    ts = np.linspace(0, 1, n)
    (poly_x, poly_y) = fit_2d_np_polys(ts, wps, deg)
    pts_2d = get_pts_2d_from_np_polys_polyval(poly_x, poly_y, ts)
    return pts_2d

def fit_2d_np_polys(ts, pts_2d, deg):
    poly_x = np.polyfit(ts, pts_2d[:, 0], deg)
    poly_y = np.polyfit(ts, pts_2d[:, 1], deg)
    return (poly_x, poly_y)

def get_2d_pts_from_polys_polyval(poly_x, poly_y, ts):
    xs = np.polyval(poly_x, ts)
    ys = np.polyval(poly_y, ts)
    pts_2d = np.stack((xs, ys), axis=1)
    return pts_2d

def interpolate_pts_2d_along_exterior(exterior, n):
    pts_coords = np.array(list(exterior.coords))
    pts_coords_interpolated = np.array([np.linspace(pts_coords[i][0], pts_coords[i+1][0], n) for i in range(len(pts_coords)-1)]).flatten()
    pts_coords_interpolated = np.vstack((pts_coords_interpolated, np.array([np.linspace(pts_coords[i][1], pts_coords[i+1][1], n) for i in range(len(pts_coords)-1)]).flatten()))
    return pts_coords_interpolated.T

def translate_pts_np(pts, delta):
  return pts + delta

def rotate_pts_around_centroid_np(pts, angle):
  centroid = np.mean(pts, axis=0)
  rot_mat = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
  new_pts = np.dot(pts - centroid, rot_mat) + centroid
  return new_pts

def scale_pts_around_centroid_np(traj_pts, scale_x=1.5, scale_y=1.5):
    centroid = np.mean(traj_pts, axis=0)
    new_traj_pts = traj_pts - centroid
    new_traj_pts[:, 0] = new_traj_pts[:, 0] * scale_x
    new_traj_pts[:, 1] = new_traj_pts[:, 1] * scale_y
    new_traj_pts = new_traj_pts + centroid
    return new_traj_pts

def interpolate_pts_along_exterior(exterior, n):
    pts_coords = []
    for i in range(n):
        t = i / (n - 1)
        pt = exterior.interpolate(t, normalized=True)
        pts_coords.append(pt.coords[0])
    return pts_coords

def make_rectangle(width, height, center):
  rect = box(center[0] - width / 2, center[1] - height / 2, center[0] + width / 2, center[1] + height / 2)
  return rect

# define function: traj_has_pos_close_to_target_obj_pos(traj_pts, apple_pos, threshold=0.1).
def traj_has_pos_close_to_target_obj_pos(traj_pts, apple_pos, threshold=0.1):
  for traj_pt in traj_pts:
    if np.linalg.norm(traj_pt - apple_pos) < threshold:
      return True
  return False

def make_line(start, end):
  line = LineString([start, end])
  return line

def get_orthogonal_direction_from_line_to_point(line, point):
  # get the line's direction.
  direction = np.array(line.coords[1]) - np.array(line.coords[0])
  direction = direction / np.linalg.norm(direction)
  # get the orthogonal direction.
  orthogonal_direction = np.array([-direction[1], direction[0]])
  # get the point's direction.
  point_direction = np.array(point) - np.array(line.coords[0])
  # get the sign of the point's direction.
  sign = np.sign(np.dot(point_direction, orthogonal_direction))
  # get the orthogonal direction from the line to the point.
  orthogonal_direction_from_line_to_point = sign * orthogonal_direction
  return orthogonal_direction_from_line_to_point

def interpolate_pts_np(pt1, pt2, num_pts):
  ts = np.linspace(0, 1, num_pts)
  traj_pts = np.array([pt1 * (1 - t) + pt2 * t for t in ts])
  return traj_pts

def make_ellipse(center, width, height):
  ellipse = Point(center).buffer(1.0)
  ellipse = scale(ellipse, xfact=width, yfact=height, origin=ellipse.centroid)
  return ellipse

def reverse_pts_np(traj_pts):
  return traj_pts[::-1]

def get_segmask_area(object_name):
    segmask = get_segmask(object_name)
    area = np.sum(segmask)
    return area

def make_hexagon(radius, center):
    hexagon_shape = Polygon([[center[0] + radius, center[1]],
                             [center[0] + radius / 2, center[1] + radius * np.sqrt(3) / 2],
                             [center[0] - radius / 2, center[1] + radius * np.sqrt(3) / 2],
                             [center[0] - radius, center[1]],
                             [center[0] - radius / 2, center[1] - radius * np.sqrt(3) / 2],
                             [center[0] + radius / 2, center[1] - radius * np.sqrt(3) / 2]])
    return hexagon_shape

def make_triangle(size, center):
    triangle_shape = Polygon([[0, 0], [size, 0], [size/2, size]])
    triangle_shape = translate(triangle_shape, xoff=center[0], yoff=center[1])
    return triangle_shape