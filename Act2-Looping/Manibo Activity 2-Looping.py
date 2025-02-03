# 1
start = int(input("Input first number: "))
end = int(input("Input last number: "))

total = 0

for i in range(start, end + 1):
    total += i

print(f"The sum of the numbers from {start} to {end} is {total}")

print()
print()

# 2
def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if check_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")