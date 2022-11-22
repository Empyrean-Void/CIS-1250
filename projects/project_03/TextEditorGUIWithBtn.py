from tkinter import * #import all of tkinter's members into this application

def clicked():
    print('I was clicked!')

if __name__ == "__main__":
    top = Tk() #creat top level window
    btn = Button() #instantiate a button
    btn.pack() #use pack layout manager to position the button on the form
    btn['text'] = 'Click me!' #Set the text attribute of the button
    btn['command'] = clicked
    mainloop() #start the main event loop that monitors for when the button is clicked along with other form events