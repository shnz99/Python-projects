from tkinter import *

window = Tk()
window.title("Mile to KM")
window.config(padx=15, pady=15)


def calculate():
    result = round(int(entry.get()) * 1.609, 2)

    result_label.config(text=result)


# labels
mph_label = Label(text="Miles")
mph_label.grid(column=2, row=0)
mph_label.config(padx=10, pady=10)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

result_label = Label(text="0")
result_label.grid(column=1, row=1)
result_label.config(padx=10, pady=10)

km_label = Label(text="km")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)
# entries
entry = Entry(width=20)
entry.grid(column=1, row=0)

# buttons
button = Button(text="calculate", command=calculate)
button.grid(column=1, row=2)
button.config(padx=10, pady=2)

window.mainloop()
