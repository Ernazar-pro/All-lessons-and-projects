import tkinter
from tkinter import ttk
from tkinter import messagebox


class Win(tkinter.Tk):
    def __init__(self, ):
        super().__init_()
        self.title(string='Homework')
        self.geometry(newgeometry='720x480')
        self.resizable(width=False,height=False)
        self.configure(bg='white')


        self.btn1 = ttk.Button(self,text='Info')
        self.btn1['command'] =self.show
        self.btn1.bind('<Return>',self.show)

        self.btn1.pack()

        self.btn2 = ttk.Button(self,text='Exit')
        self.btn2['command'] =self.exit
        self.btn2.bind('<Return>',self.exit)

        self.btn2.pack()

        self.btn3 = ttk.Button(self,text='Open')
        self.btn3['command'] =self.open
        self.btn3.bind('<Return>',self.open)

        self.btn3.pack()

        self.btn4 = ttk.Button(self,text='Save')
        self.btn4['command'] =self.save
        self.btn4.bind('<Return>',self.save)

        self.btn4.pack()
    
        self.btn5 = ttk.Button(self,text='Menu')
        self.btn5['command'] =self.menu
        self.btn5.bind('<Return>',self.menu)

        self.btn5.pack()

        self.btn6 = ttk.Button(self,text='Help')
        self.btn6['command'] =self.help
        self.btn6.bind('<Return>',self.help)

        self.btn6.pack()
        
        self.btn7 = ttk.Button(self,text='Add')
        self.btn7['command'] =self.add
        self.btn7.bind('<Return>',self.add)

        self.btn7.pack()

        self.entry1 = ttk.Entry(self,width=40)
        self.entry1.focus()
        self.entry1.pack()

    

if __name__ == '__main__':
    app = Win()
    app.mainloop()