def computepay(work_hours, pay_rate):
    print("Your worked for : ", str(work_hours) + "Hours", "at " + "$" + str(pay_rate) + " per Hour")
    if work_hours > 40:
        regular_pay = pay_rate * work_hours
        overtime_pay = (work_hours - 40) * (pay_rate * 0.5)
        #print(regular_pay, overtime_pay)
        wage = regular_pay + overtime_pay
       # print(wage)
    else:
        wage = work_hours * pay_rate
        #print(wage)
    return wage

wh = input("Enter Hours: ")
wr = input("Enter Rate: ")
f_wh = int(wh)
f_wr = float(wr)

#print(f_wh, f_wr)

wage = computepay(f_wh, f_wr)

print("Your Pay is: ", "$" + str(wage))

