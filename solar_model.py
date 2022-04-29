GRAVITATION_CONSTANT = 6.67408E-11


def calculate_force(body, space_objects):
    """
     Calculate acting force
     :param body: the body to be moved by force
     :param space_objects: list of objects
     """

    body.Fx = 0
    body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        rx = (obj.x - body.x)
        ry = (obj.y - body.y)
        r = (rx ** 2 + ry ** 2) ** 0.5
        body.Fx += (GRAVITATION_CONSTANT * (body.m * obj.m) / r ** 3 * rx)
        body.Fy += (GRAVITATION_CONSTANT * (body.m * obj.m) / r ** 3 * ry)


#
def move_space_object(body, dt):
    """
     Function moves the body in accordance with the force acting on it.
     :param body: the body to be moved
     :param dt: duration of the force
    """
    try:
        if dt > 900000:
            raise ValueError(
                "Too big dt, dt = " + str(dt) + ", please, reudce value to 900000 with left down corner")
        if body.m == 0:
            ax = 0
            ay = 0
        else:
            ax = body.Fx / body.m
            ay = body.Fy / body.m

        if body.type != "star":
            body.Vx += ax * dt
            body.x += body.Vx * dt

            body.Vy += ay * dt
            body.y += body.Vy * dt
    except ValueError as e:
        print(e)
        exit()


def recalculate_space_objects_positions(space_objects, dt):
    """
    Recalculate the coordinates
     :space_objects: a list of objects for which you need to recalculate the coordinates
     :dt: time step
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)
    return space_objects


if __name__ == "__main__":
    print("This module is not for direct call!")
