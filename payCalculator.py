def calculatePay():
    # This first line is provided for you

    # Inputs
    total_hours = input("Enter total hours: ")
    total_hours = float(total_hours)

    hourly_rate = input("Enter hourly rate: ")
    hourly_rate = float(hourly_rate)

    # Logic for overtime pay
    if total_hours > 40:
        overtime = total_hours - 40
        normal_hours = 40

        otpay = overtime * hourly_rate * 1.5
        regpay = normal_hours * hourly_rate

        gross_pay = otpay + regpay

    # Without overtime    
    else:
        gross_pay = total_hours * hourly_rate
    
    print(f"Pay: {gross_pay}")

    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
