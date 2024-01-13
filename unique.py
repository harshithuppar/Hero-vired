set3 = input("Enter element for first sets\n")

set4 = input("Enter element for second sets\n")

set_1  = set(set3)
set_2  = set(set4)

set = set_1.intersection(set_2)

print(f"common elements {set}")
