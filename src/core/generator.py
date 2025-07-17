from dataclasses import dataclass
from .models.grid import Grid
from .models.tile_factory import TileFactory
from .algorithms.noise import Noise

@dataclass
class GeneratorConfig:
    width: int = 100
    height: int = 100
    terrain_intensity: float = 0.0
    lake_frequency: float = 0.5
    river_frequency: float = 0.5

class Generator:
    def __init__(self, config: GeneratorConfig):
        self.config = config
        layout = [[TileFactory.create_empty() for _ in range(config.width)] for _ in range(config.height)]
        self.grid = Grid(config.width, config.height, layout)

    def generate_terrain(self):
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                elevation = Noise.perlin_noise(x, y)
                self.grid.set_tile(x, y, TileFactory.create_empty(elevation)) 