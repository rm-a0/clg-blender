from typing import Dict, Optional, List
from .tile import TileType, TileDefinition

class TileDefinitionRegistry:
    '''Singleton registry for managing tile definitions'''
    _instance = None
    _definitions: Dict[int, TileDefinition] = {}
    _next_id: int = 1

    def __new__(cls):
        '''Ensures singleton instance of the registry'''
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._definitions = {}
            cls._next_id = 1
            cls._init_defaults()
        return cls._instance
    
    @classmethod
    def _init_defaults(cls):
        for tile_type in TileType:
            cls.add_definition(
                type=tile_type,
                name=f"Default {tile_type.name.title()}",
                width=0.0,
                height=0.0,
                is_default=True
            )

    @classmethod
    def add_definition(cls, type: TileType, name: str, width: float, height: float, is_default: bool = False) -> TileDefinition:
        '''Add a tile definition and return it'''
        definition = TileDefinition(
            id=cls._next_id, 
            type=type, 
            name=name, 
            width=width, 
            height=height, 
            is_default=is_default
        )
        cls._definitions[cls._next_id] = definition
        cls._next_id += 1
        return definition

    @classmethod
    def get_by_id(cls, id: int) -> Optional[TileDefinition]:
        '''Get a tile definition by ID'''
        return cls._definitions.get(id)

    @classmethod
    def get_by_name(cls, name: str) -> Optional[TileDefinition]:
        '''Get a tile definition by name'''
        for defn in cls._definitions.values():
            if defn.name == name:
                return defn
        return None
    
    @classmethod
    def get_all_by_type(cls, type: TileType) -> List[TileDefinition]:
        '''Returns all tiles with specified type (except default)'''
        tile_list = []
        for defn in cls._definitions.values():
            if defn.type == type and defn.is_default == False:
                tile_list.append(defn)
        return tile_list

    @classmethod
    def remove_definition(cls, id: int) -> None:
        '''Remove tile definition by ID'''
        cls._definitions.pop(id, None)
        cls._sync_next_id()

    @classmethod
    def has_type(cls, type: TileType) -> bool:
        '''Check if registry has a tile of specified type (except default)'''
        for defn in cls._definitions.values():
            if defn.type == type and defn.is_default == False:
                return True
        return False
    
    @classmethod
    def get_default_by_type(cls, type: TileType) -> Optional[TileDefinition]:
        '''Return default definition of a specified type'''
        for defn in cls._definitions.values():
            if defn.is_default and defn.type == type:
                return defn
        return None