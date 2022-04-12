"""Visualization module."""

header_font = "Arial-16"
window_width = 600
window_height = 600

scale_factor = None
"""Scaling of screen coordinates in relation to physical ones.
Type: float
Measure: number of pixels per meter."""


def calculate_scale_factor(max_distance):
    """
    Count scale_factor using height,width.
    """
    global scale_factor
    scale_factor = 0.4 * min(window_height, window_width) / max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    """
    Returns the screen **x** coordinate given the **x** coordinate of the model.

    return: int value
    """
    return int(x * scale_factor) + window_width // 2


def scale_y(y):
    """
    Returns the screen **y** coordinate given the **y** coordinate of the model.

    return: int value
    """
    return int(y * scale_factor) + window_height // 2


def create_star_image(space, star):
    """Create the star object.

    param: x,y - coordinates after scaling
    param: r - radius of the star
    """
    x = scale_x(star.x)
    y = scale_y(star.y)
    r = star.R
    star.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=star.color)


def create_planet_image(space, planet):
    """Create the planet object.

    param: x,y - coordinates after scaling
    param: r - radius of the planet
    """
    x = scale_x(planet.x)
    y = scale_y(planet.y)
    r = planet.R
    planet.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=planet.color)


def update_system_name(space, system_name):
    """Create text with name of objects

    param: space — canvas
    param: system_name
    """
    space.create_text(30, 80, tag="header", text=system_name, font=header_font)


def update_object_position(space, body):
    """Moves objects

    param: space — canvas
    param: body - the object need to replace
    """
    x = scale_x(body.x)
    y = scale_y(body.y)
    r = body.R
    if x + r < 0 or x - r > window_width or y + r < 0 or y - r > window_height:
        space.coords(body.image, window_width + r, window_height + r,
                     window_width + 2 * r, window_height + 2 * r)  # положить за пределы окна
    space.coords(body.image, x - r, y - r, x + r, y + r)


if __name__ == "__main__":
    print("This module is not for direct call!")
