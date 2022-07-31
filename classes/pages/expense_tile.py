import tkinter as tk
from tkinter import ttk

from classes.objects.expense import Expense

from typing import TYPE_CHECKING

class ExpenseTile(tk.Frame):

    if TYPE_CHECKING:
        from main import MainApp
        app = MainApp()

    def __init__(self, master, *args, **kwargs):

        tk.Frame.__init__(self, master, *args, **kwargs)
        self.canvas = tk.Canvas(self, bg='white', width=500, height=500)
        self.canvas.pack(fill="both", expand=True)
        master.title('Expense Tile')

        expense_id = master.set_expense_id()
        expense_list = master.set_expenses_list()
        expense_object = None
        for expense in expense_list:
            if expense[0] == expense_id:
                expense_object = expense
                

        var_name = tk.StringVar()
        var_name.set(expense_object[1])
        
        var_amount = tk.StringVar()
        var_amount.set(expense_object[2])
        
        var_date = tk.StringVar()
        var_date.set(expense_object[3])
        
        expense_name_entry =tk.Entry(self.canvas, textvariable=var_name)
        expense_amount_entry =tk.Entry(self.canvas, textvariable=var_amount)
        expense_date_entry = tk.Entry(self.canvas, textvariable=var_date)
        
        
        ex_name_label = tk.Label( self.canvas, text='Name')
        ex_amount_label = tk.Label( self.canvas, text='Amount')
        ex_date_label = tk.Label( self.canvas, text='Date')
        
        self.canvas.create_window(250, 50, window=expense_name_entry)
        self.canvas.create_window(250, 100, window=expense_amount_entry)
        self.canvas.create_window(250, 150, window=expense_date_entry)
        
        self.canvas.create_window(150, 50, window=ex_name_label)
        self.canvas.create_window(150, 100, window=ex_amount_label)
        self.canvas.create_window(150, 150, window=ex_date_label)

        
        def handle_back_button():
            master.switch_canvas('ExpensesList')
            
            
        def handle_save_button():
            exp_number = expense_id
            name = expense_name_entry.get()
            amount = expense_amount_entry.get()
            date = expense_date_entry.get()
            new_expense = Expense(exp_number,name,amount,date)
            master.update_expense(new_expense)
            master.switch_canvas('ExpensesList')
        
        
        back_button = tk.Button(self, text='Back',
                                borderwidth=2,  bg='white', command=handle_back_button)
        back_button_button_canvas = self.canvas.create_window(
            10, 450, anchor="nw", window=back_button)
        
        
        save_button = tk.Button(self, text='Save',
                                borderwidth=2,  bg='white', command=handle_save_button)
        save_button_button_canvas = self.canvas.create_window(
            450, 450, anchor="nw", window=save_button)