# test_elitenova.py
"""
Tests for EliteNova module.
"""

import unittest
from elitenova import EliteNova

class TestEliteNova(unittest.TestCase):
    """Test cases for EliteNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EliteNova()
        self.assertIsInstance(instance, EliteNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EliteNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
