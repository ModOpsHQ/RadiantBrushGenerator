from typing import Tuple
from .calculate_texture_params import calculate_texture_params
from .rotate_point import rotate_point

def create_brush(width: float, length: float, height: float, 
                texture: str, 
                position: Tuple[float, float, float] = (0, 0, 0),
                rotation: Tuple[float, float, float] = (0, 0, 0)) -> str:
    """
    Create a brush with the specified dimensions, texture, position and rotation.
    Uses integer coordinates to avoid floating point precision issues.
    
    Args:
        width: Width of brush (X axis)
        length: Length of brush (Y axis)
        height: Height of brush (Z axis)
        texture: Texture name to apply
        position: (x, y, z) world position for brush center
        rotation: (x, y, z) rotation in degrees
    """
    # Round dimensions to integers
    width = round(width)
    length = round(length)
    height = round(height)
    pos_x, pos_y, pos_z = [round(p) for p in position]
    
    # Calculate half dimensions
    half_width = width // 2
    half_length = length // 2
    half_height = height // 2
    
    # Define vertices relative to origin (before rotation)
    vertices = [
        # For each face, define 3 points in counter-clockwise order
        (-half_width, -half_length, -half_height),  # Bottom face
        (half_width, -half_length, -half_height),
        (half_width, half_length, -half_height),
        (-half_width, half_length, -half_height),
        
        (-half_width, -half_length, half_height),   # Top face
        (half_width, -half_length, half_height),
        (half_width, half_length, half_height),
        (-half_width, half_length, half_height)
    ]
    
    # Rotate vertices if needed
    if any(r != 0 for r in rotation):
        vertices = [rotate_point(x, y, z, rotation) for x, y, z in vertices]
    
    # Move vertices to final position
    vertices = [(x + pos_x, y + pos_y, z + pos_z) for x, y, z in vertices]
    
    # Generate faces using rotated vertices
    faces = [
        # Bottom face (normal = 0 0 -1)
        f"( {vertices[2][0]} {vertices[2][1]} {vertices[2][2]} ) ( {vertices[3][0]} {vertices[3][1]} {vertices[3][2]} ) ( {vertices[0][0]} {vertices[0][1]} {vertices[0][2]} )",
        # Top face (normal = 0 0 1)
        f"( {vertices[4][0]} {vertices[4][1]} {vertices[4][2]} ) ( {vertices[7][0]} {vertices[7][1]} {vertices[7][2]} ) ( {vertices[6][0]} {vertices[6][1]} {vertices[6][2]} )",
        # Front face (normal = 0 -1 0)
        f"( {vertices[4][0]} {vertices[4][1]} {vertices[4][2]} ) ( {vertices[5][0]} {vertices[5][1]} {vertices[5][2]} ) ( {vertices[1][0]} {vertices[1][1]} {vertices[1][2]} )",
        # Right face (normal = 1 0 0)
        f"( {vertices[5][0]} {vertices[5][1]} {vertices[5][2]} ) ( {vertices[6][0]} {vertices[6][1]} {vertices[6][2]} ) ( {vertices[2][0]} {vertices[2][1]} {vertices[2][2]} )",
        # Back face (normal = 0 1 0)
        f"( {vertices[6][0]} {vertices[6][1]} {vertices[6][2]} ) ( {vertices[7][0]} {vertices[7][1]} {vertices[7][2]} ) ( {vertices[3][0]} {vertices[3][1]} {vertices[3][2]} )",
        # Left face (normal = -1 0 0)
        f"( {vertices[7][0]} {vertices[7][1]} {vertices[7][2]} ) ( {vertices[4][0]} {vertices[4][1]} {vertices[4][2]} ) ( {vertices[0][0]} {vertices[0][1]} {vertices[0][2]} )"
    ]
    
    # Face normals need to be rotated too
    base_normals = [
        (0, 0, -1),  # Bottom
        (0, 0, 1),   # Top
        (0, -1, 0),  # Front
        (1, 0, 0),   # Right
        (0, 1, 0),   # Back
        (-1, 0, 0)   # Left
    ]
    
    normals = [rotate_point(nx, ny, nz, rotation) for nx, ny, nz in base_normals]
    
    # Generate brush definition with calculated texture parameters
    brush_faces = []
    for vertex_str, normal in zip(faces, normals):
        tex_params = calculate_texture_params(normal, (width, length, height), position, rotation)
        brush_faces.append(f" {vertex_str} {texture} {tex_params}")
    
    return "{\n" + "\n".join(brush_faces) + "\n}"