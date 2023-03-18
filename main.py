from password_generator import password_generator
from tkinter import messagebox
import clipboard
from tkinter import *
import json

# CONSTANTS

red = "#E21818"
width = 40
# create screen

screen = Tk()
screen.title("Password Saver")
screen.config(padx=50, pady=50)
screen.resizable(False, False)


# add functionality
def generate_password():
    password_entry.delete(0, END)
    new_password = password_generator()
    password_entry.insert(0, new_password)
    clipboard.copy(new_password)


def save_data():
    website = website_entry.get().title()
    user = email_username_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=f"{website}", message=f"Are you sure you want to save it?\n"
                                                               f"User: {user}\n"
                                                               f"Password: {password}")
    if is_ok:
        list_data = {}
        if len(website) == 0 or len(user) == 0 or len(password) == 0:
            warning_label.config(text="Please complete all the entries.")
        else:
            warning_label.config(text="")
            with open("saved_data.json", "r") as file_open:
                data = json.load(file_open)
                list_data = data
            list_data["Socials"][website] = {"User": f"{user}", "Password": f"{password}"}
            with open("saved_data.json", "w") as file_open:
                json.dump(list_data, file_open, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        email_username_entry.delete(0, END)


def search():
    warning_label.config(text="")
    website = website_entry.get().title()
    with open("saved_data.json", "r") as file_open:
        data = json.load(file_open)
        for key in data["Socials"]:
            if key == website:
                password_entry.delete(0, END)
                password_entry.insert(0, data["Socials"][key]["Password"])
                email_username_entry.delete(0, END)
                email_username_entry.insert(0, data["Socials"][key]["User"])
            else:
                pass


# add widgets
canvas = Canvas(width=200, height=189)
logo_image = PhotoImage(file="../logo.png")
canvas.create_image((100, 95), image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_entry = Entry(width=34)
website_entry.grid(row=1, column=1, sticky=W)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=1, sticky=E)

email_username_label = Label(text="User/Email: ")
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=43)
email_username_entry.grid(row=2, column=1, sticky=W)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1, sticky=W)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=1, sticky=E)

add_button = Button(text="Add", command=save_data, width=width)
add_button.grid(row=4, column=1)

warning_label = Label(text="", fg=red)
warning_label.grid(row=5, column=1)
screen.mainloop()
