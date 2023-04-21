from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=400, height=100)

# Entry
input_box = Entry(width=15)
input_box.grid(column=2, row=1)

# Labels
miles_label = Label(text="Miles")
info_label = Label(text="is equal to:")
km_label = Label(text="Km")
result_label = Label(text="0")

miles_label.grid(column=3, row=1)
info_label.grid(column=1, row=2)
km_label.grid(column=3, row=2)
result_label.grid(column=2, row=2)


# Buttons
def button_clicked():
    result_label.config(text=f"{int(input_box.get()) * 1.609344}")


calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=2, row=3)

window.mainloop()
