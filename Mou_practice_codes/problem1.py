try:
    score = input("Enter Score:")
    x = float(score)
    # score = int(input("Enter Score:"))    ---> You can use this single line expression too
    # print(f"Score you entered: {x}")      ---> Just for confirmation
    # print(f"Data type of x: {type(x)}")   ---> To check converted data type
    if 0 <= x <= 1:
        if x >= 0.9:
            print("A")
        elif x >= 0.8:
            print("B")
        elif x >= 0.7:
            print("C")
        elif x >= 0.6:
            print("D")
        else:
            print("F")
    else:
        raise ArithmeticError
except ArithmeticError:
    print("Sorry! Please enter a score within the range of 0 to 1")
except ValueError:
    print("Value Error occurred!")
