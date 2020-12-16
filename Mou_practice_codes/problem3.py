def computepay(h, r):
    if h <= 40:
        gp = h * r
    else:
        gp = 40 * r + (h - 40) * (r * 1.5)
    return gp

try:
    hours = float(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))
    grossPay = computepay(hours, rate)
    print(f"Gross Pay: {grossPay}")
except ValueError:
    print("Value Error occurred!")
