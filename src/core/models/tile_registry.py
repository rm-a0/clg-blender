from typing import Dict, Optional
from .tile import TileType, TileDefinition

class TileDefinitionRegistry:
    _instance = None
    _definitions: Dict[int, TileDefinition] = {}
    _next_id: int = 1

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._definitions = {}
            cls._next_id = 1
        return cls._instance

    @classmethod
    def add_definition(cls, type: TileType, name: str, width: float, height: float) -> TileDefinition:
        definition = TileDefinition(id=cls._next_id, type=type, name=name, width=width, height=height)
        cls._definitions[cls._next_id] = definition
        cls._next_id += 1
        return definition

    @classmethod
    def get_definition(cls, id: int) -> Optional[TileDefinition]:
        return cls._definitions.get(id)

    @classmethod
    def get_definition_by_name(cls, name: str) -> Optional[TileDefinition]:
        for defn in cls._definitions.values():
            if defn.name == name:
                return defn
        return None

    @classmethod
    def remove_definition(cls, id: int) -> None:
        cls._definitions.pop(id, None)
        cls._sync_next_id()