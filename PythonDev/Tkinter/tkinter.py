import tkinter
import random
from tkinter import ttk
from tkinter import messagebox

color=random.randrange(0,2**24)

hex_color=hex(color)
std_color="#" + hex_color[2:]


class Root(tkinter.Tk):
    def __init__(self, ):
        super().__init__()
        self.title(string='My first application')
        self.geometry(newGeometry='720x480')
        self.resizable(width=False, height=False)
        self.configure(bg=std_color)


        self.entry1 = ttk.Entry(self,width=30)
        self.entry1.focus()
        self.entry1.bind('<Return>',self.next)
        self.entry1.pack()

        self.entry2= ttk.Entry(self,width=30)
        self.entry2.pack()

        self.button = ttk.Button(self,text='Press')
        self.button['command'] = self.show
        self.button.bind('<Return>',self.show)

        self.button.pack()
    
    def show(self,*args):
        result=int(self.entry1.get()) + int(self.entry2.get())
        return messagebox.showinfo(
            title='Info',
            message=f'Summa{result}'
        ), self.entry1.delete(0,tkinter.END), self.entry2.delete(0,tkinter.END),self.entry1.focus()
    
    def next(self,*args):
        self.entry2.focus()

if __name__ == '__main__':
    root=Root()
    root.mainloop()