import tkinter as tk
import sqlite3
from tkinter import messagebox as mb
from datetime import datetime as dt

#relief = flat, groove, raised, ridge, solid, sunken

connection = sqlite3.connect('To_Do_List_db.db')


class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title('To Do List')
        self.root.geometry('515x582')
        self.root.resizable(False, False)
        self.root.config(bg=None)
        self.database()
        self.tasks_id_incomp = []
        self.tasks_id_pend = []
        self.tasks_id_comp = []
        
        self.setup_ui()
        self.load_tasks()

    def database(self):
        conn = sqlite3.connect('To_Do_List_db.db')
        query = '''CREATE TABLE IF NOT EXISTS Tasks (Task_Name VARCHAR,
                    Task_Status VARCHAR,
                    Date DATE,
                    Time VARCHAR)'''
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()

    def setup_ui(self):

        self.label_topic = tk.Label(self.root,text = 'To Do List',width = 22,font = ('ariel',12,'bold'),padx = 5,pady = 5,relief = 'ridge')
        self.label_topic.place(x = 5,y = 5)

        #frame_createbt and its widgets
        self.frame_createbt = tk.LabelFrame(self.root,text = 'Create New task',font = ('ariel',12),padx = 5,pady = 3,relief = 'groove')
        self.frame_createbt.place(x = 5,y = 50)

        self.enter_task = tk.Entry(self.frame_createbt,font = ('ariel',12),width = 24)
        self.enter_task.grid(row = 1,column = 0,pady = 5)
        
        self.bt_create = tk.Button(self.frame_createbt,text = 'Create',padx = 10,pady = 5,command=self.create_task)
        self.bt_create.grid(row = 2,column = 0,pady = 5)
        
        #frame_list_incomp and its widgets
        self.frame_list_incomp = tk.LabelFrame(self.root,text ='Incomplete Tasks',font = ('ariel',12),padx = 5,pady = 5,relief = 'groove')
        self.frame_list_incomp.place(x = 250,y = 5)

        self.scrollyincomp = tk.Scrollbar(self.frame_list_incomp)
        self.scrollyincomp.pack(side = 'right',fill = 'both')
        
        self.listbox_incomplete = tk.Listbox(self.frame_list_incomp,height = 8,width = 25,font = ('ariel',12),
                                             yscrollcommand = self.scrollyincomp.set)
        self.listbox_incomplete.pack()

        self.scrollyincomp.config(command = self.listbox_incomplete.yview)

        #frame_pend and its widgets
        self.frame_list_pend = tk.LabelFrame(self.root,text = 'Pending Tasks',font = ('ariel',12),padx = 5,pady = 5,relief = 'groove')
        self.frame_list_pend.place(x = 250,y = 200)

        self.scrollypend = tk.Scrollbar(self.frame_list_pend)
        self.scrollypend.pack(side = 'right',fill = 'both')
        
        self.listbox_pending = tk.Listbox(self.frame_list_pend,height = 8,width = 25,font = ('ariel',12),
                                          yscrollcommand=self.scrollypend.set)
        self.listbox_pending.pack()

        self.scrollypend.config(command = self.listbox_pending.yview)
        
        #frame_list_comp and its widgets
        self.frame_list_comp = tk.LabelFrame(self.root,text = 'Completed Tasks',font = ('ariel',12),padx = 6,pady = 5,relief = 'groove')
        self.frame_list_comp.place(x = 5,y = 390)#x = 113

        self.scrollycomp = tk.Scrollbar(self.frame_list_comp)
        self.scrollycomp.pack(side = 'right',fill = 'both')
        
        self.listbox_completed = tk.Listbox(self.frame_list_comp,height = 8,width = 52,font = ('ariel',12),
                                            yscrollcommand = self.scrollycomp.set)
        self.listbox_completed.pack()

        self.scrollycomp.config(command = self.listbox_completed.yview)
        
        #frame_updatebt and its widgets
        self.frame_updatebt = tk.LabelFrame(self.root,text = 'Update Task Status',relief = 'groove',font = ('ariel',12),padx = 5,pady = 5)
        self.frame_updatebt.place(x = 5,y = 170)

        self.update_task = tk.Entry(self.frame_updatebt,font = ('ariel',12),width = 24)
        self.update_task.grid(row = 0, column = 0,pady = 5)

        self.status_button = tk.Button(self.frame_updatebt,text = 'Update',padx = 10,pady = 5,command = self.update_status)
        self.status_button.grid(row =1,column = 0)

        #frame_deletebt and its widgets
        self.frame_deletebt = tk.LabelFrame(self.root,text = 'Delete tasks',padx = 33,pady = 5,relief = 'groove',font = ('ariel',13))
        self.frame_deletebt.place(x = 5,y = 277)

        self.label = tk.Label(self.frame_deletebt,text = 'Select a Task to delete',font = ('ariel',12))
        self.label.grid(row = 0, column = 0,pady = 5)
        
        self.bt_delete = tk.Button(self.frame_deletebt,text = 'Delete task',command=self.delete_tasks,padx = 20,pady = 5)
        self.bt_delete.grid(row = 1, column = 0,pady = 5)
        
    def create_task(self):
        taskname = self.enter_task.get()
        taskstatus = 'Incomplete'
        if taskname != "":
            now = dt.now()
            current_date = now.strftime("%Y-%b-%d")
            
            conn = sqlite3.connect('To_Do_List_db.db')
            cur = conn.cursor()
            cur.execute('''INSERT INTO Tasks (Task_Name, Task_Status, Date) 
                           VALUES (?, ?, ?)''', (taskname, taskstatus, current_date))
            conn.commit()
            self.enter_task.delete(0,'end')
        else:
            mb.showwarning("Warning", "You must enter a task.")
            
        self.load_tasks()
        
    def update_status(self):
        now = dt.now()
        current_date = now.strftime("%Y-%b-%d")
        task_oid = None
        new_status = None
        new_status = self.update_task.get()

        if self.listbox_incomplete.get('anchor'):
            taskname = self.listbox_incomplete.get('anchor',)
            index = (int(taskname.split('.')[0])-1)
            task_oid = self.tasks_id_incomp[index][0]
                
        if self.listbox_pending.get('anchor'):
            taskname = self.listbox_pending.get('anchor',)
            index = (int(taskname.split('.')[0])-1)
            task_oid = self.tasks_id_pend[index][0]
            
        if self.listbox_completed.get('anchor'):
            taskname = self.listbox_completed.get('anchor')
            index = (int(taskname.split('.')[0])-1)
            task_oid = self.tasks_id_comp[index][0]
            
        if new_status and task_oid:
            conn = sqlite3.connect('To_Do_List_db.db')
            cur = conn.cursor()
            comm = '''UPDATE Tasks SET Task_Status = ?, Date = ? WHERE oid = ?'''
            cur.execute(comm,(new_status, current_date,task_oid))
            conn.commit()
            self.update_task.delete(0,'end')
        else:
            mb.showwarning("Warning", "You must enter task Status as well \nas select task from list box.")
            
        self.load_tasks()

    def delete_tasks(self):
        task_oid = None
        if len(self.tasks_id_incomp) == 0 and len(self.tasks_id_pend) == 0 and len(self.tasks_id_comp) == 0:
            mb.showinfo('No Tasks','No tasks to delete')
            
        else:      
            if self.listbox_incomplete.get('anchor',):
                taskname = self.listbox_incomplete.get('anchor',)
                index = (int(taskname.split('.')[0])-1)
                task_oid = self.tasks_id_incomp[index][0]
                
            if self.listbox_pending.get('anchor'):
                taskname = self.listbox_pending.get('anchor',)
                index = (int(taskname.split('.')[0])-1)
                task_oid = self.tasks_id_pend[index][0]
            
            if self.listbox_completed.get('anchor'):
                taskname = self.listbox_completed.get('anchor')
                index = (int(taskname.split('.')[0])-1)
                task_oid = self.tasks_id_comp[index][0]
                
            if task_oid == None :
                mb.showwarning('Warning','Please select a task a to delete it')        
            
            else:
                connection = sqlite3.connect('To_Do_List_db.db')
                comm = '''DELETE FROM Tasks WHERE oid = ?'''
                connection.execute(comm,(task_oid,))
                connection.commit()

        self.load_tasks()

    def load_tasks(self):
        self.listbox_incomplete.delete(0,'end')
        self.listbox_pending.delete(0,'end')
        self.listbox_completed.delete(0,'end')
        
        conn = sqlite3.connect('To_Do_List_db.db')
        cur = conn.cursor()
        cur.execute('''SELECT oid,Task_name,Task_Status,Date FROM Tasks''')
        tasks = cur.fetchall()
        
        self.tasks_id_incomp = []
        self.tasks_id_pend = []
        self.tasks_id_comp = []

        incomp = 1
        pend = 1
        comp = 1
        
        for data in tasks:
            oid, taskname, taskstatus, date = data
            
            if taskstatus.lower() == 'incomplete':
                self.listbox_incomplete.insert('end',f'{incomp}.{taskname}')
                self.tasks_id_incomp.append(tuple([oid,taskname]))
                incomp += 1
                
            elif taskstatus.lower() not in ['incomplete', 'complete', 'completed', 'finished', 'completed task', 'complete task']:
                self.listbox_pending.insert('end',f'{pend}.{taskname}')
                self.tasks_id_pend.append(tuple([oid,taskname]))
                pend += 1
                
            elif taskstatus.lower() in ['complete','completed','finished','completed task','complete task']:
                self.listbox_completed.insert('end',f'{comp}.{taskname} => completed on {date}')
                self.tasks_id_comp.append(tuple([oid,taskname]))
                comp += 1
                
            else:
                mb.showwarning('Warning', 'Some error occurred while updating \ntask please try again')
        conn.commit()


root = tk.Tk()
app = ToDoList(root)
connection.commit()
connection.close()
root.mainloop()



