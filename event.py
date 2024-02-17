from customtkinter import *

app = CTk()
app.geometry("500x400")

# BUTTON
def click():
    print("BUTTON CLICKED")

btn = CTkButton(master=app, text="Click Me", command=click)

btn.place(relx=0.5, rely=0.5, anchor='center')


app.mainloop()



# ComboBox

def change_handler(value):
    print(f"SELECTED VALUE: {value}")

btn = CTkComboBox(master=app, values=["Option1", "Option2", "Option3"], command=change_handler)

btn.place(relx=0.5, rely=0.5, anchor='center')
