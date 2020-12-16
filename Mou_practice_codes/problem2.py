try:
    hours = float(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))

    if hours <= 40:
        grossPay = hours*rate
    else:
        grossPay = 40*rate + (hours-40)*(rate*1.5)

    print(f"Gross Pay: {grossPay}")
except ValueError:
    print("Value Error occurred!")