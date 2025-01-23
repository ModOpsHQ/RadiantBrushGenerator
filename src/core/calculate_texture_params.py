from typing import Tuple
import math
from .vector_math import normalize, cross, dot, closest_axis

def calculate_texture_params(face_normal: Tuple[int, int, int], 
                           dimensions: Tuple[float, float, float],
                           position: Tuple[float, float, float],
                           rotation: Tuple[float, float, float]) -> str:
    """
    Calculate texture parameters based on face orientation and brush properties.
    Using Hammertime's texture alignment approach.
    
    Args:
        face_normal: Normal vector of the face (determines orientation)
        dimensions: (width, length, height) of the brush
        position: World position of the brush
        rotation: (x, y, z) rotation in degrees
    """
    # Normalize the face normal
    normal = normalize(face_normal)
    
    # Get closest major axis to this normal
    axis = closest_axis(normal)
    
    # Pick temporary vector based on closest axis
    # If closest is Z, use -Y, otherwise use -Z
    if axis[2] != 0:  # If Z is dominant
        temp_v = (0, -1, 0)  # -Y
    else:
        temp_v = (0, 0, -1)  # -Z
    
    # Calculate texture axes
    u_axis = normalize(cross(normal, temp_v))  # U = normal × temp
    v_axis = normalize(cross(u_axis, normal))  # V = U × normal
    
    # Calculate scale based on brush dimensions
    width, length, height = dimensions
    if face_normal[2] != 0:  # Top/Bottom faces
        scale_x = width
        scale_y = -length
    elif face_normal[0] != 0:  # Left/Right faces
        scale_x = length
        scale_y = -height
    else:  # Front/Back faces
        scale_x = width
        scale_y = -height
    
    # Calculate texture shift to center texture
    if face_normal[2] != 0:
        offset_x = width/2
        offset_y = -length/2
    elif face_normal[0] != 0:
        offset_x = length/2
        offset_y = -height/2
    else:
        offset_x = width/2
        offset_y = -height/2
    
    # Apply rotation based on texture axes
    tex_rotation = 0  # Let the texture axes handle rotation
    
    # Lightmap parameters
    lightmap_x = 0
    lightmap_y = 0
    lightmap_z = 0
    
    return f"{scale_x} {scale_y} {offset_x} {offset_y} {tex_rotation} 0 lightmap_gray 16384 16384 {lightmap_x} {lightmap_y} {lightmap_z} 0"