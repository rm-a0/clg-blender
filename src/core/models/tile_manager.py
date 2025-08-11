from .tile import Tile, TileType
from .tile_registry import TileDefinitionRegistry

class TileManager:
    '''Static namespace for tile creation and modification methods'''
    @classmethod
    def create_default_tile(cls, tile_type: TileType, elevation: float = 0.0) -> Tile:
        '''Create tile with default definition'''
        default_def = cls.get_default_by_type(tile_type)
        if default_def is None:
            raise ValueError(f"No default tile found for type '{tile_type}'")
        return Tile(definition=default_def, elevation=elevation)

    @classmethod
    def create_tile_by_name(cls, def_name: str, elevation: float = 0.0) -> Tile:
        '''Create tile with definition defined by its name'''
        definition = TileDefinitionRegistry.get_definition_by_name(def_name)
        if definition is None:
            raise ValueError(f"TileDefinition with name '{def_name}' not found")
        return Tile(definition=definition, elevation=elevation)
    
    @classmethod
    def plug_def_by_name(cls, tile: Tile, def_name: str) -> None:
        '''Changes definition in the tile for a new one specified by its name'''
        definition = TileDefinitionRegistry.get_definition_by_name(def_name)
        if definition is None:
            raise ValueError(f"TileDefinition with name '{def_name}' not found")
        tile.definition = definition

    @classmethod
    def unplug_def(cls, tile: Tile) -> None:
        '''Removes definition from the tile'''
        tile.definition = None
