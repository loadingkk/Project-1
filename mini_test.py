#!/usr/bin/env python3
"""
Minimal Unit Tests - Core Functionality Only

Usage: python mini_test.py
"""

import unittest
from main import Option_0, Time_Measure


class TestCore(unittest.TestCase):
    """Test core functionality"""
    
    def test_algorithm_basic(self):
        """Test basic algorithm functionality"""
        # Test edge cases
        self.assertEqual(Option_0(1), 0)
        self.assertEqual(Option_0(2), 0)
        
        # Test normal cases
        result = Option_0(100)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)
        
        print(f"✅ Option_0(100) = {result}")
    
    def test_time_measurement(self):
        """Test time measurement functionality"""
        time_result = Time_Measure(50, trials=3)
        self.assertIsInstance(time_result, float)
        self.assertGreater(time_result, 0)
        
        print(f"✅ Time_Measure(50) = {time_result:.6f} seconds")
    
    def test_algorithm_consistency(self):
        """Test algorithm consistency"""
        # Same input should produce same result
        result1 = Option_0(50)
        result2 = Option_0(50)
        self.assertEqual(result1, result2)
        
        print(f"✅ Consistency test passed: Option_0(50) = {result1}")


if __name__ == '__main__':
    print("Minimal Unit Tests")
    print("=" * 30)
    
    # Run tests
    unittest.main(verbosity=2, exit=False)
    
    print("\n" + "=" * 30)
    print("Tests completed! 🎉")