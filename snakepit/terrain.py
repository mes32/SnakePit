import map_entity

class Terrain(map_entity.MapEntity):
    """
    Type of terrain located at a particular tile of PlayingField
    """

    # walkable

    def __init__(self, position_lookup, position, walkable=False):

        # For now any/all terrain objects are non-traversable walls
        super(Terrain, self).__init__(position_lookup, position)
        self.walkable = walkable

    def is_walkable(self):
        return self.walkable
