import os

from src.core.create_brush import create_brush
from src.core.create_map_file import create_map_file

file = "s32_64_8_p0_0_0_r90_0_0_test2.map"
dir = r"D:\SteamLibrary\steamapps\common\Call of Duty World at War\map_source\brush_tests\python"
path = dir + "\\" + file
os.makedirs(dir, exist_ok=True)

def main():
    # Create two brushes at different world positions
    create_map_file([
        # create_brush(32,32,32, "berlin_roof_wood_dirty", position=(0,0,0), rotation=(0,0,0)),
        create_brush(32,64,8, "berlin_roof_wood_dirty", position=(0,0,0), rotation=(90,0,0)),
    ], path)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        print(f"Successfully created map: {path}")
