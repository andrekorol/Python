import health_methods


class Character(object):
    def __init__(self, health, is_alive=True):
        self.health = health
        self.max_health = self.health
        self.is_alive = is_alive

    def update_health(self,
                      health_action,
                      health_points,
                      increase_max_health=False):
        self.health, self.max_health, self.is_alive = health_methods.update_health(
            self.health, self.max_health, self.is_alive, health_action,
            health_points, increase_max_health)

    def set_health(self, new_health):
        self.health, self.max_health, self.is_alive = health_methods.set_health(
            self.health, self.max_health, new_health)
