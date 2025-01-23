from typing import Tuple, List
import math

def rotate_point(x: int, y: int, z: int, rotation: Tuple[float, float, float]) -> Tuple[int, int, int]:
    """
    Rotate a point in 3D space using integer coordinates.
    Applies rotations one at a time in X, Y, Z order.
    Args:
        x, y, z: Point coordinates
        rotation: (x, y, z) rotation in degrees
    """
    rx, ry, rz = rotation
    point = (x, y, z)
    
    # Apply X rotation first
    if rx != 0:
        rx_rad = math.radians(rx)
        cos_rx = math.cos(rx_rad)
        sin_rx = math.sin(rx_rad)
        x, y, z = point
        new_y = round(y * cos_rx - z * sin_rx)
        new_z = round(y * sin_rx + z * cos_rx)
        point = (x, new_y, new_z)
    
    # Then Y rotation (note: negative angle to match Radiant's direction)
    if ry != 0:
        ry_rad = math.radians(-ry)  # Negative to match Radiant
        cos_ry = math.cos(ry_rad)
        sin_ry = math.sin(ry_rad)
        x, y, z = point
        new_x = round(x * cos_ry + z * sin_ry)
        new_z = round(-x * sin_ry + z * cos_ry)
        point = (new_x, y, new_z)
    
    # Finally Z rotation
    if rz != 0:
        rz_rad = math.radians(rz)
        cos_rz = math.cos(rz_rad)
        sin_rz = math.sin(rz_rad)
        x, y, z = point
        new_x = round(x * cos_rz - y * sin_rz)
        new_y = round(x * sin_rz + y * cos_rz)
        point = (new_x, new_y, z)
    
    return point
