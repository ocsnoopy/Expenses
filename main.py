from msilib.schema import Error
from classes.pages.expenses_list import ExpensesList
from classes.pages.add_expense import AddExpense
from classes.pages.expense_tile import ExpenseTile

from classes.objects.expense import Expense

import tkinter as tk
import sys
import csv


class TemplateApp(tk.Tk):
    
    expense_list = []
    object_id = None
    
    def __init__(self):
        tk.Tk.__init__(self)
        self._Canvas = None
        self.switch_canvas('ExpensesList')

    def switch_canvas(self, canvas_class):
        template_canvas_class = getattr(sys.modules[__name__], canvas_class)
        new_canvas = template_canvas_class(self)
        if self._Canvas is not None:
            self._Canvas.destroy()
        self._Canvas = new_canvas
        self._Canvas.pack()
     
    def get_object_array(self):
        with open('data/backup.csv', 'r') as array:
            lines = csv.reader(array)
            expenses = []
            try:
                for l in lines:
                    print('error: ', l)
                    line = [l[0], l[1], l[2], l[3]]
                    print('line: ', line)
                    expenses.append(line)
                    print('self.expense_list:---- ', self.expense_list)
                array.close()
            except Error as error:
                print('Erroooor: ', error)
            finally:
                return expenses
        
    def add_expense(self, expense):
        number = expense.EXPENSE_NUMBER
        name = expense.NAME
        amount = expense.AMOUNT
        date = expense.DATE
        print('aount: ', amount)
        new_exp = [number, name, amount, date]
        self.expense_list.append(new_exp)
        
        
        
    def update_expense(self, expense):
        number = expense.EXPENSE_NUMBER
        name = expense.NAME
        amount = expense.AMOUNT
        date = expense.DATE
        new_exp = [number,name, amount, date]
        exp_list = self.set_expenses_list()
        for exp in exp_list:
            if exp[0] == number:
                exp_list.append(new_exp)
                exp_list.remove(exp)
        self.expense_list = exp_list
        self.override_array()
        
    
    def override_array(self):
        with open('data/backup.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for expense in self.expense_list:
                csv_writer.writerow(expense)
        
        
        
    def set_expenses_list(self):
        self.expense_list.clear()
        expenses =self.get_object_array()
        print('expenses-------: ', expenses)
        for expense in expenses:
            self.expense_list.append(expense)
        return self.expense_list
    
    
            
    def count_csv_lines(self):
            lines_nr = 0
            with open('data/backup.csv', 'r') as f:
                lines = f.readline()
                for line in lines:
                    lines_nr += 1
            return lines_nr
                    
            
    def update_object_array(self,object):
        is_first_line = self.is_empty()
        
        if is_first_line == True:
            self.write_first_lise(object)
        else:
            self.write_other_lines(object)
            
    def is_empty(self):
        with open('data/backup.csv', 'r') as array:
            lines = csv.reader(array)
            is_empty = []

            try:
                for l in lines:
                    pass
                is_empty = False
                array.close()
                
            except Error as error:
                is_empty = True
            finally:
                array.close()
                return is_empty
    
    
    def write_first_lise(self, object):
        number = object.EXPENSE_NUMBER
        name = object.NAME
        amount = object.AMOUNT
        date = object.DATE
        amount_list = [number, name, amount, date]
        print('amount_list: ', amount_list)
        lines_nr = self.count_csv_lines()
        print('lines: ', lines_nr)
        with open('data/backup.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(amount_list)
            
    
    def write_other_lines(self, object):
        number = object.EXPENSE_NUMBER
        name = object.NAME
        amount = object.AMOUNT
        date = object.DATE
        amount_list = [number, name, amount, date]
        print('amount_list: ', amount_list)
        lines_nr = self.count_csv_lines()
        print('lines: ', lines_nr)
        with open('data/backup.csv', 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(amount_list)
    
    
    def get_expense_id(self, object):
        self.object_id = object[0]
        
    
    def set_expense_id(self):
        return self.object_id
    
    
    
    
            
    
    
        
        
            
        
        
if __name__ == '__main__':
    app = TemplateApp()
    app.get_object_array()
    app.mainloop()