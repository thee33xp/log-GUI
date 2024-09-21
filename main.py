import tkinter as tk
from gui import App

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Log Repository")
    root.geometry("1024x640")

    app = App(root)

    root.protocol("WM_DELETE_WINDOW", app.close)
    # Close the database on exit()
    root.mainloop()