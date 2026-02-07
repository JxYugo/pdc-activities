import tkinter as tk

def add_grade_field():
    entry = tk.Entry(scrollable_frame, width=10)
    entry.pack(pady=4)
    grade_entries.append(entry)
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("GWA Calculator")
root.geometry("420x500")
root.resizable(False, False)

tk.Label(root, text="GWA Calculator", font=("Arial", 16, "bold")).pack(pady=10)

box_frame = tk.Frame(root, bd=2, relief="groove")
box_frame.pack(padx=15, pady=10, fill="both")

grades_container = tk.Frame(box_frame)
grades_container.grid(row=0, column=0, padx=5, pady=5)

canvas = tk.Canvas(grades_container, height=220, width=150)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(grades_container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

grade_entries = []

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Grade", width=12, command=add_grade_field).grid(row=0, column=0, padx=5)

for _ in range(5):
    add_grade_field()

root.mainloop() 