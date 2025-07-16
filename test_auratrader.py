# test_auratrader.py
"""
Tests for AuraTrader module.
"""

import unittest
from auratrader import AuraTrader

class TestAuraTrader(unittest.TestCase):
    """Test cases for AuraTrader class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AuraTrader()
        self.assertIsInstance(instance, AuraTrader)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AuraTrader()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
