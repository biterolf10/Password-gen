from tkinter import *
import random as rnd


root = Tk()

def create_window():
    def gen_passwd(lenght, all, cnn, cns, snn):
        def generate_password_all(length):
            password = ""
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#&'*+-/:;<=>?\""

            for i in range(length):
                password += chars[rnd.randrange(0, len(chars))]

            return password

        def generate_password_CnN(length):
            password = ""
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

            for i in range(length):
                password += chars[rnd.randrange(0, len(chars))]

            return password

        def generate_password_CnS(length):
            password = ""
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#&'*+-/:;<=>?\""

            for i in range(length):
                password += chars[rnd.randrange(0, len(chars))]

            return password

        def generate_password_SnN(length):
            password = ""
            chars = "1234567890!@#&'*+-/:;<=>?\""

            for i in range(length):
                password += chars[rnd.randrange(0, len(chars))]

            return password
            
        
        if all == True:
            passwd = generate_password_all(lenght)

        if cnn:
            passwd = generate_password_CnN(lenght)

        if cns:
            passwd = generate_password_CnS(lenght)

        if snn:
            passwd = generate_password_SnN(lenght)

        generated_passwd.delete(0, END)
        generated_passwd.insert(0, passwd)

    canvas = Canvas(root, width=400, height=175)
    canvas.pack()

    main_frame = Frame(root, bg="white")
    main_frame.place(relwidth=1, relheight=1)

    title_lable = Label(main_frame, text="Password Gen")
    title_lable.pack()

    generated_passwd = Entry(main_frame, bg="white",)
    generated_passwd.pack()

    lenght = Entry(main_frame, bg="white")
    lenght.pack()

    gen_pass_all = Button(
        main_frame,
        bg="white",
        text="Generate password with all letters",
        command=lambda: gen_passwd(int(lenght.get()), True, False, False, False),
    )
    gen_pass_all.pack()

    gen_pass_cnn = Button(
        main_frame,
        bg="white",
        text="Generate password with chars and numbers",
        command=lambda: gen_passwd(int(lenght.get()), False, True, False, False),
    )
    gen_pass_cnn.pack()

    gen_pass_cns = Button(
        main_frame,
        bg="white",
        text="Generate password with chars and symbols",
        command=lambda: gen_passwd(int(lenght.get()), False, False, True, False),
    )
    gen_pass_cns.pack()

    gen_pass_snn = Button(
        main_frame,
        bg="white",
        text="Generate password with symbols and numbers",
        command=lambda: gen_passwd(int(lenght.get()), False, False, False, True),
    )
    gen_pass_snn.pack()

    root["bg"] = "white"

    root.title("Password Gen")
    root.geometry("400x175")
    root.resizable(False, False)

    root.mainloop()


def main():
    create_window()

if __name__ == '__main__':
    main()