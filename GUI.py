from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# creating tkinter window 
root = Tk() 
root.geometry('220x230+500+100') 

#dropdown menu
Options=["McDonald's", 'Burger King']

restaurant = StringVar(root)
restaurant.set(Options[0])#default option

#logo
photo = PhotoImage(file = r'C:\Users\ducta\Documents\VandyHacks\Automatic_Survey_scraper\logo_cropped1.png')

logolabel = Label(root,image=photo).pack(side= TOP, pady = 0)

r=OptionMenu(root,restaurant,*Options)
r.pack(side = TOP, pady = (1,2))

def click_here_info():
    messagebox.showinfo('hey','xin chao!')


def open_image():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    pathlabel.config(text=filename)



pathlabel= Label(root, width = 20)
pathlabel.pack(side = TOP, pady = 5)



button2 = Button(root, text = 'Receipt', command= open_image).pack(side = TOP, pady = 5) 
button = Button(root, text = 'Start', command= click_here_info).pack(side = TOP, pady = (5,10)) 

#menu bar
menubar = Menu (root)
#file
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Open File", command=NONE)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu = filemenu)
#display the menu
root.config(menu=menubar)


mainloop() 
