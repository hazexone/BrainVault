# test_brainvault.py
"""
Tests for BrainVault module.
"""

import unittest
from brainvault import BrainVault

class TestBrainVault(unittest.TestCase):
    """Test cases for BrainVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BrainVault()
        self.assertIsInstance(instance, BrainVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BrainVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
