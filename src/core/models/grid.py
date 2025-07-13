import logging
from dataclasses import dataclass
from .tile import Tile

@dataclass
class Grid:
    width: int
    height: int
    layout: list[list[Tile]]

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def set_tile(self, x: int, y: int, tile: Tile) -> None:
        if self.in_bounds(x, y):
            self.layout[x][y] = tile
        else:
            logging.warning(f"Tile {tile.definition.name}out of bounds")

    def get_tile(self, x: int, y: int) -> Tile:
        if self.in_bounds(x, y):
            return self.layout[x][y]
        else:
            logging.warning("Grid coordinates out of bounds")
