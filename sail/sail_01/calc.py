# Tkinter is a Python binding to the Tk GUI toolkit. Tk is a free and
# open-source, cross-platform widget toolkit that provides a library of basic
# elements of GUI widgets for building a graphical user interface (GUI) in many
# programming languages. Tkinter is included with standard Linux, Microsoft
# Windows and Mac OS X installs of Python.
# https://en.wikipedia.org/wiki/Tkinter
from tkinter import Button, Entry, Tk, END

# NOTE: Here, we are importing the constants that you appropriately set to
#       populate the button labels. In case of complex programs it is important
#       to separate the code into several files. Here, you see an example of
#       how you can access the code from different files. Do not worry about it
#       too much now. We will extensively cover this concept in future lectures.
from task1 import BUTTON_0, BUTTON_1, BUTTON_2, BUTTON_3, BUTTON_4, BUTTON_5,\
    BUTTON_6, BUTTON_7, BUTTON_8, BUTTON_9, BUTTON_ADD, BUTTON_SUBTRACT,\
    BUTTON_MULTIPLY, BUTTON_DIVIDE, BUTTON_CLEAR, BUTTON_EQUAL

# Classes are a convenient method of grouping related data and functionality
# together. This is a complex concept that will be extensively covered in future
# lectures. Do not be worried if you do not understand how it works or why is it
# useful at this point.
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")
        master.resizable(width=False, height=False)
        self.expression = Entry(master, width=36, borderwidth=5, justify="right")
        self.expression.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        """
        Method that creates the buttons
        INPUT:
        OUTPUT: None
        """
        # We first create each button one by one with the value we want
        # Using add_button() method which is described below
        btn_0 = self.add_button(BUTTON_0)
        btn_1 = self.add_button(BUTTON_1)
        btn_2 = self.add_button(BUTTON_2)
        btn_3 = self.add_button(BUTTON_3)
        btn_4 = self.add_button(BUTTON_4)
        btn_5 = self.add_button(BUTTON_5)
        btn_6 = self.add_button(BUTTON_6)
        btn_7 = self.add_button(BUTTON_7)
        btn_8 = self.add_button(BUTTON_8)
        btn_9 = self.add_button(BUTTON_9)

        # Arithmetical Operators
        btn_add = self.add_button(BUTTON_ADD)
        btn_sub = self.add_button(BUTTON_SUBTRACT)
        btn_mult = self.add_button(BUTTON_MULTIPLY)
        btn_div = self.add_button(BUTTON_DIVIDE)

        # Execution
        btn_clear = self.add_button(BUTTON_CLEAR)
        btn_equal = self.add_button(BUTTON_EQUAL)

        # Arrange the buttons into lists which represent calculator rows
        row_1=[btn_7, btn_8,btn_9, btn_add]
        row_2=[btn_4, btn_5,btn_6, btn_sub]
        row_3=[btn_1, btn_2,btn_3, btn_mult]
        row_4=[btn_clear, btn_0, btn_equal, btn_div]

        # Each button is assigned to a particular location in the layout
        for row_i, row in enumerate([row_1, row_2, row_3, row_4], start=1):
            for col_i, button in enumerate(row, start=0):
                button.grid(row=row_i, column=col_i, columnspan=1)

    def add_button(self, value):
        """
        This method handles creation of a button and makes it clickable.
        INPUT: Calculator, string, string
        OUTPUT: Button
        """
        str_value = str(value)
        return Button(self.master, text=str_value, width=9,
                      command=lambda: self.click_button(str_value))

    def click_button(self, value):
        """
        This method created actions that will happen in the calculator after a
        button is clicked.
        INPUT: string
        OUTPUT: None
        """
        current_equation = str(self.expression.get())
        if current_equation == 'ERROR':
            current_equation = ''
        
        # If user clicked BUTTON_CLEAR, then clear the screen
        if value == BUTTON_CLEAR:
            self.expression.delete(-1, END)
        
        # If user clicked BUTTON_EQUAL, then compute the answer and display it
        elif value == BUTTON_EQUAL:
            try:
                answer = str(eval(current_equation))
            except Exception:
                answer = "ERROR"
            self.expression.delete(-1, END)
            self.expression.insert(0, answer)
        
        # If user clicked any other button, then add it to the equation line
        else:
            self.expression.delete(0, END)
            self.expression.insert(0, current_equation + value)


# Execution
if __name__=='__main__':
    # Create the main window of an application
    root = Tk()

    # Tell our calculator class to use this window
    my_gui = Calculator(root)
    
    # Executable loop on the application, waits for user input
    root.mainloop()