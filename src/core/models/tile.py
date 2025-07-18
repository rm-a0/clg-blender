from dataclasses import dataclass
from enum import Enum
from typing import Optional

class TileType(Enum):
    PATH = "path"
    WATER = "water"
    STRUCTURE = "structure"
    DECORATION = "decoration"

@dataclass
class TileDefinition:
    id: int
    type: TileType
    name: str 
    width: float
    height: float

@dataclass
class Tile:
    definition: Optional[TileDefinition] = None
    elevation: float = 0.0
