import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    """
    Retrieves user input, calculates the simple interest, 
    and updates the result label.
    """
    try:
        # Retrieve values from the entry fields and convert to floats
        p = float(entry_principal.get())
        r = float(entry_rate.get())
        t = float(entry_time.get())
        
        # Calculate simple interest and total amount
        si = (p * r * t) / 100
        total_amount = p + si
        
        # Update the text on the results label
        label_result.config(text=f"Simple Interest: ${si:.2f}\nTotal Amount: ${total_amount:.2f}")
        
    except ValueError:
        # Show an error pop-up box if the user types letters instead of numbers
        messagebox.showerror("Input Error", "Please enter numerical values only.")

#Main Window Setup 
window = tk.Tk()
window.title("Simple Interest Calculator")
window.geometry("300x300") # Width x Height
window.resizable(False, False) # Prevents the window from being resized

#Input Fields & Labels
#Principal
tk.Label(window, text="Principal Amount ($):").pack(pady=(15, 0))
entry_principal = tk.Entry(window, justify="center")
entry_principal.pack(pady=5)

#Rate
tk.Label(window, text="Annual Interest Rate (%):").pack()
entry_rate = tk.Entry(window, justify="center")
entry_rate.pack(pady=5)

#Time
tk.Label(window, text="Time (Years):").pack()
entry_time = tk.Entry(window, justify="center")
entry_time.pack(pady=5)

#Calculate Button
btn_calculate = tk.Button(window, text="Calculate", command=calculate_interest, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_calculate.pack(pady=15)

#Results Display
label_result = tk.Label(window, text="Simple Interest: $0.00\nTotal Amount: $0.00", font=("Arial", 11, "bold"), fg="#333333")
label_result.pack(pady=10)

#Run the Application
window.mainloop()
