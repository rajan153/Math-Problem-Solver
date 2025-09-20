from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import math
import fractions
from typing import Dict, List, Tuple, Optional

app = Flask(__name__)
CORS(app)

class TrigonometryCalculator:
    """Handles trigonometry calculations including Pythagorean triplets"""
    
    @staticmethod
    def find_pythagorean_triplet(a: int, b: int) -> Optional[Tuple[int, int, int]]:
        """Find Pythagorean triplet given two sides"""
        c_squared = a*a + b*b
        c = int(math.sqrt(c_squared))
        
        if c*c == c_squared:
            return (a, b, c)
        return None
    
    @staticmethod
    def calculate_sec_cot(perpendicular: int, base: int, hypotenuse: float) -> Dict:
        """Calculate Sec C + Cot A for a right triangle"""
        # Sec C = Hypotenuse / Base
        sec_c_decimal = hypotenuse / base
        
        # Cot A = Perpendicular / Base  
        cot_a_decimal = perpendicular / base
        
        # Sec C + Cot A
        result_decimal = sec_c_decimal + cot_a_decimal
        
        # Convert to fractions for display
        sec_c = fractions.Fraction(sec_c_decimal).limit_denominator(1000)
        cot_a = fractions.Fraction(cot_a_decimal).limit_denominator(1000)
        result = fractions.Fraction(result_decimal).limit_denominator(1000)
        
        return {
            'sec_c': {
                'numerator': sec_c.numerator,
                'denominator': sec_c.denominator,
                'decimal': sec_c_decimal
            },
            'cot_a': {
                'numerator': cot_a.numerator,
                'denominator': cot_a.denominator,
                'decimal': cot_a_decimal
            },
            'result': {
                'numerator': result.numerator,
                'denominator': result.denominator,
                'decimal': result_decimal
            },
            'triangle': {
                'perpendicular': perpendicular,
                'base': base,
                'hypotenuse': round(hypotenuse, 2)
            }
        }
    
    @staticmethod
    def verify_pythagorean_triplet(a: int, b: int, c: int) -> bool:
        """Verify if three numbers form a Pythagorean triplet"""
        return a*a + b*b == c*c

class InterestCalculator:
    """Handles compound interest calculations"""
    
    @staticmethod
    def find_interest_rate(principal: float, amount: float, time: int) -> Dict:
        """Find the rate of interest given principal, amount, and time"""
        # A = P(1 + r/100)^t
        # (1 + r/100)^t = A/P
        # 1 + r/100 = (A/P)^(1/t)
        # r/100 = (A/P)^(1/t) - 1
        # r = 100 * ((A/P)^(1/t) - 1)
        
        ratio = amount / principal
        rate_decimal = ratio**(1/time) - 1
        rate_percent = rate_decimal * 100
        
        # Convert to fraction for display
        rate_fraction = fractions.Fraction(rate_decimal).limit_denominator(1000)
        
        return {
            'rate_percent': round(rate_percent, 2),
            'rate_decimal': rate_decimal,
            'rate_fraction': {
                'numerator': rate_fraction.numerator,
                'denominator': rate_fraction.denominator
            },
            'ratio': {
                'numerator': int(amount),
                'denominator': int(principal)
            },
            'simplified_ratio': InterestCalculator._simplify_ratio(int(amount), int(principal)),
            'calculation_steps': InterestCalculator._get_rate_calculation_steps(principal, amount, time, rate_percent)
        }
    
    @staticmethod
    def calculate_compound_amount(principal: float, rate: float, time: int) -> Dict:
        """Calculate compound amount"""
        amount = principal * (1 + rate/100)**time
        interest = amount - principal
        
        return {
            'principal': principal,
            'rate': rate,
            'time': time,
            'amount': round(amount, 2),
            'interest': round(interest, 2),
            'calculation_steps': InterestCalculator._get_amount_calculation_steps(principal, rate, time)
        }
    
    @staticmethod
    def _simplify_ratio(num: int, den: int) -> Dict:
        """Simplify a ratio to its lowest terms"""
        gcd_val = math.gcd(num, den)
        return {
            'numerator': num // gcd_val,
            'denominator': den // gcd_val
        }
    
    @staticmethod
    def _get_rate_calculation_steps(principal: float, amount: float, time: int, rate: float) -> List[Dict]:
        """Get step-by-step calculation for rate finding"""
        steps = []
        
        # Step 1: Basic equation
        steps.append({
            'step': 1,
            'equation': f"{int(principal)} = P[1 + r/100]^{time} = {int(amount)}",
            'description': "Given equation"
        })
        
        # Step 2: Isolate the bracket
        ratio = amount / principal
        steps.append({
            'step': 2,
            'equation': f"[1 + r/100]^{time} = {int(amount)}/{int(principal)}",
            'description': "Isolate the bracket term"
        })
        
        # Step 3: Simplify ratio
        simplified = InterestCalculator._simplify_ratio(int(amount), int(principal))
        steps.append({
            'step': 3,
            'equation': f"[1 + r/100]^{time} = {simplified['numerator']}/{simplified['denominator']}",
            'description': "Simplify the ratio"
        })
        
        # Step 4: Take nth root
        steps.append({
            'step': 4,
            'equation': f"1 + r/100 = ({simplified['numerator']}/{simplified['denominator']})^(1/{time})",
            'description': f"Take {time}th root"
        })
        
        # Step 5: Calculate r
        steps.append({
            'step': 5,
            'equation': f"r = {round(rate, 2)}%",
            'description': "Calculate rate"
        })
        
        return steps
    
    @staticmethod
    def _get_amount_calculation_steps(principal: float, rate: float, time: int) -> List[Dict]:
        """Get step-by-step calculation for amount calculation"""
        steps = []
        
        # Step 1: Formula
        steps.append({
            'step': 1,
            'equation': f"A = {int(principal)}[1 + {rate}/100]^{time}",
            'description': "Compound interest formula"
        })
        
        # Step 2: Calculate rate factor
        rate_factor = 1 + rate/100
        steps.append({
            'step': 2,
            'equation': f"A = {int(principal)} × {rate_factor}^{time}",
            'description': "Calculate rate factor"
        })
        
        # Step 3: Final calculation
        amount = principal * (rate_factor**time)
        steps.append({
            'step': 3,
            'equation': f"A = {round(amount, 2)}",
            'description': "Final amount"
        })
        
        return steps

# API Routes

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/trigonometry', methods=['POST'])
def calculate_trigonometry():
    """Calculate trigonometry values"""
    try:
        data = request.get_json()
        perpendicular = int(data.get('perpendicular', 7))
        base = int(data.get('base', 24))
        
        # Find hypotenuse using Pythagorean theorem
        hypotenuse_squared = perpendicular**2 + base**2
        hypotenuse = math.sqrt(hypotenuse_squared)
        
        # Allow any valid right triangle (not just integer sides)
        result = TrigonometryCalculator.calculate_sec_cot(perpendicular, base, hypotenuse)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/interest/rate', methods=['POST'])
def find_interest_rate():
    """Find interest rate from principal, amount, and time"""
    try:
        data = request.get_json()
        principal = float(data.get('principal', 12000))
        amount = float(data.get('amount', 20736))
        time = int(data.get('time', 3))
        
        if principal <= 0 or amount <= 0 or time <= 0:
            return jsonify({'error': 'All values must be positive'}), 400
        
        result = InterestCalculator.find_interest_rate(principal, amount, time)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/interest/amount', methods=['POST'])
def calculate_compound_amount():
    """Calculate compound amount"""
    try:
        data = request.get_json()
        principal = float(data.get('principal', 12000))
        rate = float(data.get('rate', 20))
        time = int(data.get('time', 2))
        
        if principal <= 0 or rate < 0 or time <= 0:
            return jsonify({'error': 'Invalid input values'}), 400
        
        result = InterestCalculator.calculate_compound_amount(principal, rate, time)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/template1')
def template1():
    """Serve Template 1 (Trigonometry)"""
    return render_template('template1.html')

@app.route('/template2')
def template2():
    """Serve Template 2 (Compound Interest)"""
    return render_template('template2.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
