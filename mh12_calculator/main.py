from tkinter import *

def display_config():
    display_text.set('mhr')



if __name__ == "__main__":
    
    root = Tk()
    root.title("mhr_calculator")
    

    display_frame = Frame(root)
    display_frame.grid()

    display_text = StringVar()
    display_lbl = Label(display_frame, textvariable=display_text, height=1, width=20, relief='sunken',
                        borderwidth=10, bg='#D8D2C2', font=('FreeSerif', 50))
    display_lbl.pack()
####todo
    btn1 = Button(root, text='1', command=display_config)
    btn1.grid(row=1, column=0)



    root.mainloop()