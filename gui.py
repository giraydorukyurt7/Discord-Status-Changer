import tkinter as tk
from tkinter import messagebox
import os
import subprocess
class MyGUI:

    def __init__(self):

        self.root =tk.Tk()
    ## Title
        self.root.title("Discord Status Changer")
    ## window size
        self.root.geometry("600x600")
    ## icon
        self.root.iconbitmap('images/logo/logo.ico')
#### Creating a Menu ######################################################
    ## Creating a menubar
        self.menubar = tk.Menu(self.root)
    ## First menu
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="CLOSE", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="CLOSE Without Question", command=exit)
    ## Second menu    
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)
    ## Adding them on menubar   
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")
    ## Config settings for the menubar
        self.root.config(menu=self.menubar)
########################################################################
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        #printing on window
        self.label = tk.Label(self.root, text="Create a file", font=('Arial',31))
        self.label.pack(padx=10,pady=31)

        #file name entry section
        self.fileNameEntry = tk.Entry(self.root)
        self.fileNameEntry.pack(padx=10, pady=10)
        #confirm file name button
        self.confirmFileNamebtn = tk.Button(self.root, text="Confirm File Name", font=('Arial',15), command=self.confirmFileName)
        self.confirmFileNamebtn.pack(padx=10, pady=10)
        #create file button
        self.createFilebtn = tk.Button(self.root, text="Create File", font=('Arial',15), command=self.createFile)
        self.createFilebtn.pack(padx=10,pady=10)
        #create file delete button
        self.deleteFilebtn = tk.Button(self.root, text="Delete File", font=('Arial',15), command=self.deleteFile)
        self.deleteFilebtn.pack(padx=10,pady=10)
        #start window
        self.root.mainloop()
    
    def confirmFileName(self):
        filename = self.fileNameEntry.get() + ".py"
        print(filename)
        self.root.title(self.confirmFileName)
        return filename
    def createFile(self):
        filename = self.confirmFileName()
        file = open(filename,"w")
        with open(filename,'w') as file:
            file.write('print("File has been succesfully created")\n\n')
            file.write('import tkinter as tk\n\n')
            file.write('class TheGui:\n\n')
            file.write('\tdef __init__(self):\n')
            file.write('\t\tself.root = tk.Tk()\n')
            file.write('\t## Title\n')
            file.write('\t\tself.root.title("' + filename + '")\n')
            file.write('\t## Window Size")\n')
            file.write('\t\tself.root.geometry("500x10")\n')
            file.write('\t## Start The Loop\n')
            file.write('\t\tself.root.mainloop()\n')
            file.write('TheGui()')
        subprocess.run(['python', filename])
    
    def deleteFile(self):
        filename = self.confirmFileName()

        if os.path.exists(filename):
            os.remove(filename)    
        else:
            print("the file does not exists")

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
    
    def shortcut(self, event):
        if event.state == 4 and event.keysym == "Return":
            self.show_message()
    
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)

MyGUI()

# import tkinter as tk
# class MyGUI:
#     def __init__(self):
#         self.root =tk.Tk()
#     ## Title
#         self.root.title("Test Succesfull")
#     ## window size
#         self.root.geometry("600x600")
#     ## start the loop
#         self.root.mainloop()