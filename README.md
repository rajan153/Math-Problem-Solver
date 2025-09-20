# Math Problem Solver Backend

A Flask-based backend system that provides interactive calculators for Trigonometry and Compound Interest problems, integrated with beautiful frontend templates.

## Features

### 🧮 Trigonometry Calculator (Template 1)

- Calculate Sec C + Cot A for any right triangle
- Works with both Pythagorean triplets and non-integer hypotenuses
- Interactive triangle diagram with dynamic dimensions
- Step-by-step solution display
- Fraction-based calculations for precise results
- Automatic hypotenuse calculation using Pythagorean theorem

### 💰 Compound Interest Calculator (Template 2)

- Find interest rates from principal, amount, and time
- Calculate compound amounts for any time period
- Detailed step-by-step calculations
- Fraction simplification for rate factors
- Professional mathematical layout

## Installation

1. **Clone or download the project**

   ```bash
   cd /home/rajan/Downloads/Backend/project
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**

   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser and go to: `http://localhost:5000`
   - Or access directly: `http://0.0.0.0:5000`

## API Endpoints

### Trigonometry

- **POST** `/trigonometry`
  - Input: `{"perpendicular": 7, "base": 24}`
  - Output: Complete trigonometry calculations with fractions

### Compound Interest

- **POST** `/interest/rate`

  - Input: `{"principal": 12000, "amount": 20736, "time": 3}`
  - Output: Interest rate calculation with steps

- **POST** `/interest/amount`
  - Input: `{"principal": 12000, "rate": 20, "time": 2}`
  - Output: Compound amount calculation

## Usage Examples

### Trigonometry Problem

1. Go to `http://localhost:5000/template1`
2. Enter perpendicular and base values
3. Get instant calculation of Sec C + Cot A
4. View step-by-step solution with triangle diagram

### Compound Interest Problem

1. Go to `http://localhost:5000/template2`
2. Enter principal, amount, and time values
3. Specify calculation time period
4. Get complete solution with rate finding and amount calculation

## Project Structure

```
project/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── index.html        # Main landing page
│   ├── template1.html    # Trigonometry calculator
│   └── template2.html    # Compound interest calculator
├── static/               # Static assets
│   ├── arrow.png         # Arrow image for templates
│   └── interesticon.png  # Interest calculator icon
└── README.md            # This file
```

## Technical Details

### Backend Features

- **Flask Framework**: Lightweight and flexible web framework
- **CORS Support**: Cross-origin resource sharing enabled
- **Fraction Calculations**: Precise mathematical calculations using Python's fractions module
- **Input Validation**: Comprehensive error handling and validation
- **RESTful API**: Clean API design for frontend integration

### Frontend Features

- **Responsive Design**: Works on desktop and mobile devices
- **Interactive Forms**: Real-time input validation
- **Dynamic Updates**: Live calculation updates without page refresh
- **Professional Layout**: Maintains original template styling
- **Error Handling**: User-friendly error messages

### Mathematical Accuracy

- **Pythagorean Triplets**: Automatic verification of right triangle properties
- **Fraction Arithmetic**: Exact calculations without floating-point errors
- **Compound Interest**: Precise rate calculations using nth root methods
- **Step-by-Step Solutions**: Detailed mathematical breakdowns

## Sample Problems

### Trigonometry Example

- **Input**: Perpendicular = 7, Base = 24
- **Output**: Sec C + Cot A = 4/3
- **Verification**: 7, 24, 25 is a Pythagorean triplet

**Non-Pythagorean Example:**

- **Input**: Perpendicular = 5, Base = 6
- **Output**: Sec C + Cot A = 1834/859 ≈ 2.135
- **Hypotenuse**: √61 ≈ 7.81 (automatically calculated)

### Compound Interest Example

- **Input**: Principal = ₹12,000, Amount = ₹20,736, Time = 3 years
- **Output**: Rate = 20%, Amount in 2 years = ₹17,280

## Development

To extend the system:

1. **Add new calculation types**: Extend the calculator classes in `app.py`
2. **Create new templates**: Add HTML files in the `templates/` directory
3. **Add new endpoints**: Create new routes in the Flask application
4. **Enhance frontend**: Modify JavaScript functions in the templates

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py` (line: `app.run(port=5001)`)
2. **Missing dependencies**: Run `pip install -r requirements.txt`
3. **Images not loading**: Ensure images are in the `static/` directory
4. **CORS errors**: The application includes CORS support by default

### Error Messages

- **"Not a valid right triangle"**: The entered dimensions don't form a Pythagorean triplet
- **"Amount must be greater than principal"**: Invalid compound interest input
- **"All values must be positive"**: Negative or zero values entered

## License

This project is created for educational and demonstration purposes.
