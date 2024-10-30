import tkinter as tk

root = tk.Tk()
res3=[]
root.title("Gugu")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 900
window_height = 550
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2 )

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#Functions

def sum():
    res1 = (int(entry1.get())+int(entry2.get())+int(entry3.get())+int(entry4.get()))
    Label1.config(text=res1)

def multi():
    
    res2 = (int(entry1.get())*int(entry2.get())*int(entry3.get())*int(entry4.get()))
    Label1.config(text=res2)

def min():
    x1=int(entry1.get())
    x2=int(entry2.get())
    x3=int(entry3.get())
    x4=int(entry4.get())
    allName = [x1,x2,x3,x4]
    res=1000000000000000000
    for i in allName:
        if i<res:
            res = i
    Label1.config(text=res)

def maxi():
    res2 = [int(entry1.get()),int(entry2.get()),int(entry3.get()),int(entry4.get())]
    res3 = res2
    maxb = max(res3)
    Label1.config (text=maxb)

Button1 = tk.Button (root, text = "Sum", command = sum)
Button1.place( x = 120, y = 200)

Button2 = tk.Button (root, text = "Multi", command = multi)
Button2.place( x = 120, y = 250)

Button3 = tk.Button (root, text = "Max", command = maxi)
Button3.place( x = 120, y = 300)

Button4 = tk.Button (root, text = "Min", command = min)
Button4.place( x = 120, y = 350)

entry1 = tk.Entry (root)
entry1.place ( x = 180, y = 200)

entry2 = tk.Entry (root)
entry2.place ( x = 180, y = 250)

entry3 = tk.Entry (root)
entry3.place ( x = 180, y = 300)

entry4 = tk.Entry (root)
entry4.place ( x = 180, y = 350)

Label1 = tk.Label (root)
Label1.place ( x = 450 ,  y = 5)

root.mainloop()