from dataclasses import dataclass
from enum import Enum
from typing import Optional

class TileType(Enum):
    '''Enum for different tile types''' 
    LAND= "land"
    PATH = "path"
    WATER = "water"
    STRUCTURE = "structure"
    DECORATION = "decoration"

@dataclass
class TileDefinition:
    '''Definition of a tile'''
    id: int
    type: TileType
    name: str 
    width: float
    height: float
    is_default: bool

@dataclass
class Tile:
    '''Tile instance'''
    definition: Optional[TileDefinition] = None
    elevation: float = 0.0
