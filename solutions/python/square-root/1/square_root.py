def square_root(number, tolerance=1e-10, max_iterations=1000):
    guess = number / 2  # Starting point
    for _ in range(max_iterations):#loop
        new_guess = (guess + number / guess) / 2 #newton thingy
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess
    return guess #if tolerance hasnt been reached 
    

