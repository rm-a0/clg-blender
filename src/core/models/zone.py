from dataclasses import dataclass
from enum import Enum

class ZoneType(Enum):
    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"
    INDUSTRIAL = "industrial"

class RoadAlgorithm(Enum):
    NONE = "none"
    VORONOI = "voronoi"
    AI = "ai"

class BuildingAlgorithm(Enum):
    NONE = "none"
    GRID = "grid"
    RADIAL = "radial"
    AI = "ai"

@dataclass
class ZoneDefinition:
    id: int
    type: ZoneType
    frequency: float
    road_algorithm: RoadAlgorithm = RoadAlgorithm.NONE
    building_algorithm: BuildingAlgorithm = BuildingAlgorithm.NONE

@dataclass
class Zone:
    definition: ZoneDefinition