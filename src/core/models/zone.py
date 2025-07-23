from dataclasses import dataclass
from enum import Enum

class ZoneType(Enum):
    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"
    INDUSTRIAL = "industrial"

class PathAlgorithm(Enum):
    NONE = "none"
    VORONOI = "voronoi"
    AI = "ai"

class StructureAlgorithm(Enum):
    NONE = "none"
    GRID = "grid"
    RADIAL = "radial"
    AI = "ai"

@dataclass
class ZoneDefinition:
    id: int
    type: ZoneType
    name: str
    frequency: float
    path_algorithm: PathAlgorithm = PathAlgorithm.NONE
    structure_algorithm: StructureAlgorithm = StructureAlgorithm.NONE

@dataclass
class Zone:
    definition: ZoneDefinition