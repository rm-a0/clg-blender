TODO List

- [ ] Create UI and user input
  - [ ] Allow user to select meshes/collections and assign types for them
    - [ ] Define tile types (water, road, building, ...)
  - [ ] Allow user to set main setting for generation
    - [ ] Grid size (width and height in tiles)
    - [ ] Strength of terrain generation (adjust elevation)
    - [ ] Water generation (frequency)
        - [ ] Lake generation
        - [ ] River generation
    - [ ] Main road generation (frequency, spacing, algorithm)
  - [ ] Allow user to add and define zones (different parts of the city)
    - [ ] Frequency (how often certain type of zone appears)
    - [ ] Allowed tiles (tiles that can be generated inside the zone)
    - [ ] Secondary road generation algorithm (none, voronoi diagrams, ai, ...)
    - [ ] Building generation algorithm (none, grid, radial, ai, ...)

- [ ] Rewrite [Lua modules](https://github.com/rm-a0/city-sim) to Python code
- [ ] Add AI for road generation (train on satellite images from cities or something)
- [ ] Add generation for different tile shapes (hexagonal, triangular)