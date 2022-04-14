from distutils import command
import tkinter as tk
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfilename
from lineCounter import run_line_counter

filepath = ''

def open_file():
    global filepath
    "Open file path for program"
    filepath = askopenfilename(
        filetypes=[("RAM Files", "*.ram"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END) ###<<<Error was here, do not quote tk.END!!###
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"OEE Datalogger - {filepath}")


def log_data():
    "Log OEE data to the database"
    global filepath
    run_line_counter(filepath)
    
    window.title(f"OEE Datalogger {filepath} ")

window = tk.Tk()
window.title("OEE Datalogger")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit =tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text ="Open", command=open_file)
btn_log = tk.Button(fr_buttons, text="Log Data", command=log_data)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_log.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")



window.mainloop()