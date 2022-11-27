# Imports #
import tkinter as tk  # GUI library

# Globals #
calculation = ""

# Colors #
bg_color = "#1e1e2e"
btn_bg_color = "#1e1e2e"
fg_color = "#cdd6f4"

# Fonts #
font_btn = ("Arial", 14)
font_box = ("Arial", 20)


# Functions #
# Append input to calculation and display in text box
def add_to_calculation(symbol):
    global calculation

    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


# Evaluate appended calculation
def evaluate_calculation():
    global calculation

    # Basic error handling to prevent arbitrary code execution
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    except Exception as e:
        clear_field()
        e = "Error"
        text_result.insert(1.0, e)


# Clear the text box
def clear_field():
    global calculation

    calculation = ""
    text_result.delete(1.0, "end")


# Main #
if __name__ == "__main__":
    # Window settings
    root = tk.Tk()

    root.title("Py Calc  ")  # title
    root.geometry("315x245")  # window size
    root.configure(bg=bg_color)  # window background color

    # Text Box #
    text_result = tk.Text(
        root,
        padx=1,
        pady=1,
        bg=bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,
        height=2,
        width=20,
        font=font_box
    )
    text_result.grid(columnspan=5)

    # Buttons #
    btn_1 = tk.Button(
        root,
        text="1",
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation(1), width=5, font=font_btn
    )

    # Button positioning
    btn_1.grid(row=2, column=1)

    btn_2 = tk.Button(
        root,
        text="2",
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation(2), width=5, font=font_btn
    )

    # Button positioning
    btn_2.grid(row=2, column=2)

    btn_3 = tk.Button(
        root,
        text="3",
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation(3), width=5, font=font_btn
    )

    # Button positioning
    btn_3.grid(row=2, column=3)

    btn_4 = tk.Button(
        root,
        text="4",
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation(4), width=5, font=font_btn
    )

    # Button positioning
    btn_4.grid(row=3, column=1)

    btn_5 = tk.Button(
        root,
        text="5",
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation(5), width=5, font=font_btn
    )

    # Button positioning
    btn_5.grid(row=3, column=2)

    btn_6 = tk.Button(
        root,
        text="6",
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation(6), width=5, font=font_btn
    )

    # Button positioning
    btn_6.grid(row=3, column=3)

    btn_7 = tk.Button(
        root,
        text="7",
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation(7), width=5, font=font_btn
    )

    # Button positioning
    btn_7.grid(row=4, column=1)

    btn_8 = tk.Button(
        root,
        text="8",
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation(8), width=5, font=font_btn
    )

    # Button positioning
    btn_8.grid(row=4, column=2)

    btn_9 = tk.Button(
        root,
        text="9",
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation(9), width=5, font=font_btn
    )

    # Button positioning
    btn_9.grid(row=4, column=3)

    btn_0 = tk.Button(
        root,
        text="0",
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation(0), width=5, font=font_btn
    )

    # Button positioning
    btn_0.grid(row=5, column=2)

    btn_plus = tk.Button(
        root,
        text="\u002B",  # Addition unicode
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation("+"), width=5, font=font_btn
    )

    # Button positioning
    btn_plus.grid(row=2, column=4)

    btn_sub = tk.Button(
        root,
        text="\u2212",  # Subtraction unicode
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation("-"), width=5, font=font_btn
    )

    # Button positioning
    btn_sub.grid(row=3, column=4)

    btn_mult = tk.Button(
        root,
        text="\u00D7",  # Multiplication unicode
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation("*"), width=5, font=font_btn
    )

    # Button positioning
    btn_mult.grid(row=4, column=4)

    btn_div = tk.Button(
        root,
        text="\u00F7",  # Division unicode
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation("/"), width=5, font=font_btn
    )

    # Button positioning
    btn_div.grid(row=5, column=4)

    btn_lper = tk.Button(
        root,
        text="\u0028",  # Left parenthesis unicode
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation("("), width=5, font=font_btn
    )

    # Button positioning
    btn_lper.grid(row=5, column=1)

    btn_rper = tk.Button(
        root,
        text="\u0029",  # Right parenthesis unicode
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,

        # Use lambda to only run when button is pressed
        command=lambda: add_to_calculation(")"), width=5, font=font_btn
    )

    # Button positioning
    btn_rper.grid(row=5, column=3)

    btn_eq = tk.Button(
        root,
        text="\u003D",  # Equal unicode
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,
        command=evaluate_calculation, width=13, font=font_btn
    )

    # Button positioning
    btn_eq.grid(row=6, column=3, columnspan=2)

    btn_c = tk.Button(
        root,
        text="C",
        bg=btn_bg_color,
        fg=fg_color,
        highlightbackground=btn_bg_color,
        command=clear_field, width=13, font=font_btn
    )

    # Button positioning
    btn_c.grid(row=6, column=1, columnspan=2)

    root.mainloop()
