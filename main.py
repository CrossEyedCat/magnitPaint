from tkinter import *
import tkinter.filedialog as fd
from ElectricityCluster import *
from Electricity import *
from VectorField import *


class PaintApp:
    Cluster = ElectricityCluster()
    VecFil = VectorField()
    drawing_tool = "inside"
    left_button = "up"
    x_position, y_position = None, None

    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

    @staticmethod
    def quit_app():
        root.quit()

    def __init__(self, Root):
        self.drawing_area = Canvas(Root, width=500, height=500, bg="white")
        self.drawing_area.pack()

        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.left_button_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.left_button_up)

        the_menu = Menu(Root)
        file_menu = Menu(the_menu, tearoff=0)
        tool_menu = Menu(the_menu, tearoff=0)
        elect_menu = Menu(the_menu, tearoff=0)
        elect_menu.add_command(label="Inside", command=self.set_inside_drawing_tool)
        elect_menu.add_command(label="Outside", command=self.set_outside_drawing_tool)
        tool_menu.add_command(label="Remove", command=self.remove_drawing_tool)
        tool_menu.add_command(label="Move", command=self.move_drawing_tool)
        file_menu.add_command(label="Save", command=self.save)
        file_menu.add_command(label="load", command=self.load)
        file_menu.add_command(label="Quit", command=self.quit_app)
        the_menu.add_cascade(label="Options", menu=file_menu)
        the_menu.add_cascade(label="Tools", menu=tool_menu)
        the_menu.add_cascade(label="Electricity", menu=elect_menu)
        Root.config(menu=the_menu)

    def save(self):
        self.text = Text(self, height=10, width=50)
        self.btn_save = Button(self, text="Сохранить", command=self.save_file)

        self.text.pack()
        self.btn_save.pack(pady=10, ipadx=5)

    def save_file(self):
        new_file = fd.asksaveasfile(title="Сохранить файл", defaultextension=".txt",
                                    filetypes=(("Текстовый файл", "*.txt"),))
        if new_file:
            new_file.write(self.Cluster.get_JSON())
            new_file.close()

    def load(self):
        btn_file = self.tk.Button(self, text="Выбрать файл", command=self.choose_file)

    def set_inside_drawing_tool(self):
        self.drawing_tool = "inside"

    def set_outside_drawing_tool(self):
        self.drawing_tool = "outside"

    def remove_drawing_tool(self):
        self.drawing_tool = "remove"

    def move_drawing_tool(self):
        self.drawing_tool = "move"

    def left_button_down(self, event=None):
        self.left_button = "down"
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    def left_button_up(self, event=None):
        self.left_button = "up"
        self.x_position = None
        self.y_position = None

        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        if self.drawing_tool == "inside":
            self.inside_draw(event)
        if self.drawing_tool == "outside":
            self.outside_draw(event)
        if self.drawing_tool == "remove":
            self.remove_draw(event)
        if self.drawing_tool == "move":
            self.move_draw(event)

    def motion(self, event=None):
        self.x_position = event.x
        self.y_position = event.y

    def inside_draw(self, event=None):
        if None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
            diameter = 15
            center_x = min(self.x1_line_pt, self.x2_line_pt) + diameter
            center_y = min(self.y1_line_pt, self.y2_line_pt) + diameter
            new_elect = Electricity(x=center_x, y=center_y, clockwise=1)
            self.Cluster.add_electricity(new_elect)
            self.build_Vector_field(event)

    def outside_draw(self, event=None):
        if None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
            diameter = 15
            center_x = min(self.x1_line_pt, self.x2_line_pt) + diameter
            center_y = min(self.y1_line_pt, self.y2_line_pt) + diameter
            new_elect = Electricity(x=center_x, y=center_y, clockwise=0)
            self.Cluster.add_electricity(new_elect)
            self.build_Vector_field(event)

    def remove_draw(self, event=None):
        for elect in self.Cluster.get_cluster():
            if (elect.get_x() - self.x2_line_pt) ** 2 + (elect.get_y() - self.y2_line_pt) ** 2 <= 900:
                self.Cluster.get_cluster().remove(elect)
                self.build_Vector_field(event)

    def move_draw(self, event=None):
        for elect in self.Cluster.get_cluster():
            if (elect.get_x() - self.x1_line_pt) ** 2 + (elect.get_y() - self.y1_line_pt) ** 2 <= 900:
                elect.set_x(self.x2_line_pt)
                elect.set_y(self.y2_line_pt)
                self.build_Vector_field(event)

    def build_Vector_field(self, event):
        self.drawing_area.delete("all")
        for elect in self.Cluster.get_cluster():
            x = elect.get_x()
            y = elect.get_y()
            if elect.get_clockwise() == 0:
                event.widget.create_oval(x - 15, y - 15, x + 15,
                                         y + 15, fill="blue", outline="black", width=1)
                event.widget.create_oval(x - 7.5, y - 7.5,
                                         x + 7.5, y + 7.5,
                                         fill="black", width=1)
            else:
                event.widget.create_oval(x - 15, y - 15, x + 15,
                                         y + 15, fill="red", outline="black", width=1)
                event.widget.create_line(x, y - 7.5,
                                         x, y + 7.5,
                                         fill="black",
                                         width=4)
                event.widget.create_line(x - 7.5, y,
                                         x + 7.5, y,
                                         fill="black",
                                         width=4)

        for vector in self.VecFil.get_VectorField():
            x = vector.get_X()
            y = vector.get_Y()
            length = 0
            angle = 0
            len2 = 0
            flag = 1
            for elect in self.Cluster.get_cluster():
                temp_len = elect.get_vector_length(vector_x=x, vector_y=y)

                temp_angle = elect.get_vector_angle(vector_x=x, vector_y=y)

                if flag == 1:
                    length = temp_len
                    angle = temp_angle
                    len2 = length
                    flag = 0
                else:
                    num = math.pi - angle + temp_angle
                    cos = math.cos(num)
                    sin = math.sin(num)
                    len2 = temp_len * temp_len + length * length - 2 * temp_len * length * cos
                    len2 = math.sqrt(len2)
                    angle = math.asin(sin * temp_len / len2) + temp_angle

            vector.set_length(len2)
            vector.set_angle(angle)
            vector.draw(event)


root = Tk()
paint_app = PaintApp(root)
root.mainloop()
