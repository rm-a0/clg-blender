TODO List

- [ ] Create UI and user input
  - [x] Allow user to select meshes/collections and assign types for them
    - [x] Define tile types (water, road, building, ...)
  - [x] Allow user to set main setting for generation
    - [x] Grid size (width and height in tiles)
    - [x] Strength of terrain generation (adjust elevation)
    - [x] Water generation (frequency)
        - [x] Lake generation
        - [x] River generation
    - [x] Main road generation (frequency, spacing, algorithm)
  - [x] Allow user to add and define zones (different parts of the city)
    - [x] Frequency (how often certain type of zone appears)
    - [x] Allowed tiles (tiles that can be generated inside the zone)
    - [x] Secondary road generation algorithm (none, voronoi diagrams, ai, ...)
    - [x] Building generation algorithm (none, grid, radial, ai, ...)
  - [ ] Allow user to select connection points for tiles and select meshes it "must" be connected to

- [ ] Rewrite [Lua modules](https://github.com/rm-a0/city-sim) to Python code
- [ ] Add AI for road generation (train on satellite images from cities or something)
- [ ] Add generation for different tile shapes (hexagonal, triangular)