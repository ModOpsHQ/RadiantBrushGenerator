from typing import Tuple
import math

def calculate_face_angle(normal: Tuple[int, int, int], rotation: Tuple[float, float, float]) -> float:
    """Calculate the angle of a face after rotation"""
    # Convert rotation to radians
    rx, ry, rz = [math.radians(r) for r in rotation]
    
    # Create rotation matrices
    def rot_x(v):
        y = v[1] * math.cos(rx) - v[2] * math.sin(rx)
        z = v[1] * math.sin(rx) + v[2] * math.cos(rx)
        return (v[0], y, z)
    
    def rot_y(v):
        x = v[0] * math.cos(ry) + v[2] * math.sin(ry)
        z = -v[0] * math.sin(ry) + v[2] * math.cos(ry)
        return (x, v[1], z)
    
    def rot_z(v):
        x = v[0] * math.cos(rz) - v[1] * math.sin(rz)
        y = v[0] * math.sin(rz) + v[1] * math.cos(rz)
        return (x, y, v[2])
    
    # Apply rotations in sequence
    rotated = normal
    rotated = rot_x(rotated)
    rotated = rot_y(rotated)
    rotated = rot_z(rotated)
    
    # Calculate angle in XY plane
    angle = math.degrees(math.atan2(rotated[1], rotated[0]))
    return angle
