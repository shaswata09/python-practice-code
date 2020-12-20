largest = None
smallest = None
while True:
    num = input("Enter a Number:")
    if num == "done":
        break
    try:
        inum = int(num)
        if largest == smallest is None:
            largest = smallest = inum
        elif inum > largest:
            largest = inum
        elif inum < smallest:
            smallest = inum
    except ValueError:
        print("Invalid input")
        continue
print(f"Maximum is {largest}")
print(f"Minimum is {smallest}")
