import pytest
import os
from pathlib import Path
from scanfiles import list_files, file_count, total_size, extensions

@pytest.fixture
def test_directory(tmp_path):
    """Create a test directory structure with sample files."""
    test_dir = tmp_path / "test_project"
    test_dir.mkdir()
    
    # Create test files with known content
    files = {
        "file1.txt": "Hello",                    # 5 bytes
        "file2.py": "print('test')",            # 12 bytes
        "file3.py": "def test(): pass",         # 15 bytes
        "subdir/file4.txt": "Test file",        # 9 bytes
        "subdir/.hidden": "hidden"              # hidden file
    }
    
    for filepath, content in files.items():
        file_path = test_dir / filepath
        file_path.parent.mkdir(exist_ok=True)
        file_path.write_text(content)
    
    with pytest.MonkeyPatch().context() as mp:
        mp.chdir(str(test_dir))
        yield test_dir

class TestFileScanning:
    """Test suite for file scanning functionality."""
    
    def test_file_counting(self, test_directory):
        """Test if the correct number of files is counted."""
        stats = list_files(str(test_directory))
        assert stats['file_count'] == 4, "Should find 4 non-hidden files"

    def test_size_calculation(self, test_directory):
        """Test if the total file size is calculated correctly."""
        stats = list_files(str(test_directory))
        expected_size = 5 + 12 + 15 + 9  # Sum of all non-hidden files
        assert stats['total_size'] == expected_size, f"Total size should be {expected_size} bytes"

    def test_extension_tracking(self, test_directory):
        """Test if file extensions are tracked correctly."""
        stats = list_files(str(test_directory))
        expected_extensions = {'txt': 2, 'py': 2}
        assert stats['extensions'] == expected_extensions, "Extension counts don't match expected values"

    def test_hidden_files_ignored(self, test_directory, capsys):
        """Test if hidden files are properly ignored."""
        list_files(str(test_directory))
        captured = capsys.readouterr()
        assert '.hidden' not in captured.out, "Hidden files should not be included in output"

    def test_empty_directory(self, tmp_path):
        """Test handling of empty directories."""
        empty_dir = tmp_path / "empty_project"
        empty_dir.mkdir()
        
        with pytest.MonkeyPatch().context() as mp:
            mp.chdir(str(empty_dir))
            stats = list_files(str(empty_dir))
        
        assert stats['file_count'] == 0, "Empty directory should have 0 files"
        assert stats['total_size'] == 0, "Empty directory should have 0 total size"
        assert stats['extensions'] == {}, "Empty directory should have no extensions"

    def test_directory_not_found(self):
        """Test handling of non-existent directories."""
        with pytest.raises(FileNotFoundError):
            list_files("/nonexistent/directory")

    def test_nested_directories(self, test_directory):
        """Test if nested directories are properly scanned."""
        stats = list_files(str(test_directory))
        subdir_file = test_directory / "subdir" / "file4.txt"
        assert subdir_file.exists(), "Nested file should exist"
        assert stats['extensions']['txt'] == 2, "Should count files in subdirectories"