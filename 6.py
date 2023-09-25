def count_factors(n):
    factors = []  # Initialize an empty list to store factors
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)  # Append factors to the list
    return factors

def has_four_distinct_factors(num):
    factors = count_factors(num)
    distinct_factors = set(factors)  # Use a set to eliminate duplicates
    return len(distinct_factors) == 4
    

# Input number
input_num = int(input("Enter a number: "))

factors = count_factors(input_num)

if has_four_distinct_factors(input_num):
    print(f"{input_num} has exactly 4 distinct factors:")
    print("Factors:", factors)
    
else:
    print(f"{input_num} does not have exactly 4 distinct factors.")
