hour = float(input("please input the hours worked\n"))
rate = 10.0

if hour <= 40:  
    pay = hour * rate
    print ("your pay is:",pay,"\n")
else:
    pay = 40 * rate + (hour-40)*10*1.5 #subtracting the overtime from the set time(40) then multiply by the rate and the 1.5 incentive

    print ("your pay is:",pay,"\n")
