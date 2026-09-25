units = int(input("enter electricty units:"))
if units <=100:
    bill =((50* 1.95)+(units-50)*3.10)
elif units <= 145:
    bill = (100 * 3.40) + ((units - 100) * 3.40)
elif units <= 225:
    bill = (200 * 5.10) + ((units - 200) * 7.70)
elif units <= 475:
    bill = (200 * 5.10) + (99 * 7.7) + (99 * 9.00) + (77 * 9.5)
print("your bill is ",bill)
