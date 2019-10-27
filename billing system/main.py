from tkinter import *
from data import *
from tkinter import ttk
from datetime import datetime


selected_items = []


def resetf():
    global selected_items
    selected_items.clear()


def get_bill(username):
    cost = 0
    for i in selected_items:
        cost = cost + i[2]
    tax = round(cost * 0.2, 2)
    service = round(cost/99, 2)
    total_cost = cost+tax+service
    t = Toplevel()
    t.geometry("350x200")
    t.title("BILL")
    t.configure(bg="#212121")
    date = Label(t, text="DATE: "+datetime.now().strftime("%d-%m-%Y"), fg="white", bg="#212121")
    time = Label(t, text="TIME: "+datetime.now().strftime("%H:%M"), fg="white", bg="#212121")
    emp = Label(t, text="EMPLOYEE ID: "+str(username), fg="white", bg="#212121")
    costl = Label(t, text="COST: "+str(cost), fg="white", bg="#212121")
    taxl = Label(t, text="TAX: "+str(tax), fg="white", bg="#212121")
    servicel = Label(t, text="SERVICE CHARGES: "+str(service), fg="white", bg="#212121")
    total_costl = Label(t, text="TOTAL COST: "+str(total_cost), fg="white", bg="#212121")
    reset = Button(t, text="RESET", command= lambda: resetf(), fg="white", bg="#212121")
    date.pack()
    time.pack()
    emp.pack()
    costl.pack()
    taxl.pack()
    servicel.pack()
    total_costl.pack()
    reset.pack()
    return t


def add_item(item, itemno):
    cost = get_cost(item)
    selected_items.append((item, itemno, cost))
    return


def two(tree):
    tree.delete(*tree.get_children())
    for row in selected_items:
        tree.insert("", 0, text=row[0], values=(row[1], row[2]))


def show_items(tab_main, username):
    t = Frame(tab_main, background="#212121")
    tree = ttk.Treeview(t)
    b = Button(t, text="REFRESH", command=lambda: two(tree), fg="white", bg="#212121")
    b2 = Button(t, text="SUBMIT", command=lambda: get_bill(username), fg="white", bg="#212121")
    reset = Button(t, text="RESET", command= lambda: resetf(), fg="white", bg="#212121")
    tree["columns"] = ("one", "two")
    tree.heading("#0", text="NAME")
    tree.heading("one", text="NO")
    tree.heading("two", text="COST")
    tree.column("#0", anchor=CENTER)  
    tree.column("one", anchor=CENTER)  
    tree.column("two", anchor=CENTER)  
    b.pack()
    b2.pack()
    reset.pack()
    tree.pack()
    return t


def bill(tab_main, username):
    t = Frame(tab_main, background="#212121")
    rows = get_items()
    options = []
    for i in rows:
        options.append(i[1])
    clicked = StringVar()
    clicked.set(options[0])
    cl = IntVar()
    cl.set(1)
    drop = OptionMenu(t, clicked, *options)
    l = Label(t, text="SELECT QUANTITY:", fg="white", bg="#212121")
    q = OptionMenu(t, cl, 1,2,3,4,5,6,7,8,9)
    b = Button(t, text="ADD", command= lambda: add_item(clicked.get(), cl.get()), fg="white", bg="#212121")
    reset = Button(t, text="RESET", command= lambda: resetf(), fg="white", bg="#212121")
    drop.pack()
    l.pack()
    q.pack()
    b.pack()
    reset.pack()
    return t


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
    ud.geometry("600x500")
    ud.title("USER DASH")
    ud.configure(bg="#212121")
    tab_main = ttk.Notebook(ud)
    t1 = user_details(tab_main, username)
    t2 = bill(tab_main, username)
    t3 = show_items(tab_main, username)
    tab_main.add(t1, text="USER DETAILS")
    tab_main.add(t2, text="BILLING")
    tab_main.add(t3, text="VIEW BILL")
    tab_main.pack(expand=1, fill='both')


def ad(username):
    ad = Toplevel()
    ad.geometry("500x700")
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
    ul.geometry("400x400")
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
    al.geometry("500x600")
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
root.geometry("200x200")
root.title("Restaurant Billing System")
root.configure(bg="#212121")
adminB = Button(root, text="ADMIN", fg="white", bg="#212121", padx=16, 
pady=8, bd=5, width=10, anchor="center", command= admin_login)
userB = Button(root, text="USER", fg="white", bg="#212121", padx=16, 
pady=8, bd=5, width=10, anchor="center", command= user_login)
adminB.pack()
userB.pack()
root.mainloop()