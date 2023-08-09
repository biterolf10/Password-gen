from tkinter import *
import random as rnd

root = Tk()

root.title("Password Gen")
root.geometry("400x200")
root.resizable(False, False)

char_sets = {
    "all" : "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
    "cnn" : "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
    "cns" : "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#&'*+-/:;<=>?\"",
    "snn" : "1234567890!@#&'*+-/:;<=>?\""
}

def create_window():
    def gen_passwd(length, pwd):
        password = ""

        for _ in range(length):
            password += char_sets[pwd][rnd.randrange(0, len(char_sets[pwd]))]

        generated_passwd.delete(0, END)
        generated_passwd.insert(0, password)

    main_frame = Frame(root, bg="#f5f5f5")
    main_frame.place(relwidth=1, relheight=1)

    title_lable = Label(main_frame, text="Password Gen")
    title_lable.pack()

    generated_passwd = Entry(main_frame, bg="white", justify="center")
    generated_passwd.pack()

    length = Entry(main_frame, bg="white", justify="center")
    length.insert(0, "Password length")
    length.pack()

    gen_pass_all = Button(main_frame, bg="white", text="Generate password with all letters", command=lambda: gen_passwd(int(length.get()), "all"))
    gen_pass_all.pack(pady=4)

    gen_pass_cnn = Button(main_frame, bg="white", text="Generate password with chars and numbers", command=lambda: gen_passwd(int(length.get()), "cnn"))
    gen_pass_cnn.pack(pady=4)

    gen_pass_cns = Button(main_frame, bg="white", text="Generate password with chars and symbols", command=lambda: gen_passwd(int(length.get()), "cns"))
    gen_pass_cns.pack(pady=4)

    gen_pass_snn = Button(main_frame, bg="white", text="Generate password with symbols and numbers", command=lambda: gen_passwd(int(length.get()), "snn"))
    gen_pass_snn.pack(pady=4)

    root.mainloop()

def main():
    create_window()

if __name__ == '__main__':
    main()
