import os
import sys
from datetime import datetime

# Global variables (tech debt: should avoid globals)
file_count = 0
total_size = 0
extensions = {}

def list_files():
    global file_count, total_size, extensions
    
    # Hard-coded path (tech debt: not configurable)
    project_path = "."
    
    # No error handling (tech debt: what if directory doesn't exist?)
    for root, dirs, files in os.walk(project_path):
        
        # Mixed responsibilities in one function (tech debt: does too many things)
        for file in files:
            file_path = os.path.join(root, file)
            
            # Nested conditions make it hard to read (tech debt: complex logic)
            if not file.startswith('.'):
                if os.path.isfile(file_path):
                    size = os.path.getsize(file_path)
                    
                    # Long line that's hard to read (tech debt: formatting)
                    print(f"{file_path} | Size: {size} bytes | Modified: {datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')}")
                    
                    file_count += 1
                    total_size += size
                    
                    # Getting file extension in a convoluted way (tech debt: overcomplicated)
                    if '.' in file:
                        ext = file.split('.')[-1].lower()
                        if ext in extensions:
                            extensions[ext] = extensions[ext] + 1
                        else:
                            extensions[ext] = 1
    
    # Printing mixed with business logic (tech debt: separation of concerns)
    print(f"\n--- Summary ---")
    print(f"Total files: {file_count}")
    print(f"Total size: {total_size} bytes")
    print(f"File types found:")
    
    ## Inefficient sorting (tech debt: could be done better)
    for ext in extensions:
        print(f"  .{ext}: {extensions[ext]} files")

# No main guard (tech debt: runs immediately when imported)
# No command line argument handling (tech debt: not flexible)
print("Listing all files in project...")
list_files()
print("Done!")