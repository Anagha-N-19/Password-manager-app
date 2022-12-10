from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random

password = ""


def generate_password():
    password_entry.delete(0, 'end')
    # password_entry.insert(0,'')
    global password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    for char in password_list:
        password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def addinfo():
    if website_entry.get() == "" or password_entry.get() == "" or email_entry.get() == '':
        messagebox.showwarning(title=website_entry.get(),
                               message="empty entries")
    else:
        data_ok = messagebox.askokcancel(title=website_entry.get(),
                                         message=f"Details enetered\n Email: {email_entry.get()}\n Password: "
                                                 f"{password_entry.get()}\n Save?")
        if data_ok:
            outfile = open('password_data.txt', 'a')
            outfile.write(f'\n{website_entry.get()} |   {email_entry.get()}   |   {password_entry.get()}')
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40)

canvas = Canvas(width=150, height=150)
tom = PhotoImage(file='lock150.png')
canvas.create_image(75, 75, image=tom)
canvas.grid(row=0, column=1, padx=5, pady=5)

website_name = Label(text="Website")
website_name.grid(column=0, row=1, padx=5, pady=5)
website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

email_name = Label(text="Email/Username")
email_name.grid(column=0, row=2, padx=5, pady=5)
email_entry = Entry(width=50)
email_entry.insert(0, 'abcd@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

password_name = Label(text="Password")
password_name.grid(column=0, row=3, padx=5, pady=5)
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, padx=5, pady=5)

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3, padx=5, pady=5)

add_button = Button(text='Add', width=40, command=addinfo)
add_button.grid(column=1, row=4, columnspan=2, padx=5, pady=5)

window.mainloop()
