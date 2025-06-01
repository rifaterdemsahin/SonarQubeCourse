import unittest
import os
import tempfile
import shutil
from unittest.mock import patch
import sys
from io import StringIO

from scanfiles import list_files, FileStats

class TestFileListing(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        
        # Create some test files
        self.create_test_files()
        
        # Change to test directory
        os.chdir(self.test_dir)
        
    def tearDown(self):
        """Clean up after each test method."""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)
        
    def create_test_files(self):
        """Create test files in the temporary directory."""
        # Create regular files
        with open(os.path.join(self.test_dir, "test.py"), "w") as f:
            f.write("print('hello')")
        with open(os.path.join(self.test_dir, "readme.txt"), "w") as f:
            f.write("This is a readme file")
        with open(os.path.join(self.test_dir, "config.json"), "w") as f:
            f.write('{"key": "value"}')
            
        # Create a hidden file (should be ignored)
        with open(os.path.join(self.test_dir, ".hidden"), "w") as f:
            f.write("hidden content")
            
        # Create a subdirectory with files
        subdir = os.path.join(self.test_dir, "subdir")
        os.makedirs(subdir)
        with open(os.path.join(subdir, "nested.py"), "w") as f:
            f.write("# nested file")

    @patch('sys.stdout', new_callable=StringIO)
    def test_list_files_function(self, mock_stdout):
        """Test the list_files function returns correct statistics."""
        result = list_files(".")
        
        # Verify count, ensure we found the correct number of non-hidden files
        self.assertEqual(result.count, 4, "Should find exactly 4 non-hidden files")
        
        # Verify we found the expected file types
        self.assertEqual(result.extensions.get('py', 0), 2, "Should find 2 Python files")
        self.assertEqual(result.extensions.get('txt', 0), 1, "Should find 1 text file")
        self.assertEqual(result.extensions.get('json', 0), 1, "Should find 1 JSON file")
        
        # Verify hidden files were not included in extensions
        self.assertNotIn('hidden', result.extensions, "Should not count hidden files")
        
        # Verify total size is positive (actual size will vary by platform)
        self.assertGreater(result.size, 0, "Total size should be greater than 0")

    def test_file_size_calculation(self):
        """Test file size calculation for known content."""
        file_path = os.path.join(self.test_dir, "known_size.txt")
        content = "test content"
        with open(file_path, "w") as f:
            f.write(content)
            
        result = list_files(self.test_dir)
        self.assertGreaterEqual(result.size, len(content), 
                              "Total size should be at least the size of our test file")

    def test_empty_directory(self):
        """Test scanning an empty directory."""
        empty_dir = tempfile.mkdtemp()
        try:
            result = list_files(empty_dir)
            self.assertEqual(result.count, 0, "Empty directory should have no files")
            self.assertEqual(result.size, 0, "Empty directory should have zero total size")
            self.assertEqual(result.extensions, {}, "Empty directory should have no extensions")
        finally:
            shutil.rmtree(empty_dir)

if __name__ == '__main__':
    unittest.main()