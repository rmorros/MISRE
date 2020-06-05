import numpy as np
from scipy.spatial import distance


# https://math.stackexchange.com/questions/723937/find-the-point-on-a-plane-3x-4y-z-1-that-is-closest-to-1-0-1
def closest_point_in_plane(plane_coefs, point):
    '''
    Find the point in the plane that is closest to point.
    Usage: 
       pp = closest_point_in_plane(plane_coefs, point)

    Parameters:
    plane_coefs:  coefficients of the plane equation ax+by+cz+d=0. Numpy array.
    point:         coordinates x,y,z of the point as numpy array

    Returns: closest point in plane (x,y,z)
    '''

    # Point in homogeneous coordinates
    hpoint = np.ones(4)
    hpoint[0:3] = point

    # Normal to the plane
    normal = plane_coefs[0:3]

    c = np.dot(plane_coefs, hpoint) / np.dot(plane_coefs[0:3], normal)
    closest_point = point + c * normal
    #distance = distance.euclidean(point,closest_point)
    distance = np.dot(point-closest_point, point-closest_point)  # Square error
    return closest_point, distance
    
def closest_points_in_plane (plane_coefs, points):
    num_points = points.shape[0]
    out = np.zeros(num_points)
    total_se = 0.0
    for ii in range(num_points):
        out[ii,:],se = closest_point_in_plane(plane_coefs, points[ii,:])
        total_se = total_se + se
    return out, np.sqrt(total_se/num_points)



