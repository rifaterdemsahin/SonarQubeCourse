import os
from datetime import datetime
from dataclasses import dataclass
from typing import Dict, Optional
from colorama import init, Fore, Style

# Initialize colorama
init()

@dataclass
class FileStats:
    """Data class to hold file statistics"""
    file_count: int = 0
    total_size: int = 0
    extensions: Dict[str, int] = None

    def __post_init__(self):
        if self.extensions is None:
            self.extensions = {}

class FileScanner:
    def __init__(self, project_path: Optional[str] = None):
        self.project_path = project_path or os.getcwd()

    def get_file_info(self, file_path: str) -> tuple:
        """Get file information for a single file"""
        size = os.path.getsize(file_path)
        modified_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        return size, modified_time

    def get_file_extension(self, filename: str) -> str:
        """Extract file extension from filename"""
        return filename.split('.')[-1].lower() if '.' in filename else 'no_extension'

    def scan_files(self) -> FileStats:
        """Scan files and return statistics"""
        stats = FileStats()
        
        try:
            for root, _, files in os.walk(self.project_path):
                for file in files:
                    if file.startswith('.'):
                        continue
                        
                    file_path = os.path.join(root, file)
                    if not os.path.isfile(file_path):
                        continue

                    size, modified_time = self.get_file_info(file_path)
                    self._print_file_info(file_path, size, modified_time)
                    
                    stats.file_count += 1
                    stats.total_size += size
                    
                    ext = self.get_file_extension(file)
                    stats.extensions[ext] = stats.extensions.get(ext, 0) + 1
                    
        except Exception as e:
            print(f"Error scanning files: {str(e)}")
            
        return stats

    def _print_file_info(self, file_path: str, size: int, modified_time: str) -> None:
        """Print formatted file information"""
        print(f"{Fore.CYAN}{file_path}{Style.RESET_ALL} | "
              f"Size: {Fore.GREEN}{size} bytes{Style.RESET_ALL} | "
              f"Modified: {Fore.YELLOW}{modified_time}{Style.RESET_ALL}")

    def print_summary(self, stats: FileStats) -> None:
        """Print summary of file statistics"""
        print(f"\n{Fore.BLUE}{Style.BRIGHT}--- Summary ---{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{Style.BRIGHT}Total files:{Style.RESET_ALL} {Fore.GREEN}{stats.file_count}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{Style.BRIGHT}Total size:{Style.RESET_ALL} {Fore.GREEN}{stats.total_size} bytes{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{Style.BRIGHT}File types found:{Style.RESET_ALL}")
        
        for ext, count in sorted(stats.extensions.items()):
            print(f"  {Fore.CYAN}.{ext}:{Style.RESET_ALL} {Fore.GREEN}{count} files{Style.RESET_ALL}")

def list_files(directory):
    """
    Lists all non-hidden files in a directory and its subdirectories,
    returning statistics about the files.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
        
    stats = {
        'file_count': 0,
        'total_size': 0,
        'extensions': {}
    }

    for root, dirs, files in os.walk(directory):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            # Skip hidden files
            if file.startswith('.'):
                continue
                
            file_path = os.path.join(root, file)
            
            # Update file count
            stats['file_count'] += 1
            
            # Update total size
            stats['total_size'] += os.path.getsize(file_path)
            
            # Update extension count
            _, ext = os.path.splitext(file)
            if ext:
                # Remove the dot from extension
                ext = ext[1:]
                stats['extensions'][ext] = stats['extensions'].get(ext, 0) + 1

    return stats

# These functions are also imported in the test but appear to be unused
def file_count(directory):
    return list_files(directory)['file_count']

def total_size(directory):
    return list_files(directory)['total_size']

def extensions(directory):
    return list_files(directory)['extensions']

def main():
    scanner = FileScanner()
    print("Scanning files in project...")
    stats = scanner.scan_files()
    scanner.print_summary(stats)
    print("Done!")

if __name__ == "__main__":
    main()
