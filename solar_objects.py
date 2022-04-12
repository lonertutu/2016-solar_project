class Star:
    """Describes the star.
    Contains the mass, coordinates, speed of the star,
    as well as the visual radius of the star in pixels and its color.
    """

    type = "star"
    mass = 0
    x = 0
    y = 0
    Vx = 0
    Vy = 0
    Fx = 0
    Fy = 0
    R = 5
    color = "red"
    image = None


class Planet(Star):
    """Describes the planet."""
    type = "planet"
