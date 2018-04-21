import random

import position_map

class TerrainMap(position_map.PositionMap):
    """
    A mapping of of Terrain tiles inside the GameLevel
    """

    def is_vacant(self, position):
        if self.entity_at(position) == None or self.entity_at(position).is_walkable():
            return True
        else:
            return False

    def rand_vacant(self):
        terrain_list = self.get_list()
        index = random.randint(0, len(terrain_list) - 1)
        return terrain_list[index].position
