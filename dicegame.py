from tkinter import *
from tkinter import messagebox as box

def auth():
    global username
    global password
    global master
    username = username.get()
    password = password.get()
    master.destroy()
    found = False
    loginsfile = open('data/logins.csv')
    for each line in loginsfile:
        data = line.split(',')
        if username = data[0] and password = data[1]:
            userinfo = [data[0],data[2]]
            box.showinfo('Logged In','You have now been logged into: ' + userinfo[0])
def login():
    global username
    global password
    global master
    master = Tk()
    Label(master, text="Username:").grid(row=0, padx = 8, pady = 1)
    Label(master, text="Password:").grid(row=1, padx = 8, pady = 1)
    master.title('Login')
    username = tkinter.Entry(master)

    username.grid(row=0, column=1)

    password = tkinter.Entry(master,show='*')

    password.grid(row=1, column=1)

    tkinter.Button(master, text='login', command=auth).grid(row=3, column=2, sticky=tkinter.W, pady=1,padx =  8)
    master.mainloop( )

def lockallforreset():
    global listbox
    global optpick
    global slogan
    global button
    optpick.config(text='Resetting...', state=DISABLED)
    slogan.config(text='',state=DISABLED)
    button.config(text='',state=DISABLED)
    return True
def recoverall():
    optpick.config(text='Select', state=NORMAL)
    slogan.config(text='Play!',state=NORMAL)
    button.config(text='Quit!',state=NORMAL)
    return True
def filewipe():
    gamefiles = ['data/logins.csv','data/scores.csv']
    fnum = len(gamefiles)
    fnum = fnum -1
    count = 0
    x = True
    while x == True:
        if count > fnum:
            x = False
        else:
            file = open(gamefiles[count], mode='w+')
            file.write('')
            file.close()
            listbox.after(15)
            print('Cleared: ' + str(gamefiles[count]))
            count = count + 1
    print('Rebooting...')
    box.showinfo('Status', 'Game Files Reset')
    return True
def appmanage():
    global listbox
    global optpick
    global slogan
    global button
    locked = False
    wiped = False
    recovered = False
    try:
        option = listbox.get(listbox.curselection())
    except TclError:
        box.showerror('No Input', 'Please select an option.')
        return
    print(option)
    if str(option) == 'Reset':
        user = login()
        if user[1] = 'admin':
            locked = listbox.after(10,lockallforreset)
            while locked == False:
                print('')
            wiped = listbox.after(2500,filewipe)
            while wiped == False:
                print('')
            recovered = listbox.after(2600,recoverall)
            while recovered == False:
                print('')
            return
    elif str(option) == 'Add Accounts':
        box.showinfo('Instructions', "Open logins.csv in the data folder and add a newline in the format 'username,password,'.")

    else:
        box.showinfo('ERR1', 'This function is not available')
        
def menu():
    global listbox
    global optpick
    menus = Tk()
    listbox = Listbox(menus)
    listbox.pack(side=LEFT)

    for item in ["Start Game", "View Leaderboard", "Add Accounts", "Reset"]:
        listbox.insert(END,item)
    optpick = Button(menus,text='Select',command=appmanage)
    optpick.pack(side=RIGHT)
    
    menus.mainloop()
while True:
    startup = Tk()
    frame = Frame(startup)
    frame.pack()

    button = Button(frame,text="Quit!",command=quit)
    button.pack(side=LEFT, padx=5, pady=2)
    slogan = Button(frame,text="Play!",command=menu)
    slogan.pack(side=RIGHT, padx=5, pady=2)
    startup.minsize(100,25)
    startup.mainloop()
