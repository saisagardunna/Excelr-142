# Input a positive integer n
n = int(input("Enter a positive integer: "))

# Calculate the sum of all even numbers between 1 and n
even_sum = sum(i for i in range(2, n + 1, 2))

# Output the result
print(f"The sum of all even numbers between 1 and {n} is: {even_sum}")
