from classes.objects.expense import Expense


from cgitb import text
import tkinter as tk
from tkinter import ttk


from typing import TYPE_CHECKING

class AddExpense(tk.Frame):

    if TYPE_CHECKING:
        from main import MainApp
        app = MainApp()
        
        

    def __init__(self, master, *args, **kwargs):

        tk.Frame.__init__(self, master, *args, **kwargs)
        self.canvas = tk.Canvas(self, bg='white', width=800, height=520)
        self.canvas.pack(fill="both", expand=True)
        master.title('Add Expense')


        global expense_name_entry 
        global expense_amount_entry
        global expense_date_entry 
        

        expense_name_entry =tk.Entry(self.canvas)
        expense_amount_entry =tk.Entry(self.canvas)
        expense_date_entry = tk.Entry(self.canvas)
        
        
        ex_name_label = tk.Label( self.canvas, text='Name')
        ex_amount_label = tk.Label( self.canvas, text='Amount')
        ex_date_label = tk.Label( self.canvas, text='Date')
        
        self.canvas.create_window(250, 50, window=expense_name_entry)
        self.canvas.create_window(250, 100, window=expense_amount_entry)
        self.canvas.create_window(250, 150, window=expense_date_entry)
        
        self.canvas.create_window(150, 50, window=ex_name_label)
        self.canvas.create_window(150, 100, window=ex_amount_label)
        self.canvas.create_window(150, 150, window=ex_date_label)
        
        
        def handle_save_button():
            exp_number = (len(master.set_expenses_list()) + 1)
            name = expense_name_entry.get()
            amount = expense_amount_entry.get()
            date = expense_date_entry.get()
            new_expense = Expense(exp_number,name,amount,date)
            master.add_expense(new_expense)
            master.update_object_array(new_expense)
            master.switch_canvas('ExpensesList')
        
        
        
        def handle_back_button():
            master.switch_canvas('ExpensesList')
        
        back_button = tk.Button(self, text='Back',
                                borderwidth=2,  bg='white', command=handle_back_button)
        back_button_button_canvas = self.canvas.create_window(
            10, 480, anchor="nw", window=back_button)
        
        
        save_button = tk.Button(self, text='Save',
                                borderwidth=2,  bg='white', command=handle_save_button)
        save_button_button_canvas = self.canvas.create_window(
            750, 480, anchor="nw", window=save_button)
        