from typing import Tuple
import math

Vec3 = Tuple[float, float, float]

def normalize(v: Vec3) -> Vec3:
    """Normalize a vector to unit length"""
    length = math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])
    if length == 0:
        return (0, 0, 0)
    return (v[0] / length, v[1] / length, v[2] / length)

def cross(a: Vec3, b: Vec3) -> Vec3:
    """Calculate cross product of two vectors"""
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    )

def dot(a: Vec3, b: Vec3) -> float:
    """Calculate dot product of two vectors"""
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def closest_axis(normal: Vec3) -> Vec3:
    """Find the closest major axis to a normal vector"""
    abs_x = abs(normal[0])
    abs_y = abs(normal[1]) 
    abs_z = abs(normal[2])
    
    if abs_x >= abs_y and abs_x >= abs_z:
        return (1, 0, 0) if normal[0] > 0 else (-1, 0, 0)
    elif abs_y >= abs_x and abs_y >= abs_z:
        return (0, 1, 0) if normal[1] > 0 else (0, -1, 0)
    else:
        return (0, 0, 1) if normal[2] > 0 else (0, 0, -1)
