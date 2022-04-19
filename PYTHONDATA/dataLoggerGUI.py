from distutils import command
from posixpath import basename
import tkinter as tk
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfilename
from lineCounter import run_line_counter
import time


timestr = time.strftime("%d/%m/%Y-%H:%M:%S")
print (timestr)

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
    lbl_value["text"] = f"Data for uploaded at {timestr}"
    
    window.title(f"OEE Datalogger {filepath} ")

window = tk.Tk()
window.title("OEE Datalogger")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit =tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text ="Open", command=open_file)
btn_log = tk.Button(fr_buttons, text="Log Data", command=log_data)
lbl_value = tk.Label(master=window, text="Waiting for Data...")

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_log.grid(row=1, column=0, sticky="ew", padx=5)
lbl_value.grid(row=1, column=1, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")



window.mainloop()

###To do: improve GUI, add microchip logo as an image, add text pop up when data is logged succsessfully###