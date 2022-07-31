import tkinter as tk
from tkinter import ttk

from typing import TYPE_CHECKING

class ExpensesList(tk.Frame):

    if TYPE_CHECKING:
        from main import MainApp
        app = MainApp()

    def __init__(self, master, *args, **kwargs):

        tk.Frame.__init__(self, master, *args, **kwargs)
        self.canvas = tk.Canvas(self, bg='white', width=800, height=520)
        self.canvas.pack(fill="both", expand=True)
        master.title('Expenses')
        expenses_list = master.set_expenses_list()
        
        expenses_frame = tk.LabelFrame(self.canvas, text='Search Data')
        expenses_frame.place(height=470, width=800)
        
        tv1 = ttk.Treeview(expenses_frame, columns=(1,2,3,4),
                           show='headings', height='5')
        
        tv1.place(relheight=1, relwidth=1)
        tv1.heading(1, text='NR')
        tv1.heading(2, text='Name')
        tv1.heading(3, text='Amount')
        tv1.heading(4, text='Date')

        scroll_bar_y = tk.Scrollbar(
            expenses_frame, orient='vertical', command=tv1.yview)
        scroll_bar_x = tk.Scrollbar(
            expenses_frame, orient='horizontal', command=tv1.xview)
        tv1.configure(xscrollcommand=scroll_bar_x.set,
                      yscrollcommand=scroll_bar_y.set)
        scroll_bar_x.pack(side='bottom', fill='x')
        scroll_bar_y.pack(side='right', fill='y')

        
        print('expenses_list: ', expenses_list)

        def on_double_click(event):
            item = tv1.identify('item', event.x, event.y)
            item_nr = int(item[1:])
            item_nr -= 1
            clicked_record = expenses_list[item_nr]
            master.get_expense_id(clicked_record)
            master.switch_canvas('ExpenseTile')
        
        if len(expenses_list) > 0:
            for exp in expenses_list:
                print('exp: ', exp)
                tv1.insert('', 'end', values=exp)
        tv1.bind('<Double-1>', on_double_click)
        def handle_add_expense():
            master.switch_canvas('AddExpense')
        
        
        add_expense_button = tk.Button(self, text='Add New Expense',
                                borderwidth=2,  bg='white', command=handle_add_expense)
        add_expense_button_canvas = self.canvas.create_window(
            10, 480, anchor="nw", window=add_expense_button)