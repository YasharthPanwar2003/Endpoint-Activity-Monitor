import tkinter as tk
from backend import KeyLoggerService
from interface import AppUI

def main():
    service = KeyLoggerService()
    root = tk.Tk()
    app = AppUI(root, service)
    root.mainloop()
    service.stop_logging()

if __name__ == "__main__":
    main()
