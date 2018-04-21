
class MapEntity():
    """
    Game objects that can be placed on the map.
    """

    def __init__(self, position_map, position):
        self.position_map = position_map
        self.position = position
        self.position_map.insert(position, self)

    def move_position(self, new_position):
        self.position_map.move(self.position, new_position)
        self.position = new_position

    def delete(self):
        self.position_map.delete(self.position)