'''Function definitions and invocation.'''


def update_health(health, max_health, is_alive, health_action, health_points,
                  increase_max_health):
    if health_action == "add" and (increase_max_health
                                   or health + health_points <= max_health):
        health += health_points
        if increase_max_health and health > max_health:
            max_health = health
    elif (health_action == "add" and health + health_points > max_health):
        health = max_health

    elif health_action == "sub":
        health -= health_points

        if health <= 0:
            is_alive = False
            health = 0

    return health, max_health, is_alive


def set_health(health, max_health, new_health):
    if new_health > max_health:
        max_health = new_health
        health = new_health

    elif new_health < 0:
        health = 0

    else:
        health = new_health

    if health > 0:
        is_alive = True

    else:
        is_alive = False

    return health, max_health, is_alive
