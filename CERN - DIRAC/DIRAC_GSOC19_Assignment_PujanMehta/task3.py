"""
INSTRUCTIONS TO RUN THIS FILE:
Inside the CLI run this command: python task3.py
"""

import psutil
import json


def get_current_process():
    # Initialize the current process
    current_process = psutil.Process()

    # Gets the current process id
    current_process_id = current_process.pid

    # Gets the current process name
    current_process_name = current_process.name()

    # Gets the current process status
    current_process_status = current_process.status()

    # Gets the number of threads in the current process
    current_process_threads = current_process.num_threads()

    # Storing the process details in a dictionary
    current_process_dict = {
        "current_process_id": current_process_id,
        "current_process_name": current_process_name,
        "current_process_status": current_process_status,
        "current_process_threads": current_process_threads
    }

    with open("task3.json", "w+") as f:
        f.write(json.dumps(current_process_dict))
        f.close()


if __name__ == '__main__':
    get_current_process()