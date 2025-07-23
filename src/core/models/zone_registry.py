from .zone import ZoneDefinition, ZoneType, PathAlgorithm, StructureAlgorithm
from typing import Dict

class ZoneDefinitionRegistry:
    _instance = None
    _definitions: Dict[int, ZoneDefinition] = {}
    _next_id: int = 1

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._definitions = {}
            cls._next_id = 1
        return cls._instance
    
    @classmethod
    def add_definition(cls, 
                       type: ZoneType, 
                       name: str, 
                       frequency: float, 
                       path_algorithm: PathAlgorithm, 
                       structure_algorithm: StructureAlgorithm ) -> ZoneDefinition:
        definition = ZoneDefinition(cls._next_id, type, name, frequency, path_algorithm, structure_algorithm)
        cls._definitions[cls._next_id] = definition
        cls._next_id += 1
        return definition