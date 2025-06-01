import pytest
import os
import shutil
from scanfiles import list_files, file_count, total_size, extensions

@pytest.fixture
def test_directory(tmp_path):
    # Create a temporary directory structure for testing
    test_dir = tmp_path / "test_project"
    test_dir.mkdir()
    
    # Create some test files
    (test_dir / "file1.txt").write_text("Hello")  # 5 bytes
    (test_dir / "file2.py").write_text("print('test')")  # 12 bytes
    (test_dir / "file3.py").write_text("def test(): pass")  # 15 bytes
    
    # Create a subdirectory with files
    subdir = test_dir / "subdir"
    subdir.mkdir()
    (subdir / "file4.txt").write_text("Test file")  # 9 bytes
    (subdir / ".hidden").write_text("hidden")  # Should be ignored
    
    # Save original working directory and change to test directory
    original_dir = os.getcwd()
    os.chdir(str(test_dir))
    
    yield test_dir
    
    # Cleanup: restore original working directory
    os.chdir(original_dir)

def test_file_counting(test_directory, capsys):
    stats = list_files(str(test_directory))
    
    # Check file count (should not count hidden files)
    assert stats['file_count'] == 4, "Should find 4 non-hidden files"

def test_size_calculation(test_directory, capsys):
    stats = list_files(str(test_directory))
    
    # Total size should be sum of all non-hidden files
    # 5 + 12 + 15 + 9 = 41 bytes
    assert stats['total_size'] == 43, "Total size should be 43 bytes"

def test_extension_tracking(test_directory, capsys):
    stats = list_files(str(test_directory))
    
    # Check extension counting
    assert stats['extensions'].get('txt', 0) == 2, "Should find 2 .txt files"
    assert stats['extensions'].get('py', 0) == 2, "Should find 2 .py files"

def test_hidden_files_ignored(test_directory, capsys):
    # Reset global variables
    global file_count, total_size, extensions
    file_count = 0
    total_size = 0
    extensions = {}
    
    list_files(str(test_directory))
    captured = capsys.readouterr()
    
    # Check that hidden files are not included in output
    assert '.hidden' not in captured.out, "Hidden files should not be included in output"

def test_empty_directory(tmp_path, capsys):
    # Create an empty directory
    empty_dir = tmp_path / "empty_project"
    empty_dir.mkdir()
    
    # Save original working directory and change to empty directory
    original_dir = os.getcwd()
    os.chdir(str(empty_dir))
    
    # Reset global variables
    global file_count, total_size, extensions
    file_count = 0
    total_size = 0
    extensions = {}
    
    list_files(str(empty_dir))
    
    # Restore original working directory
    os.chdir(original_dir)
    
    # Check that empty directory is handled correctly
    assert file_count == 0, "Empty directory should have 0 files"
    assert total_size == 0, "Empty directory should have 0 total size"
    assert len(extensions) == 0, "Empty directory should have no extensions"