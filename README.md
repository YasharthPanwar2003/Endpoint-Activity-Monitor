

# Python Endpoint Activity Monitor

## Project Overview

This application functions as a local input event logger. It captures keyboard activities in the background, buffers the data for performance optimization, and allows the user to export logs in various structured formats. The system is built with a focus on clean architecture, separating the backend monitoring logic from the frontend Tkinter GUI.

### Key Features

*   **Real-time Monitoring:** Asynchronous background capture of input events using `pynput`.
*   **Performance Optimization:** Implements data buffering to minimize I/O operations, storing logs in memory before flushing to disk.
*   **Versatile Exports:** Supports saving log data to **.txt**, **.csv**, or **.json** formats.
*   **Session Management:** GUI-based controls to Start, Stop, and Clear logging sessions instantly.
*   **Clean Architecture:** Strict separation of concerns between the logging engine and the display layer.

## Technical Stack

*   **Language:** Python 3.10+
*   **Core Library:** `pynput` (Input monitoring)
*   **Interface:** `tkinter` (Standard Python GUI)
*   **Package Manager:** `pip` or `uv`

## Installation and Setup

### Option A: Standard Python (pip)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/Endpoint-Activity-Monitor.git
    cd Endpoint-Activity-Monitor
    ```

2.  **Install dependencies:**
    ```bash
    pip install pynput
    ```

3.  **Run the application:**
    ```bash
    python main.py
    ```

### Option B: Using `uv`

1.  **Initialize the project:**
    ```bash
    uv init Endpoint-Activity-Monitor
    cd Endpoint-Activity-Monitor
    ```

2.  **Create and activate virtual environment:**
    *   **Windows (PowerShell):**
        ```powershell
        .venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```

3.  **Install dependencies:**
    ```bash
    uv pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python main.py
    ```

## Usage Guide: 

1.  **Launch the App:** Run `main.py` to open the control panel.
2.  **Start Monitoring:** Click the **Start** button. Application will begin capturing events in the background.
3.  **Stop & Save:** Click **Stop** to halt capture. Export the buffered data to your preferred file format.
4.  **Clear Data:** Use the **Clear** button to wipe the current memory buffer without saving.

## Privacy Note

This application stores data **locally on your machine** and does not possess networking capabilities nor transmit logs to any external servers or third parties.
