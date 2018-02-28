from mappable_entity import MappableEntity
from position import Position

class Snake(MappableEntity):
    """
    The basic snake enemies.
    """

    def __init__(self, position_lookup, position):
        super(Snake, self).__init__(position_lookup, position)
        self.current_hp = 1
        self.total_hp = 1

    def take_damage(self, damage):
        self.current_hp = self.current_hp - damage
        if self.current_hp < 0:
            self.current_hp = 0

    def is_dead(self):
        if self.current_hp <= 0:
            return True
        else:
            return False
