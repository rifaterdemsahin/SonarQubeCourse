import os
import sys
from datetime import datetime

# Global variables (tech debt: should avoid globals)
# Tech debt: should avoid globals
file_count = 0
total_size = 0
extensions = {}

def list_files(project_path=None):
    # Initialize counters
    stats = {
        'file_count': 0,
        'total_size': 0,
        'extensions': {}
    }
    
    # Use current directory if no path provided
    if project_path is None:
        project_path = os.getcwd()
    
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
                    
                    stats['file_count'] += 1
                    stats['total_size'] += size
                    
                    # Getting file extension in a convoluted way (tech debt: overcomplicated)
                    if '.' in file:
                        ext = file.split('.')[-1].lower()
                        if ext in stats['extensions']:
                            stats['extensions'][ext] = stats['extensions'][ext] + 1
                        else:
                            stats['extensions'][ext] = 1
    
    ## Printing mixed with business logic (tech debt: separation of concerns)
    print("\n--- Summary ---")
    print(f"Total files: {stats['file_count']}")
    print(f"Total size: {stats['total_size']} bytes")
    print("File types found:")
    
    ## Inefficient sorting (tech debt: could be done better)
    for ext in stats['extensions']:
        print(f"  .{ext}: {stats['extensions'][ext]} files")
        
    return stats

# Only run if this is the main script
if __name__ == "__main__":
    print("Listing all files in project...")
    list_files()
    print("Done!")