import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):

        self.root =tk.Tk()

    ## Title
        self.root.title("Discord Status Changer")
    ## window size
        self.root.geometry("500x500")
    ## icon
        self.root.iconbitmap('images/logo/logo.ico')
#### Creating a Menu
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

        #printing on window
        self.label = tk.Label(self.root, text="Hello World", font=('Arial',31))
        self.label.pack(padx=10,pady=31)

        #adding a text box
        self.textbox = tk.Text(self.root,height=5,font=('Arial', 15))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=20)

        #check button control
        self.check_state= tk.IntVar()

        #adding check box
        self.check = tk.Checkbutton(self.root, text='complated', font=('Arial',10), variable=self.check_state)
        self.check.pack(padx=10)

        #adding a button
        self.button = tk.Button(self.root, text="Mesaji goster -_*", font=('Arial', 15), command=self.show_message)
        self.button.pack(pady=10, padx=5)

        #clear button
        self.clearbtn = tk.Button(self.root, text="Clear the Textbox", font=('Arial', 15), command=self.clear)
        self.clearbtn.pack(pady=10, padx=5)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        #start window
        self.root.mainloop()

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