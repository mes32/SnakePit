
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
