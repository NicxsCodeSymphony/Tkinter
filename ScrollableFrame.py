from customtkinter import *

app = CTk()
app.geometry("500x400")

count = 0

frame = CTkScrollableFrame(master=app, fg_color="#8D6F3A", border_color="#FFCC70", border_width=2, orientation='vertical', scrollbar_button_color="#FFCC70")
frame.pack(expand=True)

label = CTkLabel(master=frame, text="This is a frame")
entry = CTkEntry(master=frame, placeholder_text="Type Something")
btn = CTkButton(master=frame, text="Click Me")

label.pack(anchor="s", expand=True, pady=10, padx=30)
btn.pack(anchor="n", expand=True, pady=10, padx=30)
entry.pack(anchor="s", expand=True, padx=30, pady=20)
CTkButton(master=frame, text="Another Widget").pack(expand=True)
CTkButton(master=frame, text="Another Widget").pack(expand=True)
CTkButton(master=frame, text="Another Widget").pack(expand=True)
CTkButton(master=frame, text="Another Widget").pack(expand=True)
CTkButton(master=frame, text="Another Widget").pack(expand=True)

app.mainloop()
