from tkinter import *

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Website Blocker")

Label(root, text='WEBSITE BLOCKER', font='arial 20 bold').pack()
Label(root, text='Subhayu', font='arial 20 bold').pack(side=BOTTOM)

host_path = 'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'
Label(root, text='Enter Website :', font='arial 13 bold').place(x=5, y=60)
Websites = Text(root, font='arial 10', height='2', width='40', wrap=WORD, padx=5, pady=5)
Websites.place(x=140, y=60)

root.mainloop()