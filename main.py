import tkinter as tk

def get_data():
    message ="hello world"
    data_display.config(text=message)

#create window
root = tk.Tk()
root.title("Discord Status Changer")

#iu
header = tk.Label(root, text="deneme123")
header.pack()

#button
get_data_button = tk.Button(root, text="User input", command=get_data)
get_data_button.pack()

#display
data_display = tk.Label(root, text="")
data_display.pack()

#window size
root.geometry("500x500")

###################

#user input function
def get_user_input():
    name = entry.get()
    return name

#label question text
labelSoru = tk.Label(root, text="Adını yaz:")
labelSoru.pack()

#user input widget
entry = tk.Entry(root)
entry.pack()

#submit button for user input
submitButton = tk.Button(root, text="Submit", command=get_user_input)
submitButton.pack()

#label print user input
labelPrintUserInput = tk.Label(root, text=get_user_input)
labelPrintUserInput.pack()
#start
root.mainloop()
