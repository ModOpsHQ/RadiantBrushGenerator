def create_map_file(brushes: list[str], output_file: str):
    """Create a complete .map file with the given brushes"""
    map_content = '''iwmap 4
"000_Global" flags  active
"The Map" flags 
// entity 0
{
"classname" "worldspawn"
'''
    
    for i, brush in enumerate(brushes):
        map_content += f"// brush {i}\n{brush}\n"
    
    map_content += "}\n"
    
    with open(output_file, 'w') as f:
        f.write(map_content)