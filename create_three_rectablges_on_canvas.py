from tkinter import *
from time import *

class canvas(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.my_canvas = Canvas(width = 150, height = 150, bg='white')
        self.my_canvas.grid()

        red_rect = self.my_canvas.create_rectangle(10, 10, 20, 20, fill = 'red')
        self.my_canvas.create_rectangle(10, 30, 20, 40, fill = 'yellow')
        self.my_canvas.create_rectangle(10, 50, 20, 60, fill = 'blue')

        for i in range(10):
            increment = i*10
            self.my_canvas.coords(red_rect, 10 + increment, 10 + increment, 20 + increment, 20 + increment)
            sleep(1)
            self.my_canvas.update()
            
        print("Find all shapes: ")
        print(self.my_canvas.find_enclosed(0, 0, 150, 150))

        print("Find middle shapes: ")
        print(self.my_canvas.find_enclosed(0, 25, 30, 45))

        print("Find no shapes: ")
        print(self.my_canvas.find_enclosed(0, 0, 1, 1))
              
frame_01 = canvas()
frame_01.mainloop()
