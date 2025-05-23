import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    result = "".join(password_list)

    password.insert(0, result)
    pyperclip.copy(result)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website.get()
    pass_word = password.get()
    e_mail = email.get()
    new_file = {web: {'password': pass_word, 'email': e_mail}}
    if len(web) > 0 or len(pass_word) > 0 or len(e_mail) > 0:
        is_ok = messagebox.askokcancel(web, f"email:{e_mail}\n password:{pass_word}\nDo you want to save ?")
        if is_ok:
            try:
                with open('data.jason', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('data.jason', 'w') as file:
                    json.dump(new_file, file)
            else:
                with open('data.jason', 'w') as file:
                    data.update(new_file)
                    json.dump(data, file, indent=4)
            finally:
                email.delete(0, tkinter.END)
                password.delete(0, tkinter.END)
                website.delete(0, tkinter.END)
    else:
        messagebox.showinfo("Error", "Please enter valid email and password")


def find_password():
    web = website.get()
    try:
        with open('data.jason', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No data file found")
    else:
        if web in data:
            a = data[web]['password']
            b = data[web]['email']
            messagebox.showinfo(web, f"email:{b}\n password:{a}")
        else:
            messagebox.showinfo("Error", "Please enter valid website")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("password manager")
window.config(padx=20, pady=20, bg="white")
canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = tkinter.PhotoImage(file="my_pass.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
website_txt = tkinter.Label(text=" website: ", bg="white", fg="black")
website_txt.grid(row=1, column=0)
email_txt = tkinter.Label(text=" email/username: ", bg="white", fg='black')
email_txt.grid(row=2, column=0)
password_txt = tkinter.Label(text=" password: ", bg="white", fg='black')
password_txt.grid(row=3, column=0)
website = tkinter.Entry(width=21, bg="white", highlightthickness=0, fg="black", insertbackground="black")
website.focus()
website.grid(row=1, column=1, )
email = tkinter.Entry(width=35, bg="white", highlightthickness=0, fg="black", insertbackground='black')
email.grid(row=2, column=1, columnspan=2)
password = tkinter.Entry(width=21, bg="white", highlightthickness=0, fg="black", insertbackground='black')
password.grid(row=3, column=1)
generate_pass = tkinter.Button(text='generate password', highlightthickness=0, command=generate_password)
generate_pass.grid(row=3, column=2)
add = tkinter.Button(text='add', width=36, highlightthickness=0, command=save)
add.grid(row=4, column=1, columnspan=2)
search = tkinter.Button(text='search', highlightthickness=0, command=find_password)
search.grid(row=1, column=2)
window.mainloop()
