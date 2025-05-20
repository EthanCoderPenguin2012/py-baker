# Pie Baker

This project bakes up Pi to an arbitrary number of decimal places using the Gauss-Legendre recipe and Python's `decimal` kitchen scale.

## Features
- Bake Pi to millions of digits (limited by your kitchen's memory and oven power)
- Uses the high-precision Gauss-Legendre recipe
- User input for how many digits to bake
- Taste test (verification) of your pie's length

## Usage

1. **Gather your ingredients**
   ```bash
   pip install -r requirements.txt
   ```

2. **Preheat the oven and start baking**
   ```bash
   python oven.py
   ```
   Enter how many digits of Pi you want to bake when prompted.

   > **Chef's Note:** Baking millions of digits requires a lot of kitchen space (RAM) and time. For 20,000,000 digits, make sure you have at least 10GB of RAM and plenty of patience.

3. **Serving**
   - The script serves up Pi to the number of decimal places you ordered.
   - It also taste-tests (verifies) the number of digits in your pie.

## Example
```
How many do you want to bake?
1000
Baking 1000 pies...

Baked 1000Pi:
3.1415926535... (continues for 1000 digits)

Number of digits baked after decimal point: 1000
Taste test successful: Your pie has the correct number of decimal places!
```

## Kitchen Tips
- For extra-large pies, consider serving to a file:
  ```bash
  python oven.py > pi_20million.txt
  ```
- The script uses the `decimal` kitchen scale for precise measurements.
- The number of recipe steps (iterations) in the Gauss-Legendre method is fixed for practicality, but you can add more for even finer pies.

## License
MIT (Make It Tasty!)
