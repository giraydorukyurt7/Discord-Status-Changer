import tkinter as tk

#create window
root = tk.Tk()
root.title("Discord Status Changer")

#window size
root.geometry("500x500")

#printing on window
label = tk.Label(root, text="Hello World", font=('Arial',31))
label.pack(padx=10,pady=31)

#adding a text box
textbox = tk.Text(root,height=1,font=('Arial', 15))
textbox.pack(padx=20)

#adding an entry box
myentry = tk.Entry(root)
myentry.pack(pady=10)

#adding a button
button = tk.Button(root, text="tıkla banaa -_*", font=('Arial', 15))
button.pack(pady=10)

#adding grid of buttons
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial',10))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonframe, text="2", font=('Arial',10))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text="3", font=('Arial',10))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btn4 = tk.Button(buttonframe, text="4", font=('Arial',10))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
btn5 = tk.Button(buttonframe, text="5", font=('Arial',10))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
btn6 = tk.Button(buttonframe, text="6", font=('Arial',10))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
btn7 = tk.Button(buttonframe, text="7", font=('Arial',10))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)
btn8 = tk.Button(buttonframe, text="8", font=('Arial',10))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)
btn9 = tk.Button(buttonframe, text="9", font=('Arial',10))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)
btn0 = tk.Button(buttonframe, text="0", font=('Arial',10))
btn0.grid(row=3, column=1, sticky=tk.W+tk.E)
buttonframe.pack(fill='x')

#start window
root.mainloop()


# #create window
# root = tk.Tk()
# root.title("Discord Status Changer")

# #window size
# root.geometry("500x500")

# #adding an entry box
# myentry = tk.Entry(root)
# myentry.pack(pady=10)


        # #adding a text box
        # self.textbox = tk.Text(self.root,height=5,font=('Arial', 15))
        # self.textbox.bind("<KeyPress>", self.shortcut)
        # self.textbox.pack(padx=20)

        # #check button control
        # self.check_state= tk.IntVar()

        # #adding check box
        # self.check = tk.Checkbutton(self.root, text='complated', font=('Arial',10), variable=self.check_state)
        # self.check.pack(padx=10)


        # #adding a button
        # self.button = tk.Button(self.root, text="Mesaji goster -_*", font=('Arial', 15), command=self.show_message)
        # self.button.pack(pady=10, padx=5)

        # #clear button
        # self.clearbtn = tk.Button(self.root, text="Clear the Textbox", font=('Arial', 15), command=self.clear)
        # self.clearbtn.pack(pady=10, padx=5)
        # 