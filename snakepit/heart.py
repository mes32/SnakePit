from mappable_entity import MappableEntity
from position import Position

class Heart(MappableEntity):
    """
    A basic powerup that increases current HP by 1 point
    """

    def __init__(self, position_lookup, position):
        super(Heart, self).__init__(position_lookup, position)
        self.is_consumed = False

    def consume(self):
        self.is_consumed = True
