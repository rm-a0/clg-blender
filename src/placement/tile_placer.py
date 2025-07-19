import bpy
from ..core.models.grid import Grid

class TilePlacer:
    def __init__(self, grid: Grid, tile_collection: bpy.props.CollectionProperty):
        self.grid = grid
        self.tile_map = {tile.name: tile for tile in tile_collection}

    def copy_bl_tile(self): # return bl tile copy
        pass

    def place_tiles(self) -> None:
        bpy.ops.object.select_all(action='DESELECT')

        for row in range(self.grid.width):
            for col in range(self.grid.height):
                tile_name = self.grid.get_tile(row, col).definition.name

                if not tile_name or tile_name not in self.tile_map:
                    continue

                bl_tile = self.tile_map[tile_name]

