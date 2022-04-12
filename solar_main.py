import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename

import solar_input as inputing
import solar_model as model
import solar_vis as vis

perform_execution = False
physical_time = 0
displayed_time = None
time_step = None
space_objects = []


def execution():
    """
    It is executed cyclically, causing the processing of all celestial bodies, updating their position on the screen.
    """
    global physical_time
    global displayed_time
    model.recalculate_space_objects_positions(space_objects, time_step.get())
    for body in space_objects:
        vis.update_object_position(space, body)
    physical_time += time_step.get()
    displayed_time.set("%.1f" % physical_time + " seconds gone")

    if perform_execution:
        space.after(101 - int(time_speed.get()), execution)


def start_execution():
    """Click event handler for the Start button.
    Starts the cyclic execution of the execution function.
    """
    global perform_execution
    perform_execution = True
    start_button['text'] = "Pause"
    start_button['command'] = stop_execution

    execution()
    print('Started execution...')


def stop_execution():
    """Click event handler for the Start button.
    Finishes the cyclic execution of the execution function.
    """
    global perform_execution
    perform_execution = False
    start_button['text'] = "Start"
    start_button['command'] = start_execution
    print('Paused execution.')


def open_file_dialog():
    """
    Open dialog window, help to choose file, read the parameters
    """
    global space_objects
    global perform_execution
    perform_execution = False
    for obj in space_objects:
        space.delete(obj.image)  # удаление старых изображений планет
    in_filename = askopenfilename(filetypes=(("Text file", ".txt"),))
    space_objects = inputing.read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])
    vis.calculate_scale_factor(max_distance)

    for obj in space_objects:
        if obj.type == 'star':
            vis.create_star_image(space, obj)
        elif obj.type == 'planet':
            vis.create_planet_image(space, obj)
        else:
            raise AssertionError()


def save_file_dialog():
    """
    Open dialog window, help to choose file, save the parameters
    """
    out_filename = asksaveasfilename(filetypes=(("Text file", ".txt"),))
    inputing.write_space_objects_data_to_file(out_filename, space_objects)


def main():
    """
    Create graphic objects from tkinter: window, canvas, buttons
    """
    global physical_time, displayed_time, time_step, time_speed, space, start_button

    physical_time = 0

    root = tkinter.Tk()
    space = tkinter.Canvas(root, width=vis.window_width, height=vis.window_height, bg="black")
    space.pack(side=tkinter.TOP)
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.BOTTOM)

    start_button = tkinter.Button(frame, text="Start", command=start_execution, width=6)
    start_button.pack(side=tkinter.LEFT)

    time_step = tkinter.DoubleVar()
    time_step.set(1)
    time_step_entry = tkinter.Entry(frame, textvariable=time_step)
    time_step_entry.pack(side=tkinter.LEFT)

    time_speed = tkinter.DoubleVar()
    scale = tkinter.Scale(frame, variable=time_speed, orient=tkinter.HORIZONTAL)
    scale.pack(side=tkinter.LEFT)

    load_file_button = tkinter.Button(frame, text="Open file...", command=open_file_dialog)
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(frame, text="Save to file...", command=save_file_dialog)
    save_file_button.pack(side=tkinter.LEFT)

    displayed_time = tkinter.StringVar()
    displayed_time.set(str(physical_time) + " seconds gone")
    time_label = tkinter.Label(frame, textvariable=displayed_time, width=30)
    time_label.pack(side=tkinter.RIGHT)

    root.mainloop()


if __name__ == "__main__":
    main()
