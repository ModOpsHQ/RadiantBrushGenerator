from typing import Tuple, Union, List
from .calculate_texture_params import calculate_texture_params
from .rotate_point import rotate_point

def create_brush(width: float, length: float, height: float, 
                texture: Union[str, List[str]], 
                position: Tuple[float, float, float] = (0, 0, 0),
                rotation: Tuple[float, float, float] = (0, 0, 0)) -> str:
    """
    Create a brush with the specified dimensions, texture(s), position and rotation.
    Uses integer coordinates to avoid floating point precision issues.
    
    Args:
        width: Width of brush (X axis)
        length: Length of brush (Y axis)
        height: Height of brush (Z axis)
        texture: Either a single texture name for all faces, or a list of 6 textures in order:
                [Bottom, Top, Front, Right, Back, Left]
        position: (x, y, z) world position for brush center
        rotation: (x, y, z) rotation in degrees
    """
    # Round dimensions to integers
    width = round(width)
    length = round(length)
    height = round(height)
    pos_x, pos_y, pos_z = [round(p) for p in position]
    
    # Handle texture input
    if isinstance(texture, str):
        textures = [texture] * 6
    else:
        if len(texture) != 6:
            raise ValueError("If providing multiple textures, must provide exactly 6 (one per face)")
        textures = texture
    
    # Calculate half dimensions
    half_width = width // 2
    half_length = length // 2
    half_height = height // 2
    
    # Define vertices relative to origin
    vertices = [
        (-half_width, -half_length, -half_height),  # 0 bottom front left
        (half_width, -half_length, -half_height),   # 1 bottom front right
        (half_width, half_length, -half_height),    # 2 bottom back right
        (-half_width, half_length, -half_height),   # 3 bottom back left
        (-half_width, -half_length, half_height),   # 4 top front left
        (half_width, -half_length, half_height),    # 5 top front right
        (half_width, half_length, half_height),     # 6 top back right
        (-half_width, half_length, half_height)     # 7 top back left
    ]
    
    # Rotate vertices if needed
    if any(r != 0 for r in rotation):
        vertices = [rotate_point(x, y, z, rotation) for x, y, z in vertices]
    
    # Move vertices to final position
    vertices = [(x + pos_x, y + pos_y, z + pos_z) for x, y, z in vertices]
    
    # Generate faces using rotated vertices
    # Order vertices to maintain consistent winding order after rotation
    # Each face is defined by 3 vertices in counter-clockwise order when looking at the face from outside
    faces = [
        # Bottom face - CCW looking down at bottom (visible in top view)
        f"( {vertices[0][0]} {vertices[0][1]} {vertices[0][2]} ) ( {vertices[1][0]} {vertices[1][1]} {vertices[1][2]} ) ( {vertices[2][0]} {vertices[2][1]} {vertices[2][2]} )",
        
        # Top face - CCW looking down at top (visible in top view)
        f"( {vertices[4][0]} {vertices[4][1]} {vertices[4][2]} ) ( {vertices[7][0]} {vertices[7][1]} {vertices[7][2]} ) ( {vertices[6][0]} {vertices[6][1]} {vertices[6][2]} )",
        
        # Back face - CCW looking at back (visible in front view, far)
        f"( {vertices[2][0]} {vertices[2][1]} {vertices[2][2]} ) ( {vertices[6][0]} {vertices[6][1]} {vertices[6][2]} ) ( {vertices[7][0]} {vertices[7][1]} {vertices[7][2]} )",
        
        # Right face - CCW looking at right (visible in side view)
        f"( {vertices[1][0]} {vertices[1][1]} {vertices[1][2]} ) ( {vertices[5][0]} {vertices[5][1]} {vertices[5][2]} ) ( {vertices[6][0]} {vertices[6][1]} {vertices[6][2]} )",
        
        # Front face - CCW looking at front (visible in front view, near)
        f"( {vertices[0][0]} {vertices[0][1]} {vertices[0][2]} ) ( {vertices[4][0]} {vertices[4][1]} {vertices[4][2]} ) ( {vertices[5][0]} {vertices[5][1]} {vertices[5][2]} )",
        
        # Left face - CCW looking at left (visible in side view)
        f"( {vertices[3][0]} {vertices[3][1]} {vertices[3][2]} ) ( {vertices[7][0]} {vertices[7][1]} {vertices[7][2]} ) ( {vertices[4][0]} {vertices[4][1]} {vertices[4][2]} )"
    ]
    
    # Face normals after rotation
    base_normals = [
        (0, 0, -1),  # Bottom (points down)
        (0, 0, 1),   # Top (points up)
        (0, 1, 0),   # Back (points away in front view)
        (1, 0, 0),   # Right (points right in side view)
        (0, -1, 0),  # Front (points toward in front view)
        (-1, 0, 0)   # Left (points left in side view)
    ]
    
    # Generate brush definition with calculated texture parameters
    brush_faces = []
    for vertex_str, normal, tex in zip(faces, base_normals, textures):
        tex_params = calculate_texture_params(normal, (width, length, height), position, rotation)
        brush_faces.append(f" {vertex_str} {tex} {tex_params}")
    
    return "{\n" + "\n".join(brush_faces) + "\n}"