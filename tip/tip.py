n=input("Enter the bill amount: ").strip("$")
y=input("Enter the percentage amount to be tipped: ").strip("%")
n=float(n)
y=int(y)
calculated_amount=(n)*(y/100)
print(f"Leave ${calculated_amount:.2f}")

