#!/usr/bin/env python3
"""
Demo script showing how to use the Math Problem Solver API
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def demo_trigonometry():
    """Demonstrate trigonometry calculations"""
    print("🧮 Trigonometry Calculator Demo")
    print("=" * 50)
    
    # Example 1: 7, 24, 25 triangle
    print("\nExample 1: Triangle with sides 7, 24, 25")
    response = requests.post(f"{BASE_URL}/trigonometry", 
                           json={"perpendicular": 7, "base": 24})
    
    if response.status_code == 200:
        data = response.json()
        print(f"Triangle dimensions: {data['triangle']['perpendicular']}, {data['triangle']['base']}, {data['triangle']['hypotenuse']}")
        print(f"Sec C = {data['sec_c']['numerator']}/{data['sec_c']['denominator']} = {data['sec_c']['decimal']:.3f}")
        print(f"Cot A = {data['cot_a']['numerator']}/{data['cot_a']['denominator']} = {data['cot_a']['decimal']:.3f}")
        print(f"Sec C + Cot A = {data['result']['numerator']}/{data['result']['denominator']} = {data['result']['decimal']:.3f}")
    else:
        print(f"Error: {response.json()}")
    
    # Example 2: 3, 4, 5 triangle
    print("\nExample 2: Triangle with sides 3, 4, 5")
    response = requests.post(f"{BASE_URL}/trigonometry", 
                           json={"perpendicular": 3, "base": 4})
    
    if response.status_code == 200:
        data = response.json()
        print(f"Triangle dimensions: {data['triangle']['perpendicular']}, {data['triangle']['base']}, {data['triangle']['hypotenuse']}")
        print(f"Sec C = {data['sec_c']['numerator']}/{data['sec_c']['denominator']} = {data['sec_c']['decimal']:.3f}")
        print(f"Cot A = {data['cot_a']['numerator']}/{data['cot_a']['denominator']} = {data['cot_a']['decimal']:.3f}")
        print(f"Sec C + Cot A = {data['result']['numerator']}/{data['result']['denominator']} = {data['result']['decimal']:.3f}")
    else:
        print(f"Error: {response.json()}")

def demo_compound_interest():
    """Demonstrate compound interest calculations"""
    print("\n💰 Compound Interest Calculator Demo")
    print("=" * 50)
    
    # Example 1: Find interest rate
    print("\nExample 1: Find interest rate")
    print("Given: Principal = ₹12,000, Amount = ₹20,736, Time = 3 years")
    
    response = requests.post(f"{BASE_URL}/interest/rate", 
                           json={"principal": 12000, "amount": 20736, "time": 3})
    
    if response.status_code == 200:
        data = response.json()
        print(f"Interest Rate: {data['rate_percent']:.2f}%")
        print(f"Simplified ratio: {data['simplified_ratio']['numerator']}/{data['simplified_ratio']['denominator']}")
        print(f"Rate fraction: {data['rate_fraction']['numerator']}/{data['rate_fraction']['denominator']}")
    else:
        print(f"Error: {response.json()}")
    
    # Example 2: Calculate amount for 2 years
    print("\nExample 2: Calculate amount for 2 years at 20% rate")
    response = requests.post(f"{BASE_URL}/interest/amount", 
                           json={"principal": 12000, "rate": 20, "time": 2})
    
    if response.status_code == 200:
        data = response.json()
        print(f"Principal: ₹{data['principal']}")
        print(f"Rate: {data['rate']}%")
        print(f"Time: {data['time']} years")
        print(f"Amount: ₹{data['amount']}")
        print(f"Interest: ₹{data['interest']}")
    else:
        print(f"Error: {response.json()}")

def demo_web_interface():
    """Show web interface URLs"""
    print("\n🌐 Web Interface Demo")
    print("=" * 50)
    print("The system provides a beautiful web interface:")
    print(f"• Main page: {BASE_URL}/")
    print(f"• Trigonometry calculator: {BASE_URL}/template1")
    print(f"• Compound interest calculator: {BASE_URL}/template2")
    print("\nFeatures:")
    print("• Interactive input forms")
    print("• Real-time calculations")
    print("• Step-by-step solutions")
    print("• Professional mathematical layouts")
    print("• Error handling and validation")

def main():
    """Run the complete demo"""
    print("🚀 Math Problem Solver - API Demo")
    print("=" * 60)
    
    try:
        # Check if server is running
        response = requests.get(f"{BASE_URL}/")
        if response.status_code != 200:
            print("❌ Server is not running. Please start the server with: python app.py")
            return
        
        print("✅ Server is running successfully!")
        
        # Run demos
        demo_trigonometry()
        demo_compound_interest()
        demo_web_interface()
        
        print("\n🎉 Demo completed successfully!")
        print("\nTo use the system:")
        print("1. Open your browser and go to http://localhost:5000")
        print("2. Choose either Trigonometry or Compound Interest calculator")
        print("3. Enter your values and get instant calculations!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Please make sure the server is running:")
        print("   python app.py")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
