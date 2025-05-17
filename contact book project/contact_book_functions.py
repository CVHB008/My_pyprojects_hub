# functions defined in one module
import sqlite3 as sq
from tkinter import messagebox as mb


def db_conn():
    conn = sq.connect('Contactbook.db')
    return conn


def removeisosurface(self):
    self.button_add.place_forget()


def clear_form_fields(self):
    self.entry_oid.delete(0, 'end')
    self.first_entry.delete(0, 'end')
    self.last_entry.delete(0, 'end')
    self.phone_entry.delete(0, 'end')
    self.email_entry.delete(0, 'end')
    self.address_entry.delete(0, 'end')
    set_action_buttons(self)


def create_table():
    conn = db_conn()
    cur = conn.cursor()
    sql_query = '''CREATE TABLE IF NOT EXISTS Contact_book (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                f_name TEXT,
                l_name TEXT,
                phone TEXT,
                email TEXT,
                address TEXT)'''
    cur.execute(sql_query)
    conn.commit()


def add_person(self):

    # return if first name or last name empty

    if self.first_entry.get() == "" or self.last_entry.get() == "":
        mb.showwarning('Warning', 'First, Last name are required')

    else:
        # put input fields into tuple
        insert_row = (self.first_entry.get(), self.last_entry.get(), self.email_entry.get(),
                      self.phone_entry.get(), self.address_entry.get())
        conn = db_conn()
        with conn:
            cur = conn.cursor()
            sql_query = '''INSERT INTO Contact_book (f_name, l_name, email, phone, address) 
                            VALUES (?, ?, ?, ?, ?)'''
            cur.execute(sql_query, insert_row)
            conn.commit()
        conn.close()
    clear_form_fields(self)
    load_contactlist(self)


def load_contactlist(self):
    self.contacts_id = []
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT f_name, l_name, email, phone, address, oid FROM Contact_book''')
    datum = cur.fetchall()
    self.contact_list.delete(0, 'end')

    n = 1
    for data in datum:
        f_name, l_name, email, phone, address, oid = data
        self.contacts_id.append((n, oid))
        self.contact_list.insert('end', f'{n}.{f_name} {l_name}')
        n += 1
    conn.commit()
    conn.close()


def select_entry(self):
    oid = None
    contact = self.contact_list.get('anchor', )

    self.first_entry.delete(0, 'end')
    self.last_entry.delete(0, 'end')
    self.phone_entry.delete(0, 'end')
    self.email_entry.delete(0, 'end')
    self.address_entry.delete(0, 'end')
    self.contact_list.delete(0, 'end')

    conn = db_conn()
    cur = conn.cursor()
    try:
        index = (int(contact.split('.')[0]) - 1)
        oid = self.contacts_id[index][1]
        cur.execute('''SELECT f_name, l_name, email, phone, address FROM Contact_book WHERE oid = ?''', (oid,))
        data = cur.fetchone()

        f_name, l_name, email, phone, address = data
        self.entry_oid.insert(0, oid)
        self.first_entry.insert(0, f_name)
        self.last_entry.insert(0, l_name)
        self.phone_entry.insert(0, phone)
        self.email_entry.insert(0, email)
        self.address_entry.insert(0, address)

    except:
        load_contactlist(self)
        set_action_buttons(self, False)

    load_contactlist(self)
    set_action_buttons(self, False)
    conn.commit()
    conn.close()


def edit_person(self):
    if self.first_entry.get() == "" or self.last_entry.get() == "":
        mb.showwarning('Warning', 'First, Last name are required')
    else:
        update = (self.first_entry.get(), self.last_entry.get(), self.phone_entry.get(), self.email_entry.get(),
                  self.address_entry.get(), self.entry_oid.get(),)
        conn = db_conn()
        cur = conn.cursor()
        query = '''UPDATE Contact_book SET f_name = ?, l_name=?, phone=?, email=?, address=? WHERE oid = ?'''
        cur.execute(query, update)
        conn.commit()
    load_contactlist(self)
    clear_form_fields(self)


def remove_person(self):
    oid = self.entry_oid.get()
    conn = db_conn()
    cur = conn.cursor()

    query = '''DELETE FROM Contact_book WHERE oid = ?'''
    cur.execute(query, (oid,))
    conn.commit()
    conn.close()
    load_contactlist(self)
    clear_form_fields(self)


def set_action_buttons(self, add=True):
    if add:
        self.button_remove.grid_remove()
        self.button_edit.grid_remove()
        self.button_clear.grid_remove()
        self.button_add.grid()
    else:
        self.button_add.grid_remove()
        self.button_remove.grid()
        self.button_edit.grid()
        self.button_clear.grid()


