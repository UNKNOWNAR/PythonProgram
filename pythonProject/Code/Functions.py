def calculate(exp):
    total = 0
    for item in exp:
        total += item;
    return total
A = [36,41,25,30]
B = [64,43,20,12]
print("Sum of A",calculate(A))
print("Sum of B",calculate(B))
