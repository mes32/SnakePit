
import position_map

class TerrainMap(position_map.PositionMap):
    """
    A mapping of of Terrain tiles inside the GameLevel
    """

    def is_walkable(self, position):
        return self.entity_at(position).is_walkable()

    def is_open(self, position):
        if self.entity_at(position).is_walkable() and self.entity_at(position).open:
            return True
        return False
