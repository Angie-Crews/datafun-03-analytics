"""
Master script to run fetchs and processess in sequence
"""

import subprocess
import sys
from utils_logger import logger

def run_scripts():
    """List of scripts to run"""
    scripts = [
        'angiecrews_get_excel.py',
        'angiecrews_process_excel.py',
        'angiecrews_get_csv.py',
        'angiecrews_process_csv.py',
        'angiecrews_get_text.py',
        'angiecrews_process_text.py',
        'angiecrews_get_json.py',
        'angiecrews_process_json.py'
    ]
   
    """Length of scripts list"""
   
    print(f"Running {len(scripts)} scripts..")
   
    for i, script in enumerate(scripts, 1): #Using enumate to show index value along with actual script. Default is 0 overide by telling it start from 1
        print(f"\n[{i}/{len(scripts)}] Running {script}...") #printing progress inside loop
       
        try:
            subprocess.run([sys.executable, script], check=True) # run the process, raise an error and stop master sccript
            print(f"{script} completed successfully")
        except subprocess.CalledProcessError as e: #Exception handling
            print(f"{script} failed with error code {e.returncode}")
        except FileNotFoundError: #Exception handling
            print(f"{script} not found")
   
    print("\nIt is Finished!")


if __name__ == "__main__":
    run_scripts()