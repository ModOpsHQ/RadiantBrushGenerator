import os
from src.core.create_brush import create_brush
from src.core.create_map_file import create_map_file

file = "view_test.map"
dir = r"D:\SteamLibrary\steamapps\common\Call of Duty World at War\map_source\brush_tests\python"
path = dir + "\\" + file
os.makedirs(dir, exist_ok=True)

def main():
    # Create a brush with textures that match Radiant's 2D views
    create_map_file([
        create_brush(32,64,8, [
            "caulk",                        # Bottom (visible in top view)
            "berlin_roof_wood_dirty",       # Top (visible in top view)
            "atoll_ship_metal_rust2",       # Back (visible in front view, far)
            "atoll_ship_metal_rust1",       # Right (visible in side view)
            "berlin_ceiling_concrete_tile", # Front (visible in front view, near)
            "atoll_ship_metal_ribs_blend"   # Left (visible in side view)
        ], position=(0,0,0), rotation=(0,0,0)),
        create_brush(32,64,8, [
            "caulk",                        # Bottom (visible in top view)
            "berlin_roof_wood_dirty",       # Top (visible in top view)
            "atoll_ship_metal_rust2",       # Back (visible in front view, far)
            "atoll_ship_metal_rust1",       # Right (visible in side view)
            "berlin_ceiling_concrete_tile", # Front (visible in front view, near)
            "atoll_ship_metal_ribs_blend"   # Left (visible in side view)
        ], position=(256,0,0), rotation=(90,0,0)),
        create_brush(32,64,8, [
            "caulk",                        # Bottom (visible in top view)
            "berlin_roof_wood_dirty",       # Top (visible in top view)
            "atoll_ship_metal_rust2",       # Back (visible in front view, far)
            "atoll_ship_metal_rust1",       # Right (visible in side view)
            "berlin_ceiling_concrete_tile", # Front (visible in front view, near)
            "atoll_ship_metal_ribs_blend"   # Left (visible in side view)
        ], position=(0,256,0), rotation=(0,90,0)),
        create_brush(32,64,8, [
            "caulk",                        # Bottom (visible in top view)
            "berlin_roof_wood_dirty",       # Top (visible in top view)
            "atoll_ship_metal_rust2",       # Back (visible in front view, far)
            "atoll_ship_metal_rust1",       # Right (visible in side view)
            "berlin_ceiling_concrete_tile", # Front (visible in front view, near)
            "atoll_ship_metal_ribs_blend"   # Left (visible in side view)
        ], position=(0,0,256), rotation=(0,0,90))

    ], path)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        print(f"Successfully created map: {path}")
