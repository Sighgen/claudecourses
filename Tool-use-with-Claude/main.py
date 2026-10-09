def greeting():
    print("Hi there")


def calculate_pi(digits=5):
    """
    Calculate pi to the specified number of decimal digits.
    Uses the Machin formula for efficient convergence:
    pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Args:
        digits: Number of decimal digits to calculate (default: 5)
    
    Returns:
        float: Approximation of pi
    """
    def arctan(x, num_terms):
        """Calculate arctan using Taylor series expansion"""
        result = 0
        x_squared = x * x
        x_power = x
        
        for n in range(num_terms):
            sign = (-1) ** n
            result += sign * x_power / (2 * n + 1)
            x_power *= x_squared
        
        return result
    
    # Number of terms needed for desired precision
    # More terms = more precision
    num_terms = 100 + digits * 10
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi_over_4 = 4 * arctan(1/5, num_terms) - arctan(1/239, num_terms)
    pi_approx = 4 * pi_over_4
    
    return pi_approx


def get_pi_to_5th_digit():
    """
    Convenience function to get pi to the 5th decimal digit.
    
    Returns:
        float: Pi calculated to 5 decimal places (3.14159)
    """
    return round(calculate_pi(5), 5)