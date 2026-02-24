print("BMI calculator")
weight=float(input("Enter your weight(kg)"))
height=float(input("Enter your height(cm)"))
bmi=weight/(height/100)**2
if bmi<=18.4:
    print("you are underweight bmi=",bmi)
elif bmi<=24.9:
    print("You are fit bmi=",bmi)
elif bmi<=29.9:
    print("You are overweight bmi=",bmi)
elif bmi<=34.9:
    print("You are overweight bmi=",bmi)
else:
    print("you are obese bmi=",bmi)




