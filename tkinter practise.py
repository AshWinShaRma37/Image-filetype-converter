from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd 
from PIL import Image
from pkgutil import *
# writing code needs to
# create the main window of
# the application creating
# main window object named root
root = Tk()

# giving title to the main window
root.title("File Converter")

# Open window having dimension 100x100
root.geometry('400x400')

#defining withdrawing files command
def withdraw():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    a= fd.askopenfilename()
    global filename
    filename = a
    print(filename)
   
#defiining function for conversion
def converter():
         Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
         folder_selected = fd.askdirectory()
         print(folder_selected)
         im = Image.open(filename).convert("RGB")
         f = ff.get("1.0", "end-1c")
         final = folder_selected + "/"+ f
         im.save(final)

# show on the window
button1 = Button(root, text ="Select file" , command = withdraw).place(x=130, y=20)
label = Label(root, text ="Save as with file name").place(x=30, y=70)
ff = Text(root, height = 1, width = 20)
ff.place(x=200, y=70)
button2 = Button(root, text ="Convert" , command = converter).place(x=130, y=100)   

# calling mainloop method which is used
# when your application is ready to run
# and it tells the code to keep displaying
root.mainloop()
