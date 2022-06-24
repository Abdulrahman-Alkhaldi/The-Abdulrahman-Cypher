#abdulrahman alkhaldi 
# 2191114843
from tkinter import *
import tkinter.messagebox as messagebox
from Cypher import *

class Cyberistic():
    def __init__(self):
        self.window = Tk()
        self.radio_var = IntVar()

        #size of the window
        self.window.minsize(350, 250)
        self.window.title('The abdulrahman Cypher :D')
        
        #Frames
        self.margin = Frame(self.window)
        self.Top = Frame(self.window)
        self.middle = Frame(self.window)
        self.under_middle = Frame(self.window)
        self.Bottom = Frame(self.window)

        self.margin.pack(side = 'top')
        self.Top.pack()
        self.middle.pack()
        self.under_middle.pack()
        self.Bottom.pack()

        #for space
        self.empty = Label(self.margin,text = '')
        self.empty.pack()

        
        self.title = Label(self.Top, text ='Do you want to Encrypt or Decrypt your text?')
        self.title.pack()

        self.RadioButton1 = Radiobutton(self.middle, text = 'Encrypt', variable = self.radio_var, value = 1) 
        self.RadioButton1.pack() 

        self.RadioButton2 = Radiobutton(self.middle, text ='Decrypt', variable = self.radio_var, value = 2)
        self.RadioButton2.pack()
        

        self.Entry_label = Label(self.under_middle, text = 'Enter Text ')
        self.Entry_label.pack(side = 'left')

        self.Entry = Entry(self.under_middle, width = 15)
        self.Entry.pack(side = 'left')

        self.button = Button(self.Bottom,text = 'Ok', width = 10, command = self.Okbutton)
        self.button.pack(side = 'left')

        self.exit = Button(self.Bottom,text = 'Quit', width = 10, command = self.window.quit)
        self.exit.pack(side = 'right')

        mainloop()

    def Okbutton(self):
        if self.radio_var.get() == 1:
            messagebox.showinfo('Encryption',f'Encrypted text is {encrypt(self.Entry.get())} ')
        elif self.radio_var.get() == 2:
            messagebox.showinfo('Decryption', f'Decrypted text is {decrypt(self.Entry.get())}')

Cyberistic()