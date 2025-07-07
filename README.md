# Overview
This is a Blender add-on that enables users to create city layouts by organizing pre-created meshes or collections into a customizable grid-based structure.

> [!NOTE]  
> The core logic of this add-on was based on my [Lua script for procedural 2D city generation and visualization](https://github.com/rm-a0/city-sim), ported to Python for seamless integration with Blender’s API.

# Installation
1. **Download the Add-On:**
  - Clone the repository: 
      ```bash
      git clone https://github.com/rm-a0/clg-blender.git
      ```
  - Or download the latest release as a .zip file from the Releases page.

2. **Install in Blender:**
  - Open Blender (version 4.2 or later recommended).
  - Go to `Edit > Preferences > Add-ons`.
  - Click `Install`, select the clg-blender.zip or the folder’s `__init__.py`, and click `Install Add-on`.
  - Enable the add-on by checking the box next to "Add Mesh: CityLayout Generator".

3. **Dependencies:**
  - No external dependencies required; uses Blender’s built-in Python API.

# Implementation Details
## Code Structure
```
src/
├── ui/                       # User Interface
│   ├── panels.py
│   ├── operators.py
│   ├── properties.py
│   └── helpers.py
├── core/                     # Core logic
│   ├── generator.py
├── ai/                       # AI models and trainers 
│   ├── trainer.py
│   └── data/
├── tilesets/                 # User defined tiles
│   ├── registry.py
│   └── validators.py
├── utils/                    # Utilities
│   ├── geometry.py
│   ├── noise.py
│   └── blender_utils.py
└── test/                     # Tests
```