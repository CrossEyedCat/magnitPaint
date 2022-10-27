
from tkinter import *

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
    def quit_app(event=None):
        root.quit()

    def __init__(self, root):
        drawing_area = Canvas(root, width=500, height=500, bg="white")
        drawing_area.pack()

        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_button_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_button_up)

        the_menu = Menu(root)

        file_menu = Menu(the_menu, tearoff=0)
        file_menu.add_command(label="Inside", command=self.set_inside_drawing_tool)
        file_menu.add_command(label="Outside", command=self.set_outside_drawing_tool)

        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit_app)

        the_menu.add_cascade(label="Options", menu=file_menu)
        root.config(menu=the_menu)

    def set_inside_drawing_tool(self):
        self.drawing_tool = "inside"

    def set_outside_drawing_tool(self):
        self.drawing_tool = "outside"

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

    def motion(self, event=None):
        self.x_position = event.x
        self.y_position = event.y

    def inside_draw(self, event=None):
        if None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
            diameter = 25
            centerX = min(self.x1_line_pt, self.x2_line_pt)+diameter/2
            centerY = min(self.y1_line_pt, self.y2_line_pt)+diameter/2
            NewElec = Electricity(x=centerX, y=centerY, clockwise=1)
            self.Cluster.add_electricity(NewElec)
            self.build_Vector_field(event)

    def outside_draw(self, event=None):
        if None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
            diameter = 30
            centerX = min(self.x1_line_pt, self.x2_line_pt) + diameter / 2
            centerY = min(self.y1_line_pt, self.y2_line_pt) + diameter / 2
            NewElec = Electricity(x=centerX, y=centerY, clockwise=0)
            self.Cluster.add_electricity(NewElec)
            self.build_Vector_field(event)

    def build_Vector_field(self, event):
        for vector in self.VecFil.get_VectorField():
            vector.erase(event=event)
            for elec in self.Cluster.get_cluster():
                if (elec.get_clockwise() == 0):
                    event.widget.create_oval(elec.get_x() - 15, elec.get_y() - 15, elec.get_x() + 15,
                                             elec.get_y() + 15, fill="blue", outline="black", width=1)
                    event.widget.create_oval(elec.get_x() - 15 + 30 / 4, elec.get_y() - 15 + 30 / 4,
                                             elec.get_x() - 15 + 30 * 3 / 4, elec.get_y() - 15 + 30 * 3 / 4,
                                             fill="black", width=1)
                else:
                    event.widget.create_oval(elec.get_x() - 15, elec.get_y() - 15, elec.get_x() + 15,
                                             elec.get_y() + 15, fill="red", outline="black", width=1)
                    event.widget.create_line(elec.get_x() - 15 + 30 / 2, elec.get_y() - 15 + 30 / 4,
                                             elec.get_x() - 15 + 30 / 2, elec.get_y() - 15 + 30 * 3 / 4,
                                             fill="black",
                                             width=4)
                    event.widget.create_line(elec.get_x() - 15 + 30 / 4, elec.get_y() - 15 + 30 / 2,
                                             elec.get_x() - 15 + 30 * 3 / 4, elec.get_y() - 15 + 30 / 2,
                                             fill="black",
                                             width=4)
        for vector in self.VecFil.get_VectorField():
            len = 0
            angle = 0
            for elec in self.Cluster.get_cluster():
                if angle==0:
                    len = elec.get_vector_length(vector_x=vector.get_X(), vector_y=vector.get_Y())
                    angle = elec.get_vector_angle(vector_x=vector.get_X(), vector_y=vector.get_Y())
                    len2 = len
                else :
                    len1 = elec.get_vector_length(vector_x=vector.get_X(), vector_y=vector.get_Y())
                    angle1 = elec.get_vector_angle(vector_x=vector.get_X(), vector_y=vector.get_Y())
                    len2 = math.sqrt(len1*len1+len*len-2*len1*len*math.cos(math.pi-angle+angle1))
                    if((2*len*len2)==0):
                        angle = 0
                        len2 = 0
                    else:
                        angle= math.asin(math.sin(math.pi-angle+angle1)*len1/len2)+angle1

            vector.set_length(len2)
            vector.set_angle(angle)
            vector.draw(event)




root = Tk()
paint_app = PaintApp(root)
root.mainloop()
