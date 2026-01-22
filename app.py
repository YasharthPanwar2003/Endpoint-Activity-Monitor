import tkinter as tk
from tkinter import messagebox
from backend import KeyLoggerService 

class AppUI:
    def __init__(self, root: tk.Tk, logger_service: KeyLoggerService):
        self.root = root
        self.logger = logger_service
        
        self.root.title("Activity Monitor | Educational Build")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.config(bg='#2C3E50') # Professional Dark Blue/Grey
        self._setup_ui()

    def _setup_ui(self):
        lbl_title = tk.Label(self.root, text="System Monitor", 
                             font=("Helvetica", 18, "bold"), 
                             bg='#2C3E50', fg='#ECF0F1')
        lbl_title.pack(pady=30)

        self.lbl_status = tk.Label(self.root, text="Status: Idle", 
                                   font=("Helvetica", 10), 
                                   bg='#2C3E50', fg='#BDC3C7')
        self.lbl_status.pack(pady=5)

        btn_frame = tk.Frame(self.root, bg='#2C3E50')
        btn_frame.pack(pady=20)

        self._create_btn(btn_frame, "Start Monitoring", self.handle_start, "#27AE60") # Green
        self._create_btn(btn_frame, "Stop Monitoring", self.handle_stop, "#C0392B")  # Red
        
        tk.Frame(btn_frame, height=20, bg='#2C3E50').pack() # Spacer

        self._create_btn(btn_frame, "Export to TXT", self.handle_txt, "#E67E22")
        self._create_btn(btn_frame, "Export to CSV", self.handle_csv, "#E67E22")
        self._create_btn(btn_frame, "Clear Memory", self.handle_clear, "#7F8C8D")

    def _create_btn(self, parent, text, command, color):
        btn = tk.Button(parent, text=text, command=command, 
                        width=25, height=2, 
                        bg=color, fg='white', 
                        font=("Helvetica", 9, "bold"),
                        relief="flat", borderwidth=0)
        btn.pack(pady=5)

    def handle_start(self):
        if self.logger.is_running:
            messagebox.showinfo("Info", "Monitor is already running.")
            return
        
        self.logger.start_logging()
        self.lbl_status.config(text="Status: Recording...", fg="#2ECC71")

    def handle_stop(self):
        if not self.logger.is_running:
            return
        
        self.logger.stop_logging()
        self.lbl_status.config(text="Status: Stopped", fg="#E74C3C")

    def handle_txt(self):
        msg = self.logger.export_to_txt()
        messagebox.showinfo("Export", msg)

    def handle_csv(self):
        msg = self.logger.export_to_csv()
        messagebox.showinfo("Export", msg)

    def handle_clear(self):
        self.logger.clear_logs()
        messagebox.showinfo("Memory", "Log buffer cleared.")
