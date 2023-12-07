import tkinter as Tk
from tkinter import *

root = Tk()
root.title("To-Do List")
root.geometry("400x650")
root.resizable(False,False)

task_list= []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        taskbox.insert(END, task)

def deleteTask():
    global task_list
    task= str(taskbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        taskbox.delete(ANCHOR)

def openTaskFile():
    
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                taskbox.insert(END, task)
    except:
        file=open('tasklist.txt', 'w')
        file.close()


#Window Icon
Image_icon = PhotoImage(file = r'Icons/task.png')
root.iconphoto(False,Image_icon)

#Top Bar
TopImage = PhotoImage(file = r'Icons/topbar.png')
Label(root, image = TopImage).pack()

#dock image
dockImage = PhotoImage(file = r'Icons\dock.png')
Label(root,image = dockImage, bg="#32405b").place(x = 30, y = 25)

noteImage = PhotoImage(file = r'Icons/task.png')
Label(root,
      image=noteImage,
      bg = "#32405b").place(x=340,y=25)

#heading 
heading = Label(root,
                text = "ALL TASKS",
                font = "Arial 20 bold",
                fg = "white",
                bg = "#32405b")
heading.place(x = 130, y = 20)

#main
frame = Frame(root,
              width=400,
              height=50,
              bg="white")
frame.place(x=0,y=180)

#tasks
task = StringVar()
task_entry = Entry(frame,
                   width=18,
                   font="arial 20",
                   bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

#button
button = Button(frame,
                text="ADD",
                font="Arial 20 bold",
                width=6,bg="#5a95ff",
                fg="#fff",
                bd=0,
                command=addTask)
button.place(x=300,y=0)

#taskbox
task_frame= Frame(root, bd=3, width=700,height=280,bg="#32405b")
task_frame.pack(pady=(160,0))

taskbox= Listbox(task_frame,
                 font=("arial",12),
                 width=40,height=16,
                 bg="#32405b",fg="white",
                 cursor="hand2",
                 selectbackground="#5a95ff")
taskbox.pack(side=LEFT, fill=BOTH,padx=2)
scrollbar= Scrollbar(task_frame)
scrollbar.pack(side=LEFT,fill=BOTH)

taskbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=taskbox.yview)

openTaskFile()

#delete
Delete_icon=PhotoImage(file=r'Icons/delete.png')
Button(root,
       image=Delete_icon,
       bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)



root.mainloop()