from tkinter import *

window = Tk()
window.title("Interface PIC")

max_lbl1 = Label(window, text="Nombre max actuel : ")
max_lbl1.grid(column=0, row=0)
max_lbl2 = Label(window, text="3")
max_lbl2.grid(column=1, row=0)

lbl_max = Label(window, text="Nombre maximum de personnes")
lbl_max.grid(column=0, row=1)

max_ppl = Entry(window, width=5)
max_ppl.grid(column=1, row=1)


def set_max_number():
    entry = str(max_ppl.get())
    max_lbl2.configure(text=entry)
    # ajouter partie pyserial


btn = Button(window, text="Valider", command=set_max_number)
btn.grid(column=2, row=1)

lbl_atm1 = Label(window, text="Nombre actuel de personnes :")
lbl_atm1.grid(column=0, row=3)

lbl_atm2 = Label(window, text="0")
lbl_atm2.grid(column=1, row=3)


def add_people():
    people = int(lbl_atm2['text'])
    people += 1
    lbl_atm2.configure(text=str(people))
    #ajouter partie pyserial


def rem_people():
    people = int(lbl_atm2['text'])
    people -= 1
    lbl_atm2.configure(text=str(people))
    # ajouter partie pyserial

#boutons de tests en attendant la partie pyserial
btn_test_add = Button(window, text="test +1", command=add_people)
btn_test_add.grid(column=0, row=4)

btn_test_add = Button(window, text="test -1", command=rem_people)
btn_test_add.grid(column=1, row=4)

window.mainloop()
