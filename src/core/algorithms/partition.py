import numpy as np
from typing import List, Tuple, Dict

class Partition:
    @classmethod
    def voronoi_random(cls, width: int, height: int, num_zones: int) -> Dict[int, List[Tuple[int, int]]]:
        '''
        Partitions a grid into 'num_zones' voronoi zones using manhattan distance and random seed
        '''
        seeds = []
        for _ in range(num_zones):
            x = np.random.randint(1, width + 1)
            y = np.random.randint(1, height + 1)
            seeds.append((x, y))

        x_grid, y_grid = np.meshgrid(np.arrange(1, width + 1), np.arrange(1, height + 1))
        distances = np.empty((height, width, num_zones))

        for i, (sx, sy) in enumerate(seeds):
            distances[..., i] = np.abs(x_grid - sx) + np.abs(y_grid - sy)

        zones = np.argmin(distances, axis=-1)
        zones_dict = {i: [] for i in range(num_zones)}

        for y in range(height):
            for x in range(width):
                zone_id = zones[x, y]
                zones_dict[zone_id].append((x + 1, y + 1))

        return zones_dict