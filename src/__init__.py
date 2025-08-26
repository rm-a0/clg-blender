bl_info = {
    "name": "Semi-Procedural City Generator",
    "author": "rm-a0",
    "description": "Generate procedural city layouts using tile-based mesh placement",
    "version": (0, 1, 0),
    "blender": (3, 0, 0),
    "location": "View3D -> Sidebar -> CityGen",
    "category": "Object"
}

import sys
import os

addon_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(addon_dir, "libs"))

try:
    import numpy as np
except ImportError:
    print("NumPy not found in addon_libs. Please ensure it is bundled correctly.")
    raise

from .ui import panels, operators, properties

def register():
    properties.register()
    operators.register()
    panels.register()

def unregister():
    panels.unregister()
    operators.unregister()
    properties.unregister()

if __name__ == "__main__":
    register()