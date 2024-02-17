from customtkinter import *

app = CTk()
app.geometry("500x400")

def click_handler():
    print(f'Entered Value: {textBox.get('0.0', 'end')}')

textBox = CTkTextbox(master=app, border_color="#FFCC70", border_width=2)
btn = CTkButton(master=app, text="SUBMIT", command=click_handler)

textBox.pack(anchor="s", expand=True, pady=10)
btn.pack(anchor="n", expand=True)

app.mainloop()
