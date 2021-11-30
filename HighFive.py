from tkinter import *
from tkinter import ttk

def greeting():
    print(f'High five, {username.get()}!')


root = Tk()

root.title('High five')

username = StringVar()

input_frame = ttk.Frame(root, padding=(10, 5, 10, 0))
input_frame.pack(fill='both')


username_label = ttk.Label(input_frame, text='Name: ')
username_label.pack(side='left', padx=(5, 10))

entery = ttk.Entry(input_frame, width=20, textvariable=username)
entery.pack(side='left', padx=(0, 10))
entery.focus()

buttons_frame = ttk.Frame(root, padding=(10,5))
buttons_frame.pack(fill='both', expand=True)

greeting_button = Button(buttons_frame, text='Hello',
                         command=greeting)
greeting_button.pack(side='left', fill='x', expand=True)

cancel_button = ttk.Button(buttons_frame, text='Cancel',
                           command=root.destroy)
cancel_button.pack(side='left', fill='x', expand=True)

root.mainloop()
