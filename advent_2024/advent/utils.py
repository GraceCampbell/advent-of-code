def turn_90_degrees(direction=(0, 1)):
    if direction == (0, -1):
        return (1, 0)
    elif direction == (1, 0):
        return (0, 1)
    elif direction == (0, 1):
        return (-1, 0)
    else:
        return (0, -1)
