"""Visualization module."""

header_font = "Arial-16"
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600


class Scale_factor_in_class:
    value = None


"""Scaling of screen coordinates in relation to physical ones.
Type: float
Measure: number of pixels per meter."""


def calculate_scale_factor(max_distance, scale_factor):
    """
    Count scale_factor using height,width
    """
    scale_factor.value = 0.4 * min(WINDOW_HEIGHT, WINDOW_WIDTH) / max_distance
    print('Scale factor:', scale_factor)


def scale_x(x, scale_factor):
    """
    Returns the screen **x** coordinate given the **x** coordinate of the model.

    return: int value
    """
    return int(x * scale_factor.value) + WINDOW_WIDTH // 2


def scale_y(y, scale_factor):
    """
    Returns the screen **y** coordinate given the **y** coordinate of the model.

    return: int value
    """
    return int(y * scale_factor.value) + WINDOW_HEIGHT // 2


def create_star_image(space, star, scale_factor):
    """Create the star object.

    :param: x,y - coordinates after scaling
    :param: r - radius of the star
    """
    x = scale_x(star.x, scale_factor)
    y = scale_y(star.y, scale_factor)
    r = star.R
    star.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=star.color)


def create_planet_image(space, planet, scale_factor):
    """Create the planet object.

    :param: x,y - coordinates after scaling
    :param: r - radius of the planet
    """
    x = scale_x(planet.x, scale_factor)
    y = scale_y(planet.y, scale_factor)
    r = planet.R
    planet.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=planet.color)


def update_system_name(space, system_name):
    """Create text with name of objects

    :param: space — canvas
    :param: system_name
    """
    space.create_text(30, 80, tag="header", text=system_name, font=header_font)


def update_object_position(space, body, scale_factor):
    """Moves objects

    :param: space — canvas
    :param: body - the object need to replace
    """
    x = scale_x(body.x, scale_factor)
    y = scale_y(body.y, scale_factor)
    r = body.R
    if x + r < 0 or x - r > WINDOW_WIDTH or y + r < 0 or y - r > WINDOW_HEIGHT:
        space.coords(body.image, WINDOW_WIDTH + r, WINDOW_HEIGHT + r,
                     WINDOW_WIDTH + 2 * r, WINDOW_HEIGHT + 2 * r)  # положить за пределы окна
    space.coords(body.image, x - r, y - r, x + r, y + r)


if __name__ == "__main__":
    print("This module is not for direct call!")
