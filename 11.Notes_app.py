import tkinter as tk
from tkinter import filedialog,messagebox

#main window code
root = tk.Tk()
root.title("My Text Editor")
root.geometry("600x500")

#creating text area
text = tk.Text(
  root,
  wrap= tk.WORD,
  font={"TimeNewRoman",14}
)

text.pack(expand= True,fill=tk.BOTH)

#main logic

#Function 1 - to create new file
def new_file():
  text.delete(1.0,tk.END)

#Function 2 - to open a new file
def open_file():
  #open file dialogue
  file_path = filedialog.askopenfilename(
    defaultextension=".txt",
    filetypes=[("Text Files","*.txt")]
  )

  if file_path:
    #open selected file
    with open(file_path,"r") as file:
      #clear old text
      text.delete(1.0,tk.END)
      text.insert(tk.END,file.read())

#Function 3 - save the file

def save_file():
  #open save file dialogue
  file_path = filedialog.asksaveasfilename(
    defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
  )

  if file_path:
    with open(file_path,"w") as file:
      file.write(text.get(1.0,tk.END))

    messagebox.showinfo("Info","File saved succefully")

#Create Menu bar
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu,tearoff=0)

#New Open File save,exit
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)



#start and keeps the window open
root.mainloop()