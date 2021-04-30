from tkinter import *

def oi():
    print("oi")

main = Tk()
main.geometry("1000x700")

frame1 = Frame(main)
frame2 = Frame(main)

lbl = Label(frame1,text="Test label",justify=LEFT)
lbl.pack(side=LEFT)

but = Button(frame2,text="Button",command=oi)
but.pack()

frame1.pack(padx=1,pady=1)
frame2.pack(padx=10,pady=10)




main.mainloop()