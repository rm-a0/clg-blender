from dataclasses import dataclass
from enum import Enum
from typing import Optional

class TileType(Enum):
    WATER = "water"
    ROAD = "road"
    BUILDING = "building"

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
    elevation: float
