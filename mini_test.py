#!/usr/bin/env python3
"""
Minimal Unit Tests - Core Functionality Only

Unit tests for core algorithm functionality.

Author: Zhentao Fan
Date: 2025-09-26
Usage: python mini_test.py
"""

import unittest
from main import option_0, time_measure


class TestCore(unittest.TestCase):
    """Test core functionality of the algorithm implementation."""
    
    def test_algorithm_basic(self):
        """
        Test basic algorithm functionality.
        
        Tests edge cases and normal operation of Option_0 algorithm.
        """
        # Test edge cases
        self.assertEqual(option_0(1), 0)
        self.assertEqual(option_0(2), 0)
        
        # Test normal cases
        result = option_0(100)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)
        
        print(f"✅ option_0(100) = {result}")
    
    def test_time_measurement(self):
        """
        Test time measurement functionality.
        
        Validates that time measurement returns positive float values.
        """
        time_result = time_measure(50, trials=3)
        self.assertIsInstance(time_result, float)
        self.assertGreater(time_result, 0)
        
        print(f"✅ time_measure(50) = {time_result:.6f} seconds")
    
    def test_algorithm_consistency(self):
        """
        Test algorithm consistency.
        
        Verifies that the same input produces the same output consistently.
        """
        # Same input should produce same result
        result1 = option_0(50)
        result2 = option_0(50)
        self.assertEqual(result1, result2)
        
        print(f"✅ Consistency test passed: option_0(50) = {result1}")


if __name__ == '__main__':
    print("Minimal Unit Tests")
    print("=" * 30)
    
    # Run tests
    unittest.main(verbosity=2, exit=False)
    
    print("\n" + "=" * 30)
    print("Tests completed! 🎉")