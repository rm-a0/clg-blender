from .tile import Tile

class TileFactory:
    @classmethod
    def create_empty(elevation: float = 0) -> Tile:
        return Tile(definition=None, elevation=elevation)