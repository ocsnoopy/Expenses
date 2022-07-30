import tkinter as tk
import sys
from first_page import FirstPage
from second_page import SecondPage

class TemplateApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._Canvas = None
        self.switch_canvas('FirstPage')

    def switch_canvas(self, canvas_class):
        template_canvas_class = getattr(sys.modules[__name__], canvas_class)
        new_canvas = template_canvas_class(self)
        if self._Canvas is not None:
            self._Canvas.destroy()
        self._Canvas = new_canvas
        self._Canvas.pack()
        
        
        
if __name__ == '__main__':
    app = TemplateApp()
    app.mainloop()