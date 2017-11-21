import tkinter as tk
import tkinter.messagebox as msg
import tkinter.colorchooser as clr
import math


class GetPointsDialog():
    DEFAULT_COLOR = 'black'

    def __init__(self, master, Wid_type):
        """
        THIS METHOD SHOULD CONSTRUCT THE TOPLEVEL WINDOW AND
        INITIATLIZE THE MAIN LOGIC FOR TAKING INPUT FROM USER FOR
        THE CORDINATES OF CIRCLE, RETANGLE AND LINE
        """
        self.color = self.DEFAULT_COLOR  # Setting the default COLOR to black
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.rad = 0
        self.dash = 0
        self.ok = False

        self.Wid_type = Wid_type
        self.win = tk.Toplevel(master=master)
        tk.Label(self.win, text="X1").grid(row=0)
        self.ex1 = tk.Entry(self.win)
        self.ex1.grid(row=0, column=1)
        tk.Label(self.win, text="Y1").grid(row=0, column=2)
        self.ey1 = tk.Entry(self.win)
        self.ey1.grid(row=0, column=3)
        if Wid_type == 0:
            tk.Label(self.win, text="Enter Radius").grid(row=1)
            self.er = tk.Entry(self.win)
            self.er.grid(row=1, column=1)
        else:
            tk.Label(self.win, text="X2").grid(row=1)
            self.ex2 = tk.Entry(self.win)
            self.ex2.grid(row=1, column=1)
            tk.Label(self.win, text="Y2").grid(row=1, column=2)
            self.ey2 = tk.Entry(self.win)
            self.ey2.grid(row=1, column=3)
        self.dash = tk.IntVar(0)
        tk.Radiobutton(self.win, text="Dashed", variable=self.dash,
                       value=1).grid(row=2)
        tk.Radiobutton(self.win, text="Un Dashed", variable=self.dash,
                       value=0).grid(row=2, column=1)
        tk.Button(self.win, text="Color",
                  command=self.choose_color).grid(row=2, column=2)
        tk.Button(self.win, text='Submit',
                  command=self.submit).grid(row=3, columnspan=2)
        tk.Button(self.win, text='Reset',
                  command=self.reset).grid(row=3, column=2, columnspan=2)
        self.win.geometry("+%d+%d" % (master.winfo_rootx() + 50,
                          master.winfo_rooty() + 50))
        self.win.protocol("WM_DELETE_WINDOW", self.win.quit)
        self.win.mainloop()
        self.win.destroy()

    def choose_color(self):
        self.get_color = clr.askcolor(parent=self.win)
        self.color = self.get_color[1]

    def submit(self):

        """
        IT SHOULD GET THE INPUT FROM USER
        AND SHOULD CHECK ALL THE CONDITIONS GIVEN FROM USER AND VALIDATE,
        ONCE VALUES ARE GOOD SEND VALUES TO MAIN CLASS ELSE RESET THE VALUES.
        """
        try:
            self.x1 = int(self.ex1.get())
        except ValueError:
            msg.showinfo("Value Error",
                         "Coefficient of X1 can't be a character or a Null",
                         parent=self.win)
            self.reset()
            return
        try:
            self.y1 = int(self.ey1.get())
        except ValueError:
            msg.showinfo("Value Error",
                         "Coefficient of Y1 can't be a character or a Null",
                         parent=self.win)
            self.reset()
            return
        if self.Wid_type == 0:
            try:
                self.rad = int(self.er.get())
            except ValueError:
                msg.showinfo("Value Error",
                             "Radius can't be a character or a Null",
                             parent=self.win)
                self.reset()
                return
            if self.x1 < 50:
                msg.showinfo("Value Error",
                             "Coefficients of X1 or X2 can't be less than"
                             "50 or X1 < X2 or Y1 < Y2",
                             parent=self.win)
                self.reset()
                return
        else:
            try:
                self.x2 = int(self.ex2.get())
            except ValueError:
                msg.showinfo("Value Error", "Coefficient of X2 can't be a"
                             "character or a Null", parent=self.win)
                self.reset()
                return
            try:
                self.y2 = int(self.ey2.get())
            except ValueError:
                msg.showinfo("Value Error",
                             "Coefficient of Y2 can't be a"
                             "character or a Null", parent=self.win)
                self.reset()
                return
            if self.x1 < 50 or (self.x1 > self.x2) or (self.y1 > self.y2):
                msg.showinfo("Value Error",
                             "Coefficients of X1 or X2 can't be"
                             "less than 50 or X1 < X2 or Y1 < Y2",
                             parent=self.win)
                self.reset()
                return
        self.ok = True
        self.win.quit()

    def reset(self):
        """
        SHOULD RESET THE VALUES IN THE
        ENTRY BOXES IF THERE ARE ANY ALPHANUMERIC ERRORS
        """
        self.ex1.delete(0, tk.END)
        self.ey1.delete(0, tk.END)
        if self.Wid_type == 0:
            self.er.delete(0, tk.END)
        else:
            self.ex2.delete(0, tk.END)
            self.ey2.delete(0, tk.END)


class Painter():
    def __init__(self):
        """
        SHOULD INITIALISE ALL THE ROOT ATTRIBUTES FOR BASE WINDOW.

        CAN ADD ANY NUMBER OF ATTRIBUTES REQUIRED FOR THE PROGRAM
        """
        self.root = tk.Tk()
        self.root.title("Python Paint")
        self.root.geometry("800x800")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.paint_Menu = tk.Menu(self.root)

        self.X = 0
        self.Y = 0
        self.radius = 0
        self.X1_COORD = 0
        self.Y1_COORD = 0
        self.X2_COORD = 0
        self.Y2_COORD = 0
        self.COLOR = 'black'
        self.DASH = 0

        self.cords = list()
        self.corde = list()
        self.ocords = list()
        self.ocorde = list()
        self.x = list()
        self.y = list()

        self.init_widgets()

    def init_widgets(self):

        """
        SHOULD DO THE BELOW LISTED OPERATIONS.
        """
        # Adding Menu Bar TO BASE WINDOW

        # CREATE ALL MENUBAR'S

        # CREATE ALL SUB MENUS FOR MAIN MENU AND ACTIVATING DYNAMICALLY.

        # ADD BUTTONS TO THE MAIN WINDOW AND ACTIVATE THEM DYNAMICALLY

        ###########################################

        self.filemenu = tk.Menu(self.paint_Menu)
        self.paint_Menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New", command=self.create_New_Canvas)
        self.filemenu.add_command(label="Save",
                                  command=self.save_canvas, state=tk.DISABLED)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exit)

        optionsmenu = tk.Menu(self.paint_Menu, tearoff=0)
        self.paint_Menu.add_cascade(label="Options", menu=optionsmenu,
                                    state=tk.DISABLED)
        optionsmenu.add_command(label="Circle",
                                command=lambda: self.Get_Cordinate_Points(0))
        optionsmenu.add_command(label="Line",
                                command=lambda: self.Get_Cordinate_Points(1))
        optionsmenu.add_command(label="Rectangle",
                                command=lambda: self.Get_Cordinate_Points(2))
        optionsmenu.add_separator()
        optionsmenu.add_command(label="Clear All", command=self.clear_canvas)
        self.enabled = False

        helpmenu = tk.Menu(self.paint_Menu, tearoff=0)
        self.paint_Menu.add_command(label="Help", command=self.show_help_about)

        self.toolbar = tk.Frame(self.root)

        self.PenButton = tk.Button(self.toolbar, text='PEN',
                                   command=lambda: self.activate_button("PEN"),
                                   state=tk.DISABLED)
        self.PenButton.pack(side=tk.LEFT, padx=2, pady=2)
        self.LineButton = tk.Button(self.toolbar, text='LINE',
                                    command=lambda:
                                    self.activate_button("LINE"),
                                    state=tk.DISABLED)
        self.LineButton.pack(side=tk.LEFT, padx=2, pady=2)
        self.CircleButton = tk.Button(self.toolbar, text='CIRCLE',
                                      command=lambda:
                                      self.activate_button("CIRCLE"),
                                      state=tk.DISABLED)
        self.CircleButton.pack(side=tk.LEFT, padx=2, pady=2)
        self.toolbar.pack(side=tk.LEFT, anchor="nw")
        self.root.config(menu=self.paint_Menu)

        self.root.mainloop()

        ##

    def create_New_Canvas(self):

        """
        CREATE A NEW CANVAS OF SIZE 600x600 TO THE MAIN FRAME
        """
        self.frm1 = tk.Frame(self.root)
        self.frm1.pack(side=tk.TOP, anchor=tk.S)
        self.cnvs = tk.Canvas(self.frm1, width=600, height=600, bg='white')
        self.cnvs.pack()
        self.enable_menu()

    def activate_button(self, Btn_Typ):
        """
        HANDLE THE BUTTONS ADDED ON THE FRAME FOR FREE PAINT BUTTONS
        """
        self.old_x = None
        self.old_y = None
        self.base_x = None
        self.base_y = None
        self.Btn_Typ = Btn_Typ
        self.old_widget = None
        if Btn_Typ == "LINE":
            self.cnvs.bind('<B1-Motion>', self.line_click)
            self.cnvs.bind('<ButtonRelease-1>', self.button_released)
        elif Btn_Typ == "PEN":
            self.cnvs.bind('<B1-Motion>', self.Brush)
            self.cnvs.bind('<ButtonRelease-1>', self.button_released)
        else:
            self.cnvs.bind('<B1-Motion>', self.Circle_Click)
            self.cnvs.bind('<ButtonRelease-1>', self.button_released)

    def button_released(self, event):
        """
        WHEN THE MOUSE BUTTON IS RELEASED SHOULD RESET THE
        CO-ORDINATES OF THE PREVIOUS BINDED VALUES.
        """
        if self.Btn_Typ == "LINE":
            if self.base_x:
                self.cords.append([self.base_x, self.base_y])
                self.corde.append([event.x, event.y])
        elif self.Btn_Typ == "CIRCLE":
            if self.base_x:
                self.ocords.append([self.base_x, self.base_y])
                self.ocorde.append([event.x, event.y])
        else:
            pass
        self.old_x = None
        self.old_y = None
        self.base_x = None
        self.base_y = None

    def Brush(self, event):
        """
        CAN USE THE BELOW GIVEN CODE FOR BRUSH
        OR CAN MODIFY ACCORDING TO YOUR INITIASED ATTRIBUTES.
        """
        if self.old_x and self.old_y:
            self.cnvs.create_line(self.old_x, self.old_y, event.x, event.y,
                                  width=2,
                                  fill='black', splinesteps=50)
        self.old_x = event.x
        self.old_y = event.y

    def redraw(self):
        """
        SHOULD ABLE TO SAVE ALL THE PREVIOUS CO-ORDINATE VALUES
        FOR OVAL(CIRCLE), LINE
        """
        for i in range(0, len(self.cords)):
            s = self.cords[i]
            e = self.corde[i]
            self.cnvs.create_line(s[0], s[1], e[0], e[1], width=2,
                                  fill='black')
        for i in range(0, len(self.ocords)):
            x1 = self.ocords[i][0]
            y1 = self.ocords[i][1]
            x2 = self.ocorde[i][0]
            y2 = self.ocorde[i][1]
            r = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            self.cnvs.create_oval(x1 - r, y1 - r, x1 + r, y1 + r,
                                  width=2, outline='black')

    def line_click(self, event):
        """
        SHOULD ABLE TO HANDLE THE MOUSE CLICK
        EVENT AND PASS CO-ORDINATES TO THE
        CREATE_LINE EVENT FOR THE CANVASE AND
        PASS THE FILL COLOR AND SET WIDTH PROPERTIES
        AND SHOULD ABLE TO CLEAR THE PREVIOUS VALUES
        """
        if self.base_x and self.base_y:
            if self.old_widget:
                self.cnvs.delete(self.old_widget)
            self.redraw()
            self.old_widget = self.cnvs.create_line(self.base_x, self.base_y,
                                                    event.x, event.y, width=2,
                                                    fill='black')
        else:
            self.base_x = event.x
            self.base_y = event.y
        self.old_x = event.x
        self.old_y = event.y

    def Circle_Click(self, event):
        """
        SAME AS THE LINE-CLICK METHOD BUT SHOULD CREATE A OVAL HERE
        """
        if self.base_x and self.base_y:
            if self.old_widget:
                self.cnvs.delete(self.old_widget)
            x1 = self.base_x
            y1 = self.base_y
            self.redraw()
            x2 = event.x
            y2 = event.y
            r = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            self.old_widget = self.cnvs.create_oval(self.base_x - r,
                                                    self.base_y - r,
                                                    self.base_x + r,
                                                    self.base_y + r,
                                                    width=2,
                                                    outline='black')
        else:
            self.base_x = event.x
            self.base_y = event.y
        self.old_x = event.x
        self.old_y = event.y

    def enable_menu(self):

        """
        THIS METHOD SHOULD BE ABLE TO HANDLE THE
        MENUBAR STATUS AND CONFIGURE TO NORMAL
        STATUS WHEN NEW BUTTON IS SELECTED
        """
        if self.enabled:
            self.enabled = False
            self.paint_Menu.entryconfigure(2, state=tk.DISABLED)
            self.filemenu.entryconfigure("Save", state=tk.DISABLED)
            self.filemenu.entryconfigure("New", state="normal")
            self.PenButton['state'] = tk.DISABLED
            self.LineButton['state'] = tk.DISABLED
            self.CircleButton['state'] = tk.DISABLED
        else:
            self.enabled = True
            self.paint_Menu.entryconfigure(2, state="normal")
            self.filemenu.entryconfigure("Save", state="normal")
            # self.filemenu.entryconfigure("New", state=tk.DISABLED)
            self.PenButton['state'] = 'normal'
            self.LineButton['state'] = 'normal'
            self.CircleButton['state'] = 'normal'

    def Get_Cordinate_Points(self, wid_typ):
        call = GetPointsDialog(self.root, wid_typ)
        """
        CALL THE TOPLEVEL WINDOW FROM THIS METHOD,
        SHOULD GET THE CO-ORDINATES AND COLOR AND STRIKE/UNSTRIKE PROPERTIES
        AND DECIDE TO CALL THE Create_Circle OR
        Create_OR Create_Rect Line METHODS

        """
        if not call.ok:
            msg.showinfo("Error", "No coordinates have been entered")
            return
        self.X = call.x1
        self.Y = call.y1
        self.radius = call.rad
        self.X1_COORD = call.x1
        self.Y1_COORD = call.y1
        self.X2_COORD = call.x2
        self.Y2_COORD = call.y2
        self.COLOR = call.color
        self.DASH = call.dash.get()
        if wid_typ == 0:
            self.Create_Circle(self.X1_COORD,
                               self.Y1_COORD,
                               self.radius,
                               self.DASH,
                               self.COLOR)
        elif wid_typ == 1:
            self.Create_Line(self.X1_COORD,
                             self.Y1_COORD,
                             self.X2_COORD,
                             self.Y2_COORD,
                             self.DASH,
                             self.COLOR)
        elif wid_typ == 2:
            self.Create_Rect(self.X1_COORD,
                             self.Y1_COORD,
                             self.X2_COORD,
                             self.Y2_COORD,
                             self.DASH,
                             self.COLOR)

    def Create_Circle(self, x1, y1, rad, Da_or_UDa, Colo):

        """
        CREATE CIRCLE ON THE CANVAS WITH THE CORDINATES AND VALUES
        RECEIVED FROM THE USER INPUT
        """
        if Da_or_UDa:
            self.cnvs.create_oval(x1 - rad, y1 - rad, x1 + rad,
                                  y1 + rad, outline=Colo, dash=(4, 4), width=2)
        else:
            self.cnvs.create_oval(x1 - rad, y1 - rad, x1 + rad,
                                  y1 + rad, outline=Colo, width=2)
        self.cnvs.pack()

    def Create_Line(self, x1, y1, x2, y2, Da_or_UDa, Colo):
        """
        CREATE LINE ON THE CANVAS WITH THE CORDINATES
        AND VALUES RECEIVED FROM THE USER INPUT
        """
        if Da_or_UDa:
            self.cnvs.create_line(x1, y1, x2, y2, fill=Colo,
                                  dash=(4, 4), width=2)
        else:
            self.cnvs.create_line(x1, y1, x2, y2, fill=Colo, width=2)
        self.cnvs.pack()

    def Create_Rect(self, x1, y1, x2, y2, Da_or_UDa, Colo):
        """
        CREATE RECTANGE ON THE CANVAS WITH THE CORDINATES
        AND VALUES RECEIVED FROM THE USER INPUT
        """
        if Da_or_UDa:
            self.cnvs.create_rectangle(x1, y1, x2, y2, outline=Colo,
                                       dash=(4, 4), width=2)
        else:
            self.cnvs.create_rectangle(x1, y1, x2, y2, outline=Colo, width=2)
        self.cnvs.pack()

    def clear_canvas(self):
        '''
        triggered when the menu command 'Clear' is clicked
        delete everything from the canvas and set the coefficients to 0's
        '''
        self.cnvs.delete("all")
        self.X = 0
        self.Y = 0
        self.radius = 0
        self.X1_COORD = 0
        self.Y1_COORD = 0
        self.X2_COORD = 0
        self.Y2_COORD = 0
        self.COLOR = 'black'
        self.DASH = 0
        self.cords.clear()
        self.corde.clear()
        self.ocords.clear()
        self.ocorde.clear()
        self.x.clear()
        self.y.clear()

    def save_canvas(self):
        '''
        triggered when the menu command 'Save plot as .PS' is clicked
        save the graph as '{your_student_id_number}.ps'
        '''
        self.cnvs.postscript(file="1013967.ps")

    def show_help_about(self):
        '''
        triggered when the menu command 'About' is clicked
        Show an information dialog displaying
        your name on one line and id number on the second
        '''
        msg.showinfo("About PY Paint", "Created by: Durga Nikhil\nID: 1009845")

    def exit(self):
        '''
        triggered when the menu command 'Exit' is clicked
        Ask if the user is sure about exiting
        the application and if the answer is yes then quit the main window
        '''
        if msg.askyesno("Exit", "Are you sure?"):
            self.root.quit()

p = Painter()
