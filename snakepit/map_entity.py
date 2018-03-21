import position
import position_map

class MapEntity():
    """
    Game objects that can be placed on the map.
    """

    def __init__(self, position_lookup, position):
        self.position_lookup = position_lookup
        self.position = position
        self.position_lookup.insert(position, self)

    def move_position(self, new_position):
        self.position.move(new_position)
        self.position = new_position