a = input("Enter the Number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range (1, 11):
       print(f"{int(a)} x {i} = {int(a)*i}")

except Exception as e:
    print("Invalid Input!")
    print("Sorry Please Enter The Number Only")

print("Some imp lines of code")
print("End of program")