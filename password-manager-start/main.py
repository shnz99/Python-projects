from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import json
import pyperclip

FONT_NAME = "Arial", 12, "normal"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    entry_pass.delete(0, END)

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    entry_pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_web.get()
    user = entry_user.get()
    password = entry_pass.get()
    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(user) == 0:
        messagebox.showwarning(
            title="Warning", message="Please don't leave any fields empty!"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {user} \nPassword: {password} \nIs it okay to save?",
        )

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # update old data with newdata
                data.update(new_data)

                with open("data.json", "w") as file:
                    # saving updated data
                    json.dump(data, file, indent=4)
            finally:
                entry_web.delete(0, END)
                entry_pass.delete(0, END)


# -------------------------- FIND PASSWORD ---------------------------- #


def find_password():
    website = entry_web.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            search_key = data.get(website)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data file found!")
    else:
        if search_key:
            messagebox.showinfo(
                title=website,
                message=f"email: {search_key['email']} \npassword:{search_key['password']}",
            )
        else:
            messagebox.showwarning(
                title="Error", message="No details for the website exists."
            )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
my_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_image)
canvas.grid(column=1, row=0)

# Labels ############################################################################
label1 = Label(text="Website:", font=FONT_NAME)
label1.grid(column=0, row=1)
label2 = Label(text="Email/Username:", font=FONT_NAME)
label2.grid(column=0, row=2)
label3 = Label(text="Password:", font=FONT_NAME)
label3.grid(column=0, row=3)
# Entries ###########################################################################
entry_web = Entry(width=33)
entry_web.grid(column=1, row=1, columnspan=1)
entry_web.focus()

entry_user = Entry(width=52)
entry_user.grid(column=1, row=2, columnspan=2)
entry_user.insert(
    0, "d.gawin@pm.me"
)  # END to jest index końcowy, "0" to możę być początkowy

entry_pass = Entry(width=33)
entry_pass.grid(column=1, row=3, columnspan=1)
# Buttons ###########################################################################
btn_search = Button(text="Search", width=14, command=find_password)
btn_search.grid(column=2, row=1)
btn_pass = Button(text="Generate Password", width=14, command=password_generator)
btn_pass.grid(column=2, row=3)
btn_add = Button(text="Add", width=44, command=save)
btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
