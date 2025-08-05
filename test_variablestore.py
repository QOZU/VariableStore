# test_variablestore.py
"""
Tests for VariableStore module.
"""

import unittest
from variablestore import VariableStore

class TestVariableStore(unittest.TestCase):
    """Test cases for VariableStore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VariableStore()
        self.assertIsInstance(instance, VariableStore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VariableStore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
