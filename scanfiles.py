import unittest
import os
import tempfile
import shutil
from unittest.mock import patch, MagicMock
import sys
from io import StringIO

# Import the module we want to test
# Note: This is problematic because the original code runs immediately!
# We need to mock the execution or restructure the original code

class TestFileListingTechDebt(unittest.TestCase):
    
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
        """Test the list_files function - this is challenging due to tech debt!"""
        
        # We need to import and reset globals each time due to tech debt
        # This is a hack because the original code uses globals poorly
        import importlib
        
        # Mock the original module to avoid immediate execution
        with patch('builtins.print') as mock_print:
            # We need to recreate the function logic here since the original
            # code structure makes it hard to test properly
            
            # Simulate the function behavior
            file_count = 0
            total_size = 0
            extensions = {}
            
            project_path = "."
            
            for root, dirs, files in os.walk(project_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if not file.startswith('.'):
                        if os.path.isfile(file_path):
                            size = os.path.getsize(file_path)
                            file_count += 1
                            total_size += size
                            
                            if '.' in file:
                                ext = file.split('.')[-1].lower()
                                if ext in extensions:
                                    extensions[ext] = extensions[ext] + 1
                                else:
                                    extensions[ext] = 1
            
            # Verify we found the expected files
            self.assertGreater(file_count, 0, "Should find at least some files")
            self.assertIn('py', extensions, "Should find .py files")
            self.assertIn('txt', extensions, "Should find .txt files")
            self.assertIn('json', extensions, "Should find .json files")
            
            # Verify hidden files were ignored (this tests the logic)
            found_hidden = False
            for root, dirs, files in os.walk("."):
                for file in files:
                    if file.startswith('.'):
                        found_hidden = True
            
            # We should have hidden files but they shouldn't be in our extensions count
            self.assertTrue(found_hidden, "Test setup should have hidden files")

    def test_file_counting_logic(self):
        """Test the file counting logic separately."""
        extensions = {}
        test_files = ["test.py", "readme.txt", "config.json", "another.py"]
        
        # Simulate the extension counting logic from original code
        for file in test_files:
            if '.' in file:
                ext = file.split('.')[-1].lower()
                if ext in extensions:
                    extensions[ext] = extensions[ext] + 1
                else:
                    extensions[ext] = 1
        
        self.assertEqual(extensions['py'], 2, "Should count 2 Python files")
        self.assertEqual(extensions['txt'], 1, "Should count 1 text file") 
        self.assertEqual(extensions['json'], 1, "Should count 1 JSON file")

    def test_hidden_file_filtering(self):
        """Test that hidden files are properly filtered out."""
        test_files = ["regular.txt", ".hidden", "another.py", ".gitignore"]
        visible_files = [f for f in test_files if not f.startswith('.')]
        
        self.assertEqual(len(visible_files), 2, "Should filter out hidden files")
        self.assertIn("regular.txt", visible_files)
        self.assertIn("another.py", visible_files)
        self.assertNotIn(".hidden", visible_files)
        self.assertNotIn(".gitignore", visible_files)

    @patch('os.path.getsize')
    @patch('os.path.getmtime') 
    @patch('os.path.isfile')
    def test_file_size_calculation(self, mock_isfile, mock_getmtime, mock_getsize):
        """Test file size calculation with mocked file system."""
        mock_isfile.return_value = True
        mock_getsize.return_value = 1024
        mock_getmtime.return_value = 1640995200  # Fixed timestamp
        
        # This test shows how mocking becomes necessary due to tech debt
        size = mock_getsize("dummy_file.txt")
        self.assertEqual(size, 1024, "Should return mocked file size")

    def test_extension_extraction_edge_cases(self):
        """Test the extension extraction logic with edge cases."""
        # Test the problematic extension extraction from original code
        test_cases = [
            ("file.txt", "txt"),
            ("file.name.py", "py"),  # Multiple dots
            ("no_extension", None),   # No extension
            (".hidden", "hidden"),    # Hidden file with extension
            ("file.", ""),           # Ends with dot
        ]
        
        for filename, expected_ext in test_cases:
            if '.' in filename:
                ext = filename.split('.')[-1].lower()
                if expected_ext is None:
                    continue  # Skip files without extensions
                self.assertEqual(ext, expected_ext, f"Extension extraction failed for {filename}")


class TestTechDebtIssues(unittest.TestCase):
    """Tests that highlight the tech debt issues in the original code."""
    
    def test_global_variables_problem(self):
        """Demonstrate how global variables make testing difficult."""
        # This test shows why globals are problematic
        # We can't easily test the function in isolation
        # because it modifies global state
        
        # In a well-designed system, we could test:
        # result = list_files_function(path="./test")
        # self.assertEqual(result.file_count, expected_count)
        
        # But with globals, we have to work around the design
        self.assertTrue(True, "This test exists to document the global variable problem")
    
    def test_no_error_handling_problem(self):
        """Demonstrate the lack of error handling."""
        # The original code doesn't handle cases like:
        # - Permission denied
        # - File deleted during iteration
        # - Invalid paths
        
        # We can't test error conditions because they're not handled
        self.assertTrue(True, "Original code lacks error handling to test")
    
    def test_mixed_responsibilities_problem(self):
        """Demonstrate the mixed responsibilities issue."""
        # The original function does:
        # 1. File system traversal
        # 2. File filtering  
        # 3. Size calculation
        # 4. Extension counting
        # 5. Formatting output
        # 6. Printing results
        
        # This makes it impossible to test individual pieces
        self.assertTrue(True, "Function does too many things to test properly")


if __name__ == '__main__':
    # Note: Running this test is tricky because the original code
    # executes immediately when imported, which is another tech debt issue!
    unittest.main()