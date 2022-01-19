"""
Build an automatic pizza order program.
The program has to work out the final bill based on a user's order.
"""
print("Welcome to pizza order.")
size = input("Choose a size (s/m/l): ")
pepperoni = input("Add pepperoni (y/n)?: ")
cheese = input("Extra cheese (y/n)?: ")
pizza, ch, pep = 0, 0, 0
if size.lower() == "s":
    pizza += 15
elif size.lower() == "m":
    pizza += 20
elif size.lower() == "l":
    pizza += 25
if pepperoni.lower() == "y":
    if size.lower() == "m" or size.lower() == "l":
        pep += 3
    else:
        pep += 2
if cheese.lower() == "y":
    ch += 1
print(f"BILL:\n"
      f"Pizza: ${pizza:.2f}\n"
      f"Extra Pepperoni: ${pep:.2f}\n"
      f"Extra Cheese: ${ch:.2f}\n"
      f"Total: ${pizza+pep+ch:.2f}")
