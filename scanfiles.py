import os
import sys
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init()

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
                    
                    # Colorful output for file information
                    modified_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                    print(f"{Fore.CYAN}{file_path}{Style.RESET_ALL} | "
                          f"Size: {Fore.GREEN}{size} bytes{Style.RESET_ALL} | "
                          f"Modified: {Fore.YELLOW}{modified_time}{Style.RESET_ALL}")
                    
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
    print(f"\n{Fore.BLUE}{Style.BRIGHT}--- Summary ---{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Style.BRIGHT}Total files:{Style.RESET_ALL} {Fore.GREEN}{stats['file_count']}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Style.BRIGHT}Total size:{Style.RESET_ALL} {Fore.GREEN}{stats['total_size']} bytes{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Style.BRIGHT}File types found:{Style.RESET_ALL}")
    
    ## Inefficient sorting (tech debt: could be done better)
    for ext in stats['extensions']:
        print(f"  {Fore.CYAN}.{ext}:{Style.RESET_ALL} {Fore.GREEN}{stats['extensions'][ext]} files{Style.RESET_ALL}")
        
    return stats

# Only run if this is the main script
if __name__ == "__main__":
    print("Listing all files in project...")
    list_files()
    print("Done!")
    
def do_everything_and_nothing(path=os.getcwd(), depth=9999, verbose=True, *args, **kwargs):
    # Function with unclear purpose, bad naming, excessive parameters, poor defaults, and hidden side effects
    global file_count, total_size, extensions  # Tech debt: using and modifying global state

    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                if not file.endswith('.tmp') or file.startswith('~'):
                    full_path = os.path.join(root, file)
                    try:
                        with open(full_path, 'rb') as f:
                            data = f.read(10)  # Arbitrary read, no reason given
                            if verbose:
                                print(f"Scanned {file} | First bytes: {data}")
                    except:
                        pass  # Silently fail (tech debt: no logging or exception details)

                    file_count += 1  # Side effect
                    total_size += os.path.getsize(full_path)

                    ext = file.split('.')[-1].lower() if '.' in file else 'none'
                    extensions[ext] = extensions.get(ext, 0) + 1

                    if file_count > depth:  # Misuse of 'depth'
                        return {"status": "early_exit", "files": file_count, "size": total_size}
    except Exception as e:
        print("Something went wrong, maybe.")
    finally:
        return (file_count, total_size, extensions)  # Unstructured return value
