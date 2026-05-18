# gui_calculator_fixed.py
import tkinter as tk
from tkinter import messagebox
import sys

def safe_main():
    """Safe wrapper to handle the debugger issue"""
    try:
        # Your calculator GUI code
        class Calculator:
            def __init__(self, root):
                self.root = root
                self.root.title("Python Calculator")
                self.root.geometry("300x400")
                self.root.resizable(False, False)
                
                self.expression = ""
                self.input_text = tk.StringVar()
                
                self.create_widgets()
            
            def create_widgets(self):
                # Display frame
                display_frame = tk.Frame(self.root)
                display_frame.pack(expand=True, fill="both")
                
                # Input field
                input_field = tk.Entry(display_frame, font=('Arial', 18), 
                                      textvariable=self.input_text, 
                                      width=50, justify="right", bd=0, bg="#f0f0f0")
                input_field.pack(ipady=10)
                
                # Buttons frame
                buttons_frame = tk.Frame(self.root)
                buttons_frame.pack(expand=True, fill="both")
                
                # Button layout
                buttons = [
                    ['C', 'DEL', '%', '/'],
                    ['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['00', '0', '.', '=']
                ]
                
                # Create buttons
                for i, row in enumerate(buttons):
                    for j, text in enumerate(row):
                        button = tk.Button(buttons_frame, text=text, font=('Arial', 14),
                                         command=lambda x=text: self.button_click(x),
                                         relief="flat", bg="white", height=2)
                        button.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
                        
                        # Make = button different color
                        if text == '=':
                            button.config(bg="#4CAF50", fg="white")
                        elif text in ['C', 'DEL', '%', '/', '*', '-', '+']:
                            button.config(bg="#e0e0e0")
                
                # Configure grid weights
                for i in range(5):
                    buttons_frame.grid_rowconfigure(i, weight=1)
                for j in range(4):
                    buttons_frame.grid_columnconfigure(j, weight=1)
            
            def button_click(self, char):
                if char == 'C':
                    self.expression = ""
                    self.input_text.set("")
                
                elif char == 'DEL':  # Backspace
                    self.expression = self.expression[:-1]
                    self.input_text.set(self.expression)
                
                elif char == '=':
                    try:
                        result = str(eval(self.expression))
                        self.input_text.set(result)
                        self.expression = result
                    except:
                        messagebox.showerror("Error", "Invalid Expression")
                        self.expression = ""
                        self.input_text.set("")
                
                else:
                    self.expression += str(char)
                    self.input_text.set(self.expression)
        
        # Create and run the application
        root = tk.Tk()
        app = Calculator(root)
        root.mainloop()
        
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to close...")

if __name__ == "__main__":
    # This might avoid the debugger issue
    if 'debugpy' in sys.modules:
        print("Running in debug mode - using safe execution")
    
    safe_main()
