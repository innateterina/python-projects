from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# Label1
equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)

# label2
kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

# label3
label_3 = Label(text="Miles")
label_3.grid(column=2, row=0)

# label4
kilom = Label(text="Km")
kilom.grid(column=2, row=1)

# entry
kilom_input = Entry(width=7)
kilom_input.grid(column=1, row=0)


# button
def button_clicked():
    miles = float(kilom_input.get())
    km = round(miles * 1.609)
    kilometer_result.config(text=f"{km}")


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
