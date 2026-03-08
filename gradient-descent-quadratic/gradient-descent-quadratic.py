def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x = x0
    for __ in range(steps):
        gradient = 2 * a * x + b
        
        x = x - lr * gradient
    return float(x)
   # Write code here
    pass