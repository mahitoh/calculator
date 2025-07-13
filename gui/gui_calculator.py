import tkinter as tk

class calculator:
    # The __init__ method is called when a calculator object is created ; it sets up the GUI

    def __init__(self, root):

        # store the main window (root) as an instance variable to access it throughout the class

        self.root = root

        # set the window title to "GUI CALCULATOR" (appears at the top of the window)
        self.root.title("GUI CALCULATOR")

        # set the window size to 300 pixels wide and 400 pixels tall for a compact calculator
        self.root.geometry("300x400")

        # initialise an empty string to store the user's input (e.g., "5 + 2")
        self.expression = ""

        # create a StringVar to dynamically update the text in the display (Entry widget)
        self.result_var = tk.StringVar()

        self.display = tk.Entry(root, textvariable = self.result_var, font = ("Arial", 20), bd=10, insertwidth = 2, width = 14, borderwidth = 4)
        self.display.grid(row = 0, column = 0, columnspan = 4)

        button_layout = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in button_layout:

            if text == '=':
                btn = tk.Button(root, text = text, font = ("Arial", 14), command = self.evaluate)
            
            elif text == 'C':
                btn = tk.Button(root, text = text, font = ("Arial", 14), command = self.clear)

            else:
                btn = tk.Button(root, text = text, font = ("Arial", 14), command = lambda x = text: self.add_to_expression(x))

            btn.grid(row = row, column = col, sticky = "nsew", padx = 5, pady = 5)

        for i in range(6):
            self.root.grid_rowconfigure(i, weight = 1)

        for i in range(4):
            self.root.grid_columnconfigure(i, weight = 1)

    def add_to_expression(self, value):

        self.expression += value

        self.result_var.set(self.expression)

    def clear(self):

        self.expression = ""

        self.result_var.set("")

    def evaluate(self):

        try:

            result = eval(self.expression)

            self.result_var.set(result)

            self.expression = str(result)

        except ZeroDivisionError:

            self.result_var.set("Error")

            self.expression = ""
        except:

            self.result_var.set("Error")

            self.expression = ""

if __name__ == "__main__":

    root = tk.Tk()

    app = calculator(root)

    root.mainloop()