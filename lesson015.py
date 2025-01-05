print("-----#1-----")
if 1 == 1:
    print(True)
else:
    print(False)

print("-----#2-----")
if 1 != 2 and 2 == 3:
    print(True)
else:
    print(False)

print("-----#3-----")
if 1 == 2 or 2 == 2:
    print(True)
else:
    print(False)

print("-----#4-----")
if (1 + 1) == 2 and (3 / 2) == 1:
    print(True)
else:
    print(False)
print()

print("-----Problem 1-----")
val = int(input("Enter a number: "))
if val < 10 or val > 20:
    print(f"{val} is valid.")
else:
    print(f"{val} is invalid.")
print()

print("-----Problem 2-----")
val = int(input("Enter a number: "))
if val >= 10 and val <= 20:
    print(f"{val} is valid.")
else:
    print(f"{val} is invalid.")
print()

print("-----Problem 2-----")
if 10 <= val <= 20:
    print(f"{val} is valid.")
else:
    print(f"{val} is invalid.")


