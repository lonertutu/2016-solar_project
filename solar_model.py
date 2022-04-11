# Гравитационная постоянная Ньютона G
GRAVITATION_CONSTANT = 6.67408E-11


def calculate_force(body, space_objects):
    """
     функция вычисляет силу, действующую на тело.
     :param body: тело, для которого нужно вычислить дейстующую силу.
     :param space_objects: список объектов, которые воздействуют на тело.
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


def move_space_object(body, dt):
    """
     функция перемещает тело в соответствии с действующей на него силой.
     :param body: тело, которое нужно переместить.
     :param dt: время действия силы
    """
    if body.m == 0:
        ax = 0
        ay = 0
    else:
        ax = body.Fx / body.m
        ay = body.Fy / body.m

    body.Vx += ax * dt
    body.x += body.Vx * dt

    body.Vy += ay * dt
    body.y += body.Vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    """
     функция пересчитывает координаты объектов.
     :space_objects: список оьъектов, для которых нужно пересчитать координаты.
     :dt: шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")