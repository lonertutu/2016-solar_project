import tkinter
from tkinter import NW
from tkinter.filedialog import askopenfilename, asksaveasfilename

import solar_input as inputing
import solar_model as model
import solar_vis as vis



class Important_values:

    def __init__(self):
        self.perform_execution = False
        self.physical_time = 0
        self.time_step = None
        self.space_objects = []
        self.physical_time = 0
        self.displayed_time = None
        self.load_file_button = 0
        self.save_file_button = 0
        self.time_speed = 0

        self.space = 0

def execution(scale_factor, important_values_class):
    """
    It is executed cyclically, causing the processing of all celestial bodies, updating their position on the screen.
    """
    important_values_class.space_objects = model.recalculate_space_objects_positions(important_values_class.space_objects, important_values_class.time_step.get())
    for body in important_values_class.space_objects:
        vis.update_object_position(important_values_class.space, body, scale_factor)
    important_values_class.physical_time += important_values_class.time_step.get()
    important_values_class.displayed_time.set("%.1f" % important_values_class.physical_time + " seconds gone")

    if important_values_class.perform_execution:
        important_values_class.space.after(101 - int(important_values_class.time_speed.get()), lambda: execution(scale_factor, important_values_class))

#
def start_execution(scale_factor, important_values_class):
    """Click event handler for the Start button.
    Starts the cyclic execution of the execution function.
    """

    important_values_class.perform_execution = True
    important_values_class.start_button['text'] = "Pause"
    important_values_class.start_button['command'] = lambda: stop_execution(important_values_class, scale_factor)

    execution(scale_factor, important_values_class)
    print('Started execution...')


def stop_execution(important_values_class, scale_factor):
    """Click event handler for the Start button.
    Finishes the cyclic execution of the execution function.
    """
    important_values_class.perform_execution = False
    important_values_class.start_button['text'] = "Start"
    important_values_class.start_button['command'] = lambda: start_execution(scale_factor, important_values_class)
    print('Paused execution.')


def open_file_dialog(scale_factor, important_values_class):
    """
    Open dialog window, help to choose file, read the parameters
    """
    important_values_class.perform_execution = False
    for obj in important_values_class.space_objects:
        important_values_class.space.delete(obj.image)
    in_filename = askopenfilename(filetypes=(("Text file", ".txt"),))
    important_values_class.space_objects = inputing.read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in important_values_class.space_objects])
    vis.calculate_scale_factor(max_distance, scale_factor)

    for obj in important_values_class.space_objects:
        if obj.type == 'star':
            vis.create_star_image(important_values_class.space, obj, scale_factor)
        elif obj.type == 'planet':
            vis.create_planet_image(important_values_class.space, obj, scale_factor)
        else:
            raise AssertionError()


def save_file_dialog(important_values_class):
    """
    Open dialog window, help to choose file, save the parameters
    """
    out_filename = asksaveasfilename(filetypes=(("Text file", ".txt"),))
    inputing.write_space_objects_data_to_file(out_filename, important_values_class.space_objects)


def main(scale_factor, important_values_class):
    """
    Create graphic objects from tkinter: window, canvas, buttons
    """

    physical_time = 0

    root = tkinter.Tk()
    important_values_class.space = tkinter.Canvas(root, width=vis.WINDOW_WIDTH, height=vis.WINDOW_HEIGHT, bg="black")
    important_values_class.space.pack(side=tkinter.TOP)

    picture = tkinter.PhotoImage(file='cosmo.png')
    important_values_class.space.create_image(20, 20, anchor=NW, image=picture)

    frame = tkinter.Frame(root, bg='#565f9c')
    frame.pack(side=tkinter.BOTTOM)

    important_values_class.start_button = tkinter.Button(frame, text="Start", command= lambda: start_execution(scale_factor, important_values_class), width=6, bg='#565f9c')
    important_values_class.start_button.pack(side=tkinter.LEFT)

    important_values_class.time_step = tkinter.DoubleVar()
    important_values_class.time_step.set(1)
    time_step_entry = tkinter.Entry(frame, textvariable=important_values_class.time_step, bg='#3a3d78')
    time_step_entry.pack(side=tkinter.LEFT)

    important_values_class.time_speed = tkinter.DoubleVar()
    scale = tkinter.Scale(frame, variable=important_values_class.time_speed, orient=tkinter.HORIZONTAL, highlightcolor='#565f9c',
                          highlightbackground='#565f9c', bg='#3a3d78', activebackground='#565f9c',
                          troughcolor='#565f9c')
    scale.pack(side=tkinter.LEFT)

    load_file_button = tkinter.Button(frame, text="Open file...", command= lambda: open_file_dialog(scale_factor, important_values_class), bg='#565f9c')
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(frame, text="Save to file...", command= lambda: save_file_dialog(important_values_class), bg='#565f9c')
    save_file_button.pack(side=tkinter.LEFT)

    important_values_class.displayed_time = tkinter.StringVar()
    important_values_class.displayed_time.set(str(physical_time) + " seconds gone")
    time_label = tkinter.Label(frame, textvariable=important_values_class.displayed_time, width=30, bg='#3a3d78')
    time_label.pack(side=tkinter.RIGHT)

    root.mainloop()


if __name__ == "__main__":
    scale_factor = vis.Scale_factor_in_class()
    imp = Important_values()
    main(scale_factor, imp)
