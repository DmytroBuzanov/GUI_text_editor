import tkinter
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile, askopenfile


FILE_NAME = tkinter.NONE

def new_file():
	global FILE_NAME
	FILE_NAME = "Untitled"
	text.delete('1.0', tkinter.END)
	
#def insert_text():
#    try:
#        file_name=fd.askopenfilename()
#        f=open(file_name)
#        s=f.read()
#        text.insert(1.0,s)
#        f.close()
#    except FileNotFoundError:
#        mb.showinfo("Увага", "Файл не завантажено")

def open_file():    
        global FILE_NAME
        inp = askopenfile(mode="r")
        if inp is None:
            return
        FILE_NAME = inp.name
        data = inp.read()
        text.delete('1.0', tkinter.END)
        text.insert('1.0', data)
         
def extract_text():
    try:
        file_name=fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                              ("HTML files", "*.html; *.htm"),
                                              ("All files", "*.*")))
        f=open(file_name, 'w')
        s=text.get(1.0, END)
        f.write(s)
        f.close()
    except FileNotFoundError:
        mb.showinfo("Увага", "Файл не збережено")
 
def delete_text():
    answer=mb.askyesno("Підтвердження", message="Ви хочете видалити текст?")
    if answer==True:
        text.delete(0.0, END)

def info():
	mb.showinfo("Information", "GUI for Lab_7 by D_Buzanov")


def clearText():
    m=mb.askyesno(message="Ви впевнені?")
    if m==True:
      text.delete(1.0, END)
      
def menu_clear(event):
    menu2.delete(0)
    menu2.add_command(label='Clear',command=clearText)
    menu2.post(event.x_root, event.y_root)
    text.bind('<Button-1>', lambda event:menu2.delete(0)) 
              
root=Tk()
#text=Text(width=50, height=25)
#text.grid(columnspan=2)

root.title("Text Editor for Lab 7")

root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)

text = tkinter.Text(root, width=400, height=400, wrap="word")
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)
text.pack()

#Button(text="Відкрити", command=insert_text).grid(row=1,sticky=E)
#Button(text="Зберегти", command=extract_text).grid(row=1,column=1,sticky=W)
#Button(text="Очистити", command=delete_text).grid(row=1,column=1)


#root = Tk()
 
#mainmenu = Menu(root) 
#root.config(menu=mainmenu)



#mainmenu = Menu(root)
#root.config(menu=mainmenu)
#menu2=Menu(root, tearoff=0)              
#menu2.add_command(label='Clear',command=clearText)


#root = Tk()
 
mainmenu = Menu(root) 
root.config(menu=mainmenu)
menu2=Menu(root, tearoff=0)
menu2.add_command(label='Очистити',command=clearText)
text.bind('<Button-3>',menu_clear )

 
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Новий", comman = new_file)
filemenu.add_command(label="Відкрити...", command=open_file)
filemenu.add_command(label="Зберегти...", command=extract_text)
filemenu.add_command(label="Очистити все", command=delete_text)
filemenu.add_command(label="Вихід", command=root.quit)
 
helpmenu = Menu(mainmenu, tearoff=0)
#helpmenu.add_command(label="Допомога")
helpmenu.add_command(label="Довідка про розробника", command=info)
 
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Інформація", menu=helpmenu)

root.mainloop()
