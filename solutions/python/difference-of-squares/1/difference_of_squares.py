def square_of_sum(N):
    total = sum(range(1, N+1))  # 1 + 2 + ... + N
    return total ** 2            #square of sum

def sum_of_squares(N):
    return sum(i**2 for i in range(1, N+1))  # 1² + 2² + ... + N²

def difference_of_squares(N):
    return square_of_sum(N) - sum_of_squares(N)