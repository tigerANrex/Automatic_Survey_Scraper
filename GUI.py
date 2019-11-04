from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

# creating tkinter window 
root = Tk() 
root.geometry('220x220+500+100') 
#overall frame
overall_frame=Frame(root,borderwidth=2,relief='ridge')
overall_frame.pack(side=TOP)
#dropdown menu
Options=["McDonald's", 'Burger King']

restaurant = StringVar(root)
restaurant.set(Options[0])#default option

#logo
photo = PhotoImage(file = r'C:\Users\ducta\Documents\VandyHacks\Automatic_Survey_scraper\logo_cropped1.png')
logolabel = Label(overall_frame,image=photo).pack(side= TOP, pady = (10,2))



#frame for pathlabel and browse button
centerframe = Frame(overall_frame)
centerframe.pack(side = TOP, padx = 5)

def click_here_info():
    messagebox.showinfo('hey','xin chao!')


def open_image():
    filepath =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    filename = os.path.basename(filepath)
    pathlabel.config(text=filename)


button2 = Button(centerframe, text = 'Browse', command= open_image, height=1).pack(side = RIGHT, padx=3) 
pathlabel= Label(centerframe, text="Click 'Browse' to find file",width = 20, pady = 3, fg='gray')
pathlabel.config( borderwidth=2,relief='ridge', bg="white", font=("",8,'italic'))
pathlabel.pack(side = RIGHT,)


#frame
buttomframe = Frame(overall_frame, pady=30)
buttomframe.pack(side=TOP)

button = Button(buttomframe, text = 'Start', command= click_here_info).pack(side = RIGHT) 
#dropdown
r=OptionMenu(buttomframe,restaurant,*Options)
r.pack(side = RIGHT)


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
