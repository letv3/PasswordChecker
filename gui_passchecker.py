from checkmypass import pwned_api_check
from tkinter import *


def check():
    password = str(txt.get())
    count = pwned_api_check(password)
    if count:
        return f'{password} was found {count} times, u should change'
    else:
        return f'{password} was Not found'

def phrase_display():
    res = check()

    display_text = Label(master=window, text=res)
    display_text.grid(row=2, column=0)

    # text_res= Text(master=window, height=10, width=30)
    # text_res.grid(row=2, column=0)
    # text_res.insert(END, res)

window = Tk()
window.title("Password Checker")
window.geometry('350x200')

# Label
lbl = Label(text='Enter here password you want to check')
lbl.grid(row=0,column=0)

txt = Entry(width=50)
txt.grid(row=1, column=0)

button = Button(text='check', command=phrase_display)
button.grid(row=1, column=1)


window.mainloop()
