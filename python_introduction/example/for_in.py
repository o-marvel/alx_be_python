number = [1, 2, 3, 4, 5, 6]
total = 0
count = 0

for num in number:
    total = total + num
    count += 1
    if count >= len(number):
        print(total)



for i in range(1, 11):
  # Outer loop iterates through rows (multiplication factors)
  for j in range(1, 11):
    # Inner loop iterates through columns (other factors)
    product = i * j
    print(f"{i} x {j} = {product}", end="\t")  # Print with tabs for better formatting
  print()  # Move to a new line after each row