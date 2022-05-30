from tkinter import *
from PIL import Image, ImageTk

ws = Tk()
ws.title('ResizeImages')
ws.geometry('800x800')
ws.config(bg='#4a7a8c')
text = StringVar()
entry_window = Entry(
    ws, justify=LEFT, width=30, borderwidth=4, textvariable=text
    )
entry_window.place(x=20, y=20)
entry_window.insert(END, 'Paste the link of the image')

disp_img = Label()
disp_img.pack(pady=20)

label = Label()
logo = ImageTk.PhotoImage(Image.open('logo.jpg').resize((100, 100)))
label.config(image=logo)
label.image = logo
label.place(x=620, y=20)

def open_file():
    file = ImageTk.PhotoImage(
        Image.open(entry_window.get().replace('"', '')).resize((100, 100))
        )
    disp_img.config(image=file)
    disp_img.image = file
    disp_img.place(x=150, y=80)

def resize_func():
    image = Image.open(entry_window.get().replace('"', ''))
    w = int(width.get())
    h = int(height.get())
    resize_img = image.resize((w, h))
    img = ImageTk.PhotoImage(resize_img)
    disp_img.config(image=img)
    disp_img.image = img
    disp_img.place(x=150, y=80)

btn_check = Button(ws, text="Open", command=open_file, bg='#FF33FF')
btn_check.place(x=210, y=20)

frame = Frame(ws)
frame.place(x=300, y=20)

Label(frame, text='Width').pack(side=LEFT)
width = Entry(frame, width=10)
width.insert(END, 300)
width.pack(side=LEFT)

Label(frame, text='Height').pack(side=LEFT)

height = Entry(frame, width=10)
height.insert(END, 200)
height.pack(side=LEFT)

resize_btn = Button(frame, text='Resize', command=resize_func, bg='#FF33FF')
resize_btn.pack(side=LEFT)

ws.mainloop()
