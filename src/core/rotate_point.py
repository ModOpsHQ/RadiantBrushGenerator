from typing import Tuple
import math

def rotate_point(x: int, y: int, z: int, rotation: Tuple[float, float, float]) -> Tuple[int, int, int]:
    """
    Rotate a point in 3D space using integer coordinates.
    Args:
        x, y, z: Point coordinates
        rotation: (x, y, z) rotation in degrees
    """
    rx, ry, rz = [math.radians(r) for r in rotation]
    
    # Rotate around X axis
    if rx:
        new_y = round(y * math.cos(rx) - z * math.sin(rx))
        new_z = round(y * math.sin(rx) + z * math.cos(rx))
        y, z = new_y, new_z
    
    # Rotate around Y axis
    if ry:
        new_x = round(x * math.cos(ry) + z * math.sin(ry))
        new_z = round(-x * math.sin(ry) + z * math.cos(ry))
        x, z = new_x, new_z
    
    # Rotate around Z axis
    if rz:
        new_x = round(x * math.cos(rz) - y * math.sin(rz))
        new_y = round(x * math.sin(rz) + y * math.cos(rz))
        x, y = new_x, new_y
    
    return (x, y, z)
