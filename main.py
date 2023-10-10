import tkinter as tk

root = tk.Tk()
root.title("Calculator")

def add_digit(digit):
    value=calc.get()
    if value[0]=="0" and len(value)==1:
        value=value[1:]
    calc.delete(0,tk.END)
    calc.insert(0, value+digit)
def make_digit_button(digit):
    return tk.Button(text=digit,bd=5, font="Arial 13", command=lambda:add_digit(digit) )



calc=tk.Entry(root, justify=tk.RIGHT, font="Arial 15", width=15)
calc.insert(0, "0")
calc.grid(row=0, column=0, columnspan=4, stick="we", padx=5)





make_digit_button("1").grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_digit_button("2").grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_digit_button("3").grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_digit_button("4").grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_digit_button("5").grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_digit_button("6").grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_digit_button("7").grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_digit_button("8").grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_digit_button("9").grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_digit_button("0").grid(row=4, column=1, stick="wens", padx=5, pady=5)


def remove_digit():
    calc.delete(0, tk.END)
    calc.insert(0, "0")


clear_button = tk.Button(text="C", bd=5, fg="red", font="Arial 13", command=lambda:remove_digit )

clear_button.grid(row=3, column=3, stick="wens", padx=5, pady=5)
root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)
root.grid_columnconfigure(4, minsize=60)
root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)







root.mainloop()