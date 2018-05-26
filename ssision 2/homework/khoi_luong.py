kg = float(input("ban bn kg ?"))
cm = float(input("ban cao bn cm ?"))
m = cm/100
BMI = kg/(m*m)
print("BMI = ", format(BMI,'.2f'))
if BMI <= 16:
    print("thieu can nang")
elif BMI <= 18.5:
    print("thieu can")
elif BMI <= 25:
    print("binh thuong")
elif BMI <= 30:
    print("thua can")
else:
    print("beo phi")


