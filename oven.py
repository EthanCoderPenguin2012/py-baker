from decimal import Decimal, getcontext

def calculate_pi_gauss_legendre(num_digits):
    if not isinstance(num_digits, int) or num_digits < 0:
        raise ValueError("Number of digits must be a non-negative integer.")

    # Set the precision for decimal calculations.
    # We need num_digits + 1 (for the '3' before the decimal) + a few guard digits
    # for intermediate calculations to ensure accuracy of the final digit.
    # Let's use 5 guard digits.
    precision = num_digits + 1 + 5
    getcontext().prec = precision

    # Initialize constants for Gauss-Legendre algorithm
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)

    pi_old = Decimal(0) # To check for convergence, though iterations are usually fixed

    # The number of iterations needed is roughly log2(precision).
    # For ~1000 digits, log2(1000) is about 10.
    # 15-20 iterations are more than enough for this many digits.
    # Each iteration roughly doubles the number of correct digits.
    num_iterations = 0
    # Heuristic for iterations: int(math.log2(precision)) + 2 could be used if math was imported.
    # For practical purposes, 15-20 iterations is ample for thousands of digits.
    # Let's use a number of iterations that ensures convergence for the requested digits.
    # For ~1000 digits (precision ~1006), ~10 iterations are mathematically needed.
    # Let's do a few more to be safe.
    for i in range(15): # Sufficient for thousands of digits
        num_iterations += 1
        a_next = (a + b) / 2
        b_next = (a * b).sqrt()
        t_next = t - p * (a - a_next)**2
        p_next = 2 * p

        a, b, t, p = a_next, b_next, t_next, p_next

        pi_new = (a + b)**2 / (4 * t)

        # Optional: Check if pi has converged to the required precision
        # This is more useful if you don't have a fixed number of iterations
        # if pi_new == pi_old:
        #     break
        pi_old = pi_new
        # print(f"Iteration {i+1}: Pi approx {pi_new}") # For debugging

    # The result from the formula is Pi with 'precision' significant digits.
    # We want to return it, and the formatting will happen during printing.
    return pi_new

if __name__ == "__main__":
    
    digits_after_decimal = int(input("How much pie do you want? "))

    print(f"\nMixing ingredients for a {digits_after_decimal}-digit pie...")
    pi_value = calculate_pi_gauss_legendre(digits_after_decimal)

    # Format the output to show the desired number of decimal places
    formatted_pi = f"{pi_value:.{digits_after_decimal}f}"

    print(f"\n🥧 Your {digits_after_decimal} Pies are ready! 🥧\n")
    print(formatted_pi)

    # Clear the bakedfood.txt file before baking
    with open("bakedfood.txt", "w") as f:
        pass

    # Save the baked Pi to a file
    with open("bakedfood.txt", "w") as f:
        f.write(formatted_pi)
    print(f"\n(Pi has been served in 'bakedfood.txt' for your enjoyment!)")

    # Taste test (verification)
    actual_digits_printed = len(formatted_pi.split('.')[1])
    print(f"\nTaste test: Number of digits after the decimal point: {actual_digits_printed}")
    if actual_digits_printed == digits_after_decimal:
        print("Delicious! Your pie has the perfect number of digits. 😋")
    else:
        print("Oops! This pie is a little off. Back to the kitchen!")

