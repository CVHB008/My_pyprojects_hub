import tkinter as tk
import contact_book_functions as cbf


def load_gui(self, root):
        root.title('Contact Book')
        root.geometry('500x320')
        fonts = 'Helvetica 11'

        self.entry_oid = tk.Entry(root)

        self.first_name = tk.Label(root, text='First name  ', font=fonts)
        self.first_entry = tk.Entry(root, width=24, font=fonts)
        self.first_name.place(x=20, y=10)
        self.first_entry.place(x=20, y=30)

        self.last_name = tk.Label(root, text='Last name  ', font=fonts)
        self.last_entry = tk.Entry(root, width=24, font=fonts)
        self.last_name.place(x=20, y=60)
        self.last_entry.place(x=20, y=80)

        self.phone = tk.Label(root, text='Phone number  ', font=fonts)
        self.phone_entry = tk.Entry(root, width=24, font=fonts)
        self.phone.place(x=20, y=110)
        self.phone_entry.place(x=20, y=130)

        self.email = tk.Label(root, text='Email  ', font=fonts)
        self.email_entry = tk.Entry(root, width=24, font=fonts)
        self.email.place(x=20, y=160)
        self.email_entry.place(x=20, y=180)

        self.address = tk.Label(root, text='Address ', font=fonts)
        self.address_entry = tk.Entry(root, width=24, font=fonts)
        self.address.place(x=20, y=210)
        self.address_entry.place(x=20, y=230)

        #action frame for buttons add, edit, remove, clear fields
        self.actionframe = tk.LabelFrame(root, relief='flat')
        self.actionframe.place(x=20, y=260)

        self.button_add = tk.Button(self.actionframe, text='Add', font=fonts,padx=5, bg='#dcdcdc',
                                    command=lambda: cbf.add_person(self))
        self.button_add.grid(row=0, column=0)

        self.button_edit = tk.Button(self.actionframe, text='Edit', padx=5, pady=5, bg='#dcdcdc',
                                     command=lambda: cbf.edit_person(self))
        self.button_edit.grid(row=0, column=0, padx=5)
        self.button_edit.grid_remove()

        self.button_remove = tk.Button(self.actionframe, text='Remove', padx=5, pady=5, bg='#dcdcdc',
                                       command=lambda: cbf.remove_person(self))
        self.button_remove.grid(row=0, column=1, padx=5)
        self.button_remove.grid_remove()

        self.button_clear = tk.Button(self.actionframe, text='Clear', padx=5, pady=5, bg='#dcdcdc',
                                      command=lambda: cbf.clear_form_fields(self))
        self.button_clear.grid(row=0, column=2, padx=5)
        self.button_clear.grid_remove()

        self.label_contact = tk.Label(root, text='Contact list', font=fonts)
        self.label_contact.place(x=270, y=10)

        #Set a frame for listbox
        self.frame = tk.LabelFrame(root, font=fonts, padx=5, pady=5, relief='ridge')
        self.frame.place(x=270, y=30)
        self.sb = tk.Scrollbar(self.frame, orient='vertical')
        self.sb.pack(side='right', fill='both')
        self.contact_list = tk.Listbox(self.frame, height=12, width=24, font=fonts,yscrollcommand=self.sb.set)
        self.contact_list.pack()
        self.sb.config(command=self.contact_list.yview)
        self.contact_list.bind('<<ListboxSelect>>', lambda event: cbf.select_entry(self))
