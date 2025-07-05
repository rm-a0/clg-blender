bl_info = {
    "name": "Semi-Procedural City Generator",
    "author": "rm-a0",
    "description": "Generate procedural city layouts using tile-based mesh placement",
    "version": (0, 1, 0),
    "blender": (3, 0, 0),
    "location": "View3D -> Sidebar -> CityGen",
    "category": "Object"
}

import bpy

from src.ui import panels

def register():
    panels.register()

def unregister():
    panels.unregister()

if __name__ == "__main__":
    register()