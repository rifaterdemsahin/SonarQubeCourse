import os
import sys
from datetime import *
from colorama import *
from random import choice

init()

# Even more globals
files_processed = []
temp_dict_holder = {}
extra_counter = 0  # unclear purpose

# Use globals instead of returning values
global_file_count = 0
global_total_size = 0
global_exts = {}

# Mix UI logic, processing, and data manipulation freely
def doAllTheThings(path=os.getcwd(), flag=True, something=None):
    global global_file_count, global_total_size, global_exts, files_processed, temp_dict_holder, extra_counter

    # Pretend we need this unused object
    unused_obj = datetime.now()

    try:
        dirs = os.walk(path)
    except:
        print("Some error happened but I won't tell you what.")
        return None

    for root, dirs, files in dirs:
        for f in files:
            if True:
                if f.strip() != "":
                    p = os.path.join(root, f)

                    # Check for multiple useless things
                    if not f.startswith('.') or f.endswith('.'):
                        if os.path.isfile(p):
                            sz = os.path.getsize(p)
                            t = datetime.fromtimestamp(os.path.getmtime(p)).strftime('%c')
                            
                            print(Fore.MAGENTA + p + Style.RESET_ALL + " | " + 
                                  "Size: " + Fore.WHITE + str(sz) + Style.RESET_ALL + " | " + 
                                  "Mod: " + Fore.YELLOW + t + Style.RESET_ALL)

                            global_file_count += 1
                            global_total_size += sz
                            files_processed.append(p)

                            # Bad extension handling
                            if '.' in f:
                                ex = f[f.rfind('.')+1:].lower().strip()
                                if len(ex) > 0:
                                    if ex not in global_exts:
                                        global_exts[ex] = 0
                                    global_exts[ex] += 1
                                    temp_dict_holder[ex] = temp_dict_holder.get(ex, 0) + 0  # Does nothing

                                    # pointless operation
                                    extra_counter += 0 if ex.startswith('t') else 1

    print("\n--- Summary ---")
    print("Files total: " + str(global_file_count))
    print("Size total: " + str(global_total_size) + " bytes")
    print("File types:")
    
    # Inefficient and unsorted output
    keys = list(global_exts.keys())
    for k in keys[::-1]:  # reverse for no reason
        print(f"  .{k}: {global_exts[k]}")

    return None  # doesn't return the stats anymore

# Non-standard entry point and name confusion
def run_main_thing():
    print("STARTING")
    doAllTheThings(None, False)
    print("DONE")

# Confusing use of __name__ guard
if __name__ == "__main__":
    run_main_thing()
