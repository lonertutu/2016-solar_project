# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """
     функция считывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
     :param input_filename: имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """
     Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
     :param line: строка с описание звезды.
     :param star: объект звезды.
    """
    star.R = int(line.split()[1])
    star.color = line.split()[2]
    star.m = float(line.split()[3])
    star.x = float(line.split()[4])
    star.y = float(line.split()[5])
    star.Vx = float(line.split()[6])
    star.Vy = float(line.split()[7])


def parse_planet_parameters(line, planet):
    """
     Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
     :param line: строка с описание звезды.
     :param planet: объект звезды.
    """
    planet.R = int(line.split()[1])
    planet.color = line.split()[2]
    planet.m = float(line.split()[3])
    planet.x = float(line.split()[4])
    planet.y = float(line.split()[5])
    planet.Vx = float(line.split()[6])
    planet.Vy = float(line.split()[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """
    Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
     :param output_filename: имя входного файла
     :param space_objects: список объектов планет и звёзд
    """
    out_file = open(output_filename, 'w')
    for obj in space_objects:
        out_file.write(obj.type + ' ' + str(obj.R) + ' ' + obj.color + ' ' + str(obj.m) + ' ' + str(obj.x) +
                       ' ' + str(obj.y) + ' ' + str(obj.Vx) + ' ' + str(obj.Vy) + '\n')
    out_file.close()


def statistics(output_filename, space_objects, time):
    """
    при необходимости сохраняет параметры каждого объекта в файле следующей структуры:
    Star <radius in pixels> <color> <mass> <x> <y> <Vx> <Vy>,
    Planet <radius in pixels> <color> <mass> <x> <y> <Vx> <Vy>.
    :param output_filename: имя получаемого файла
    :param space_objects: список объектов, параметры которых мы записываем в файл
    :param time: расчетное время до момента, когда пользователь попросит сохранить параметры в файл
    """
    count = 0
    with open(output_filename, "w") as out_file:
        for obj in space_objects:
            if obj.type == "planet":
                print(f"{count} {time} {obj.type} {obj.x} {obj.y} {obj.vx} {obj.vy}", file=out_file)
                line = str(count) + " " + str(obj.get_distance_massive()) + " " + str(obj.get_v_massive()) + "\n"
                out_file.write(line)
            count += 1


if __name__ == "__main__":
    print("This module is not for direct call!")
