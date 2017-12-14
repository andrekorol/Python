class Health(object):
 
    def update_health(self,
                      health_action,
                      health_points,
                      increase_max_health=False):
        if health_action == "add" and (
                increase_max_health
                or self.health + health_points <= self.max_health):
            self.health += health_points
            if increase_max_health and self.health > self.max_health:
                self.max_health = self.health
        elif (health_action == "add"
              and self.health + health_points > self.max_health):
            self.health = self.max_health

        elif health_action == "sub":
            self.health -= health_points

        if self.health <= 0:
            self.is_alive = False
            self.health = 0

    def set_health(self, new_health):
        if new_health > self.max_health:
            self.max_health = new_health

        self.health = new_health
