from dataclasses import dataclass
from .models.grid import Grid
from .models.tile_manager import TileManager
from .algorithms.noise import Noise
from .models.tile_registry import TileDefinitionRegistry
from .models.tile import TileType

@dataclass
class GeneratorConfig:
    '''Configuration required for proper generator initialization'''
    width: int = 100
    height: int = 100
    terrain_intensity: float = 0.0
    lake_frequency: float = 0.5
    river_frequency: float = 0.5

class Generator:
    '''Orchestrates procedural generation algorithms on a grid'''
    def __init__(self, config: GeneratorConfig):
        self.config = config
        layout = [[TileManager.create_empty() for _ in range(config.width)] for _ in range(config.height)]
        self.grid = Grid(config.width, config.height, layout)

    def generate_terrain(self) -> None:
        '''Generates terrain using perlin noise for elevation'''
        water_threshold = self.config.lake_frequency

        for y in range(self.grid.height):
            for x in range(self.grid.width):
                raw_noise = Noise.perlin_noise(x, y, scale=0.1)
                elevation = raw_noise * self.config.terrain_intensity
                if elevation <= water_threshold:
                    tile = TileManager.create_default_tile(TileType.WATER, elevation=water_threshold)
                else:
                    tile = TileManager.create_default_tile(TileType.PATH, elevation=elevation)
                self.grid.set_tile(x, y, tile)

    def generate_zones(self) -> None:
        '''TODO'''
        pass

    def generate_rivers(self) -> None:
        '''TODO'''
        pass

    def generate_paths(self) -> None:
        '''TODO'''
        pass

    def generate_structures(self) -> None:
        '''TODO'''
        pass
