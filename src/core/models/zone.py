from dataclasses import dataclass
from enum import Enum

class ZoneType(Enum):
    '''Enum for different zone types''' 
    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"
    INDUSTRIAL = "industrial"

class PathAlgorithm(Enum):
    '''Enum for different path generation algorithms''' 
    NONE = "none"
    VORONOI = "voronoi"
    AI = "ai"

class StructureAlgorithm(Enum):
    '''Enum for different structure generation algorithms''' 
    NONE = "none"
    GRID = "grid"
    RADIAL = "radial"
    AI = "ai"

@dataclass
class ZoneDefinition:
    '''Definition of a zone'''
    id: int
    type: ZoneType
    name: str
    frequency: float
    path_algorithm: PathAlgorithm = PathAlgorithm.NONE
    structure_algorithm: StructureAlgorithm = StructureAlgorithm.NONE

@dataclass
class Zone:
    '''Zone instance'''
    definition: ZoneDefinition