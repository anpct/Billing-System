from tkinter import *
from data import *
from tkinter import ttk


def user_details(tab_main, username):
    t = Frame(tab_main, background="#212121")
    data = get_user_details(int(username))
    lname = Label(t, text="NAME: "+data[1], fg="white", bg="#212121")
    lid = Label(t, text="ID: "+str(data[0]), fg="white", bg="#212121")
    lphno = Label(t, text="PHNO: "+str(data[2]), fg="white", bg="#212121")
    lname.pack()
    lid.pack()
    lphno.pack()
    return t


def admin_details(tab_main, username):
    t = Frame(tab_main, background="#212121")
    data = get_admin_details(int(username))
    lname = Label(t, text="NAME: "+data[1], fg="white", bg="#212121")
    lid = Label(t, text="ID: "+str(data[0]), fg="white", bg="#212121")
    lphno = Label(t, text="PHNO: "+str(data[2]), fg="white", bg="#212121")
    lname.pack()
    lid.pack()
    lphno.pack()
    return t


def popup(msg):
    pop = Toplevel()
    pop.geometry("150x60")
    pop.title("ERROR")
    pop.configure(bg="#212121")
    l = Label(pop, text=msg, fg="white", bg="#212121")
    exitb = Button(pop, text="OK", fg="white", bg="#212121", command= lambda: pop.destroy())
    l.pack()
    exitb.pack()


def ud(username):
    ud = Toplevel()
    ud.geometry("350x200")
    ud.title("USER DASH")
    ud.configure(bg="#212121")
    tab_main = ttk.Notebook(ud)
    t1 = user_details(tab_main, username)
    tab_main.add(t1, text="USER DETAILS")
    tab_main.pack(expand=1, fill='both')


def ad(username):
    ad = Toplevel()
    ad.geometry("350x200")
    ad.title("ADMIN DASH")
    ad.configure(bg="#212121")
    tab_main = ttk.Notebook(ad)
    t1 = admin_details(tab_main, username)
    tab_main.add(t1, text="ADMIN DETAILS")
    tab_main.pack(expand=1, fill='both')


def user_auth(username, password):
    if username and password and username.isnumeric():
        if ck_details_emp(int(username), password):
            ud(username)
        else:
            popup("ERROR WRONG DETAILS")
    else:
        popup("ERROR WRONG DETAILS")


def admin_auth(username, password):
    if username and password and username.isnumeric():
        if ck_details_admin(int(username), password):
            ad(username)
        else:
            popup("ERROR WRONG DETAILS")
    else:
        popup("ERROR WRONG DETAILS")


def user_login():
    ul = Toplevel()
    ul.geometry("350x200")
    ul.title("USER LOGIN")
    ul.configure(bg="#212121")
    l1= Label(ul, text="ENTER EID: ", fg="white", bg="#212121")
    e1= Entry(ul)
    l2= Label(ul, text="ENTER PASSWORD: ", fg="white", bg="#212121")
    e2= Entry(ul, show="*")
    sb= Button(ul, text= "LOGIN", fg="white", bg="#212121", command= lambda: user_auth(e1.get(),e2.get()))
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    sb.grid(row=2, column=1)


def admin_login():
    al = Toplevel()
    al.geometry("350x200")
    al.title("ADMIN LOGIN")
    al.configure(bg="#212121")
    l1= Label(al, text="ENTER AID: ", fg="white", bg="#212121")
    e1= Entry(al)
    l2= Label(al, text="ENTER PASSWORD: ", fg="white", bg="#212121")
    e2= Entry(al, show="*")
    sb= Button(al, text= "LOGIN", fg="white", bg="#212121", command= lambda: admin_auth(e1.get(),e2.get()))
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    sb.grid(row=2, column=1)


root = Tk()
root.geometry("350x100")
root.title("Restaurant Billing System")
root.configure(bg="#212121")
adminB = Button(root, text="ADMIN", fg="white", bg="#212121", padx=16, 
pady=8, bd=5, width=10, anchor="center", command= admin_login)
userB = Button(root, text="USER", fg="white", bg="#212121", padx=16, 
pady=8, bd=5, width=10, anchor="center", command= user_login)
adminB.pack()
userB.pack()
root.mainloop()