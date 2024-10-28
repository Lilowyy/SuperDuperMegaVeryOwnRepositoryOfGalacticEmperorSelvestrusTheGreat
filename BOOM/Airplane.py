import tkinter as tk

from tkinter import PhotoImage

root = tk.Tk()
#Гого
icon = tk.PhotoImage(file="1.png")
root.iconphoto(root, icon)

root.title("Hello app")
# Айм блу дабуди дабудай!!!!!!!!!!!!
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 900
window_height = 550
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2 )

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
# Какие-то там функции (подглядел у Алексея)
def count():
    res666 = (int(entry2.get())+int(entry4.get())+int(entry7.get()))
    entry10.config(text=res666)

    res667 = (int(entry1.get())+int(entry5.get())+int(entry8.get()))
    entry11.config(text=res667)

    res668 = (int(entry3.get())+int(entry6.get())+int(entry9.get()))
    entry12.config(text=res668)



labelГлобГлоб = tk.Label (root, text = "Триатлон")
labelГлобГлоб.place( x = 450, y = 1)

labelГлабГлаб = tk.Label (root, text = "Алексей")
labelГлабГлаб.place( x = 450, y = 100)

labelГлобГлаб = tk.Label (root, text = "Андрей")
labelГлобГлаб.place( x = 250, y = 100)

labelГлабГлоб = tk.Label (root, text = "Акбар")
labelГлабГлоб.place( x = 650, y = 100)

labelГлыбГлуб = tk.Label (root, text = "Скорость")
labelГлыбГлуб.place( x = 150, y = 100)

labelЫ = tk.Label (root, text = "Поедание пицц")
labelЫ.place( x = 120, y = 200)

labelУ = tk.Label (root, text = "Квадробинг")
labelУ.place( x = 120, y = 280)

labelО = tk.Label (root, text = "Спортивная Охота")
labelО.place( x = 100, y = 360)

labelО = tk.Label (root, text = "Общий балл")
labelО.place( x = 120, y = 440)

entry1 = tk.Entry (root)
entry1.place( x = 450, y = 200)

entry2 = tk.Entry (root)
entry2.place( x = 250, y = 200)

entry3 = tk.Entry (root)
entry3.place( x = 650, y = 200)

entry4 = tk.Entry (root)
entry4.place( x = 250, y = 280)

entry5 = tk.Entry (root)
entry5.place( x = 450, y = 280)

entry6 = tk.Entry (root)
entry6.place( x = 650, y = 280)

entry7 = tk.Entry (root)
entry7.place( x = 250, y = 360)

entry8 = tk.Entry (root)
entry8.place( x = 450, y = 360)

entry9 = tk.Entry (root)
entry9.place( x = 650, y = 360)

entry10 = tk.Label (root)
entry10.place( x = 250, y = 440)

entry11 = tk.Label (root)
entry11.place( x = 450, y = 440)

entry12 = tk.Label (root)
entry12.place( x = 650, y = 440)

entry13 = tk.Entry (root)
entry13.place( x = 450, y = 480)

#Кнопки, почти полностью сделал сам

button1 = tk.Button (root, text = "Чемпион")
button1.place( x = 450, y = 520)

button1 = tk.Button (root, text = "Общий результат", command = count)
button1.place( x = 250, y = 520)



#Изображение

image = PhotoImage(file="1.png")
image_bob = tk.Label (root, image = image)
image_bob.place(x=5, y=5)


root.mainloop()