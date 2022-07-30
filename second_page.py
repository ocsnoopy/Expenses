import tkinter as tk
from typing import TYPE_CHECKING

class SecondPage(tk.Frame):
    if TYPE_CHECKING:
        from main import MainApp
        app = MainApp()
        
    def __init__(self, master, *args, **kwargs):

        tk.Frame.__init__(self, master, *args, **kwargs)
        self.canvas = tk.Canvas(self, bg='blue', width=200, height=600)
        self.canvas.pack(fill="both", expand=True)
        master.title('second page')
        master.resizable(0,0)
        
        
        def handle_back_button():
            print('go back')
            master.switch_canvas('FirstPage')
        
        
        back_button = tk.Button(self, text='Back', borderwidth=2, bg='white', command=handle_back_button)
        back_button_canvas = self.canvas.create_window(50,550,anchor='nw', window=back_button)