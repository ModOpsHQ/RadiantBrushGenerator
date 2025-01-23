from typing import Tuple
import math
from .calculate_face_angle import calculate_face_angle

def calculate_scale_factor(normal: Tuple[int, int, int], rotation: Tuple[float, float, float], dimensions: Tuple[float, float, float]) -> Tuple[float, float]:
    """Calculate texture scale based on face orientation and dimensions"""
    width, length, height = dimensions
    
    # Get the rotated face angle
    angle = calculate_face_angle(normal, rotation)
    
    # Base scale (from 32-unit brush example)
    base_scale = 32.0
    
    # Calculate projected dimensions based on face orientation and rotation
    if normal[2] != 0:  # Top/bottom faces
        # Scale based on rotated width/length
        cos_angle = abs(math.cos(math.radians(angle)))
        sin_angle = abs(math.sin(math.radians(angle)))
        scale_x = base_scale * (cos_angle * width/32 + sin_angle * length/32)
        scale_y = base_scale * (cos_angle * length/32 + sin_angle * width/32)
    else:  # Side faces
        # Scale based on height and rotated width/depth
        if normal[0] != 0:  # X-facing
            scale_x = base_scale * (length/32)
            scale_y = base_scale * (height/32)
        else:  # Y-facing
            scale_x = base_scale * (width/32)
            scale_y = base_scale * (height/32)
    
    return scale_x, -scale_y  # Negative Y scale from example
