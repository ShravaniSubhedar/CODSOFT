import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        
        self.expression = ""
        
        self.input_field = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=2, relief='ridge')
        self.input_field.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, padx=20, pady=20, font=('Arial', 18),
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_field.delete(0, tk.END)
        elif char == '=':
            try:
                result = eval(self.expression)
                self.input_field.delete(0, tk.END)
                self.input_field.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception as e:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_field.delete(0, tk.END)
            self.input_field.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
