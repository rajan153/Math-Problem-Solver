#!/usr/bin/env python3
"""
Test script to verify the mathematical calculations work correctly
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import TrigonometryCalculator, InterestCalculator
import math

def test_trigonometry():
    """Test trigonometry calculations"""
    print("🧮 Testing Trigonometry Calculator...")
    
    # Test case 1: 7, 24, 25 triangle (Pythagorean triplet)
    result = TrigonometryCalculator.calculate_sec_cot(7, 24, 25.0)
    
    print(f"Triangle: {result['triangle']['perpendicular']}, {result['triangle']['base']}, {result['triangle']['hypotenuse']}")
    print(f"Sec C = {result['sec_c']['numerator']}/{result['sec_c']['denominator']} = {result['sec_c']['decimal']:.3f}")
    print(f"Cot A = {result['cot_a']['numerator']}/{result['cot_a']['denominator']} = {result['cot_a']['decimal']:.3f}")
    print(f"Sec C + Cot A = {result['result']['numerator']}/{result['result']['denominator']} = {result['result']['decimal']:.3f}")
    
    # Verify the calculation
    expected = 25/24 + 7/24  # Sec C + Cot A
    actual = result['result']['decimal']
    assert abs(expected - actual) < 0.001, f"Expected {expected}, got {actual}"
    print("✅ Pythagorean triplet test passed!")
    
    # Test case 2: 5, 6 triangle (non-Pythagorean triplet)
    result2 = TrigonometryCalculator.calculate_sec_cot(5, 6, math.sqrt(61))
    
    print(f"\nTriangle: {result2['triangle']['perpendicular']}, {result2['triangle']['base']}, {result2['triangle']['hypotenuse']}")
    print(f"Sec C = {result2['sec_c']['numerator']}/{result2['sec_c']['denominator']} = {result2['sec_c']['decimal']:.3f}")
    print(f"Cot A = {result2['cot_a']['numerator']}/{result2['cot_a']['denominator']} = {result2['cot_a']['decimal']:.3f}")
    print(f"Sec C + Cot A = {result2['result']['numerator']}/{result2['result']['denominator']} = {result2['result']['decimal']:.3f}")
    
    # Verify the calculation
    expected2 = math.sqrt(61)/6 + 5/6  # Sec C + Cot A
    actual2 = result2['result']['decimal']
    assert abs(expected2 - actual2) < 0.001, f"Expected {expected2}, got {actual2}"
    print("✅ Non-Pythagorean triangle test passed!")
    print()

def test_interest():
    """Test compound interest calculations"""
    print("💰 Testing Compound Interest Calculator...")
    
    # Test case 1: Find rate
    result = InterestCalculator.find_interest_rate(12000, 20736, 3)
    
    print(f"Principal: ₹{result['ratio']['numerator']}")
    print(f"Amount: ₹{result['ratio']['denominator']}")
    print(f"Time: 3 years")
    print(f"Rate: {result['rate_percent']:.2f}%")
    print(f"Simplified ratio: {result['simplified_ratio']['numerator']}/{result['simplified_ratio']['denominator']}")
    
    # Verify the calculation
    expected_rate = 20.0  # 20%
    actual_rate = result['rate_percent']
    assert abs(expected_rate - actual_rate) < 0.1, f"Expected {expected_rate}%, got {actual_rate}%"
    print("✅ Interest rate calculation test passed!")
    
    # Test case 2: Calculate amount
    amount_result = InterestCalculator.calculate_compound_amount(12000, 20, 2)
    
    print(f"\nPrincipal: ₹{amount_result['principal']}")
    print(f"Rate: {amount_result['rate']}%")
    print(f"Time: {amount_result['time']} years")
    print(f"Amount: ₹{amount_result['amount']}")
    print(f"Interest: ₹{amount_result['interest']}")
    
    # Verify the calculation
    expected_amount = 12000 * (1.2 ** 2)  # 12000 * 1.44 = 17280
    actual_amount = amount_result['amount']
    assert abs(expected_amount - actual_amount) < 0.01, f"Expected ₹{expected_amount}, got ₹{actual_amount}"
    print("✅ Amount calculation test passed!")
    print()

def test_pythagorean_triplets():
    """Test Pythagorean triplet verification"""
    print("📐 Testing Pythagorean Triplet Verification...")
    
    # Test valid triplets
    assert TrigonometryCalculator.verify_pythagorean_triplet(3, 4, 5) == True
    assert TrigonometryCalculator.verify_pythagorean_triplet(7, 24, 25) == True
    assert TrigonometryCalculator.verify_pythagorean_triplet(5, 12, 13) == True
    
    # Test invalid triplets
    assert TrigonometryCalculator.verify_pythagorean_triplet(3, 4, 6) == False
    assert TrigonometryCalculator.verify_pythagorean_triplet(7, 24, 26) == False
    
    print("✅ Pythagorean triplet verification test passed!")
    print()

def main():
    """Run all tests"""
    print("🚀 Running Mathematical Calculation Tests\n")
    
    try:
        test_pythagorean_triplets()
        test_trigonometry()
        test_interest()
        
        print("🎉 All tests passed successfully!")
        print("\nThe backend system is ready to use!")
        print("Run 'python app.py' to start the server.")
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
