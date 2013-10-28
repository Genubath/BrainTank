TANK_IDLE     = 1
TANK_TURNING  = 2
TANK_SHOOTING = 3
TANK_MOVING   = 4
TANK_DEAD     = 5

FACING_UP     = 6
FACING_RIGHT  = 7
FACING_DOWN   = 8
FACING_LEFT   = 9


def facing_to_string(facing):
    if facing == FACING_UP:
        return "up"
    elif facing == FACING_DOWN:
        return "down"
    elif facing == FACING_LEFT:
        return "left"
    else:
        return "right"
