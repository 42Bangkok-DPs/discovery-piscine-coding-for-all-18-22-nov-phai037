num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = num1 * num2
if result > 0:
    print(f"{num1} x {num2} is {result},The result is positive.")  
elif result < 0:
    print(f"{num1} x {num2} is {result},The result is negative.")  
else:
    print(f"{num1} x {num2} is {result}, The result is  negative and positive (zero).")  