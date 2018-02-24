import position
import position_lookup

class MappableEntity():
    """
    Game objects that can be placed on the map.
    """

    def __init__(self, position_lookup, position):
        self.position_lookup = position_lookup
        self.set_position(position)

    def set_position(self, position):
        self.position = position
        self.position_lookup.insert(position, self)