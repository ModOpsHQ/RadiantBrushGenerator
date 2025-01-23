from typing import Tuple

def calculate_texture_params(face_normal: Tuple[int, int, int], 
                           dimensions: Tuple[float, float, float],
                           position: Tuple[float, float, float],
                           rotation: Tuple[float, float, float]) -> str:
    """
    Calculate texture parameters based on face orientation and brush properties.
    
    Args:
        face_normal: Normal vector of the face (determines orientation)
        dimensions: (width, length, height) of the brush
        position: World position of the brush
        rotation: (x, y, z) rotation in degrees
    """
    width, length, height = dimensions
    
    # Scale is based on brush dimensions
    scale_x = width
    scale_y = -height  # Negative because Radiant uses opposite Y direction
    
    # Offset is half of the dimensions
    offset_x = width/2
    offset_y = -height/2  # Negative to match Radiant's coordinate system
    
    # Calculate texture rotation based on face normal and brush rotation
    rx, ry, rz = rotation
    
    # Base rotation is 180 for standard orientation
    tex_rotation = 180
    
    # Adjust texture rotation based on which face it is and the brush rotation
    if face_normal[2] != 0:  # Top/Bottom faces
        tex_rotation = (tex_rotation + rz) % 360  # Z rotation affects top/bottom faces
    elif face_normal[0] != 0:  # Left/Right faces
        tex_rotation = (tex_rotation + ry) % 360  # Y rotation affects side faces
    else:  # Front/Back faces
        tex_rotation = (tex_rotation + rx) % 360  # X rotation affects front/back
    
    # Lightmap offsets based on face orientation
    if face_normal[0] != 0:  # X-facing faces
        lightmap_x = 0
        lightmap_y = 0
        lightmap_z = 0
    else:  # Y and Z facing faces
        lightmap_x = -width * 3  # Proportional to brush width
        lightmap_y = 0
        lightmap_z = 0
    
    return f"{scale_x} {scale_y} {offset_x} {offset_y} {tex_rotation} 0 lightmap_gray 16384 16384 {lightmap_x} {lightmap_y} {lightmap_z} 0"