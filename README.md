

# Python Endpoint Activity Monitor

A modular desktop application designed to demonstrate system monitoring, data persistence, and architecture separation in Python. This project utilizes Object-Oriented Programming (OOP) principles to decouple background input tracking from the user interface.


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

You can run this project using standard pip or the modern `uv` package manager.

### Option A: Standard Python (pip)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/endpoint-monitor.git
    cd endpoint-monitor
    ```

2.  **Install dependencies:**
    ```bash
    pip install pynput
    ```

3.  **Run the application:**
    ```bash
    python main.py
    ```

### Option B: Modern Workflow (using `uv`)

If you are using `uv` for fast dependency management:

1.  **Initialize the project:**
    ```bash
    uv init endpoint-monitor
    cd endpoint-monitor
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
    *(Note: Ensure `pynput` is in your requirements.txt)*

4.  **Run the application:**
    ```bash
    python main.py
    ```

## Usage Guide

1.  **Launch the App:** Run `main.py` to open the control panel.
2.  **Start Monitoring:** Click the **Start** button. The application will begin capturing events in the background.
3.  **Stop & Save:** Click **Stop** to halt capture. You can then choose to export the buffered data to your preferred file format.
4.  **Clear Data:** Use the **Clear** button to wipe the current memory buffer without saving.

## Privacy Note

This application stores data **locally on your machine**. It does not possess networking capabilities and does not transmit logs to any external servers or third parties.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
