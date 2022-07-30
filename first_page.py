import tkinter as tk
from typing import TYPE_CHECKING

class FirstPage(tk.Frame):
    if TYPE_CHECKING:
        from main import MainApp
        app = MainApp()
        
    def __init__(self, master, *args, **kwargs):

        tk.Frame.__init__(self, master, *args, **kwargs)
        self.canvas = tk.Canvas(self, bg='white', width=600, height=600)
        self.canvas.pack(fill="both", expand=False)
        master.title('first page')
        master.resizable(0,0)
        
        
        def handle_next_button():
            print('proccede to next page')
            master.switch_canvas('SecondPage')
    
    
        next_button = tk.Button(self, text='Next', borderwidth=2, bg='white', command=handle_next_button)
        next_button_canvas = self.canvas.create_window(550,550,anchor='nw', window=next_button)
        
