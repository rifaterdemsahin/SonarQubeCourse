import os
from datetime import datetime
from typing import Dict, NamedTuple, Optional

class FileStats(NamedTuple):
    count: int
    size: int
    extensions: Dict[str, int]

def process_file(file_path: str) -> tuple[int, int, str]:
    """Process a single file and return its stats."""
    size = os.path.getsize(file_path)
    ext = os.path.splitext(file_path)[1][1:].lower() if '.' in file_path else ''
    
    print(f"{file_path} | Size: {size} bytes | Modified: "
          f"{datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')}")
    
    return 1, size, ext

def list_files(project_path: Optional[str] = None) -> FileStats:
    """
    List files in a directory and collect statistics.
    
    Args:
        project_path (Optional[str]): Path to the directory to scan. Defaults to current directory.
        
    Returns:
        FileStats: Named tuple containing (file count, total size, extension counts)
    """
    if project_path is None:
        project_path = "."
        
    file_count = 0
    total_size = 0
    extensions: Dict[str, int] = {}
    
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.startswith('.'):
                continue
                
            file_path = os.path.join(root, file)
            if not os.path.isfile(file_path):
                continue
                
            count, size, ext = process_file(file_path)
            file_count += count
            total_size += size
            if ext:
                extensions[ext] = extensions.get(ext, 0) + 1
    
    print("\n--- Summary ---")
    print(f"Total files: {file_count}")
    print(f"Total size: {total_size} bytes")
    print("File types found:")
    
    for ext, count in sorted(extensions.items()):
        print(f"  .{ext}: {count} files")
    
    return FileStats(file_count, total_size, extensions)

if __name__ == '__main__':
    print("Listing all files in project...")
    list_files()
    print("Done!")