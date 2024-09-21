import tkinter as tk
from tkinter import messagebox
from database import connect_db, add_record, fetch_records, delete_record

class App:
    def __init__(self, master):
        self.master = master
        self.conn, self.cursor = connect_db()
        self.create_widgets()
        self.refresh_records()
    def create_widgets(self):
        self.name_label = tk.Label(self.master, text="Name")
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack(pady=5)

        self.date_label = tk.Label(self.master, text="Date")
        self.date_label.pack(pady=5)

        self.date_entry = tk.Entry(self.master)
        self.date_entry.pack(pady=5)

        self.description_label = tk.Label(self.master, text="Description")
        self.description_label.pack(pady=5)

        self.description_entry = tk.Text(self.master, height=5, width=40)
        self.description_entry.pack(pady=5)

        self.add_button = tk.Button(self.master, text="Add Log", command=self.add_record)
        self.add_button.pack(pady=10)

        self.listbox = tk.Listbox(self.master, width=80)
        self.listbox.pack(pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Log", command=self.delete_record)
        self.delete_button.pack(pady=10)

    def add_record(self):
        name = self.name_entry.get()
        date = self.date_entry.get()
        description = self.description_entry.get("1.0", "end-1c")

        if not name or not date or not description:
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                add_record(self.cursor, name, date, description)

                self.conn.commit()

                messagebox.showinfo("Success", "Log added to records")
                self.clear_entries()

                self.refresh_records()

            except Exception as e:
                messagebox.showerror("You broke it", str(e))


    def refresh_records(self):
        self.listbox.delete(0, tk.END)
        records = fetch_records(self.cursor)
        for record in records:
            self.listbox.insert(tk.END, "{}: {} | {} | {}".format(record[0], record[1], record[2], record[3]))
            
    def delete_record(self):
        selected_item = self.listbox.curselection()
        if selected_item:
            record_id = self.listbox.get(selected_item)[0]

            delete_record(self.cursor, record_id)
            self.conn.commit()

            messagebox.showinfo("Success", "Log deleted")
            self.refresh_records()
        
        else:

            messagebox.showwarning("Warning", "Select a record to delete")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.description_entry.delete("1.0", tk.END)

    def close(self):
        self.conn.close()

                

        

    