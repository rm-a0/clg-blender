from .tile import Tile
from .tile_registry import TileDefinitionRegistry

class TileManager:
    @classmethod
    def create_empty(cls, elevation: float = 0.0) -> Tile:
        return Tile(definition=None, elevation=elevation)
    
    @classmethod
    def create_tile_by_name(cls, def_name: str, elevation: float = 0.0) -> Tile:
        definition = TileDefinitionRegistry.get_definition_by_name(def_name)
        if definition is None:
            raise ValueError(f"TileDefinition with name '{def_name}' not found")
        return Tile(definition=definition, elevation=elevation)
    
    @classmethod
    def plug_def_by_name(cls, tile: Tile, def_name: str) -> None:
        definition = TileDefinitionRegistry.get_definition_by_name(def_name)
        if definition is None:
            raise ValueError(f"TileDefinition with name '{def_name}' not found")
        tile.definition = definition

    @classmethod
    def unplug_def(cls, tile: Tile) -> None:
        tile.definition = None
