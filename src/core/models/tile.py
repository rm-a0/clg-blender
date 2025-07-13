from dataclasses import dataclass
from typing import Tuple
from enum import Enum

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
    definition: TileDefinition
    elevation: float
