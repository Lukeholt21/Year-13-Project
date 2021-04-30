import tkinter as tk
import datetime

CELL_SIZE = (100, 50)
FIRST_ROW_HEIGHT = 20

class Cell(tk.Canvas):
    def __init__(self, root,
        width = CELL_SIZE[0],
        height = CELL_SIZE[1],
        highlightthickness = 1,
        background = 'white',
        highlightbackground = 'black',
        highlightcolor = 'red',
        *args, **kwargs):

        tk.Canvas.__init__(self, root,
            width = width,
            height = height,
            background = background,
            highlightthickness = highlightthickness,
            highlightbackground = highlightbackground,
            highlightcolor = highlightcolor,
            *args, **kwargs)

class Calendar(tk.Frame):
    def __init__(self, root, rows=0, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)

        # create the canvas and frame
        self.calendar_canvas = tk.Canvas(self)
        self.calendar_frame = tk.Frame(self.calendar_canvas)
        self.calendar_canvas.create_window((4,4), window=self.calendar_frame, anchor="nw", tags="self.calendar_frame")
        self.calendar_canvas.pack(side="top", fill="both", expand=True)

        # building scrollbar
        self.scrollbar = tk.Scrollbar(self, orient='horizontal', command=self.calendar_canvas.xview)
        self.scrollbar.pack(side="bottom", fill="x")

        # hooking up scrollbar
        self.calendar_canvas.configure(xscrollcommand=self.scrollbar.set)
        self.calendar_frame.bind("<Configure>", self.onFrameConfigure)

        # variables
        self.rows = rows
        self.cells = []


    def onFrameConfigure(self, event):
        self.calendar_canvas.configure(scrollregion=self.calendar_canvas.bbox("all"))

    def set(self, day=0):
        today = datetime.date.today()

        for i in range(day):
            self.cells.append([])

            # create first row (indicating the date)
            cell = Cell(self.calendar_frame, height=FIRST_ROW_HEIGHT)
            cell.grid(row=0, column=i)

            # add the date label into the first row
            cell.create_text(
                CELL_SIZE[0]/2,
                FIRST_ROW_HEIGHT/2,
                text = (today + datetime.timedelta(days=i)).strftime('%d/%m/%y'))

            for c in range(self.rows):
                cell = Cell(self.calendar_frame)
                cell.grid(row=c+1, column=i)

                self.cells[i].append(cell)
                
                
                
root = tk.Tk()
calendar = Calendar(root, rows=3)
calendar.set(day=10)
calendar.pack(fill='both', expand=True)
root.mainloop()