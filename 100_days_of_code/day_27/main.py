from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


# Button
button = Button(text="Press me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Press me")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
