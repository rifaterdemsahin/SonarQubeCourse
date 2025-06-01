import unittest
import os
import tempfile
import shutil
from scanfiles import list_files, FileStats

class TestScanFiles(unittest.TestCase):
    def setUp(self):
        """Create a temporary test directory with sample files."""
        self.test_dir = tempfile.mkdtemp()
        
        # Create test files structure
        self.create_test_files()
        
        # Store original directory and move to test directory
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        """Clean up test directory after tests."""
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir)

    def create_test_files(self):
        """Create a set of test files with known structure."""
        # Create some regular files
        test_files = {
            'test1.py': 'print("Hello")',
            'test2.py': 'def test(): pass',
            'readme.md': '# Test Project',
            'config.json': '{"test": true}',
            '.gitignore': '*.pyc\n.DS_Store',  # Hidden file
        }
        
        # Create files in root
        for filename, content in test_files.items():
            file_path = os.path.join(self.test_dir, filename)
            with open(file_path, 'w') as f:
                f.write(content)
        
        # Create a subdirectory with files
        subdir = os.path.join(self.test_dir, 'subdir')
        os.makedirs(subdir)
        with open(os.path.join(subdir, 'nested.py'), 'w') as f:
            f.write('# Nested file')

    def test_file_counting(self):
        """Test that files are counted correctly."""
        stats = list_files(self.test_dir)
        
        # We expect 5 non-hidden files (3 .py, 1 .md, 1 .json)
        self.assertEqual(stats.file_count, 5)
        
        # Check extension counts
        self.assertEqual(stats.extensions['py'], 3)
        self.assertEqual(stats.extensions['md'], 1)
        self.assertEqual(stats.extensions['json'], 1)

    def test_hidden_files_excluded(self):
        """Test that hidden files are properly excluded."""
        stats = list_files(self.test_dir)
        
        # .gitignore should not be counted
        self.assertNotIn('gitignore', stats.extensions)
        self.assertEqual(stats.file_count, 5)  # Only non-hidden files

    def test_total_size(self):
        """Test that file sizes are calculated correctly."""
        stats = list_files(self.test_dir)
        
        # Calculate expected size manually
        expected_size = sum(
            os.path.getsize(os.path.join(root, file))
            for root, _, files in os.walk(self.test_dir)
            for file in files
            if not file.startswith('.')
        )
        
        self.assertEqual(stats.total_size, expected_size)

    def test_empty_directory(self):
        """Test behavior with an empty directory."""
        empty_dir = tempfile.mkdtemp()
        try:
            stats = list_files(empty_dir)
            self.assertEqual(stats.file_count, 0)
            self.assertEqual(stats.total_size, 0)
            self.assertEqual(len(stats.extensions), 0)
        finally:
            shutil.rmtree(empty_dir)

    def test_file_stats_initialization(self):
        """Test FileStats class initialization."""
        stats = FileStats()
        self.assertEqual(stats.file_count, 0)
        self.assertEqual(stats.total_size, 0)
        self.assertIsNotNone(stats.extensions)
        self.assertEqual(len(stats.extensions), 0)

if __name__ == '__main__':
    unittest.main()