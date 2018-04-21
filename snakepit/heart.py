import map_entity

class Heart(map_entity.MapEntity):
    """
    A basic powerup that increases current HP by 1 point
    """

    def __init__(self, lookup, position):
        super(Heart, self).__init__(lookup, position)
        # self.lookup = lookup
        self.is_consumed = False

    def consume(self):
        self.is_consumed = True
        # self.lookup.remove(self)