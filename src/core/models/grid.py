import logging
from dataclasses import dataclass
from .tile import Tile

@dataclass
class Grid:
    '''A 2D grid of tiles with bounds checking'''
    width: int
    height: int
    layout: list[list[Tile]]

    def in_bounds(self, x: int, y: int) -> bool:
        '''Check if coordinates are within grid bounds'''
        return 0 <= x < self.width and 0 <= y < self.height

    def set_tile(self, x: int, y: int, tile: Tile) -> None:
        '''Set a tile at specified coordinates in grid'''
        if self.in_bounds(x, y):
            self.layout[x][y] = tile
        else:
            logging.warning(f"Tile {tile.definition.name}out of bounds")

    def get_tile(self, x: int, y: int) -> Tile:
        '''Get tile at coordinates from the grid'''
        if self.in_bounds(x, y):
            return self.layout[x][y]
        else:
            logging.warning("Grid coordinates out of bounds")
