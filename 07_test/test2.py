def BMI():
    mass = int(input("Enter your mass:"))
    height =int(input("Enter your height:"))
    BMI = mass/(height*height)
    if BMI < 15:
        print("severely underweight")
    elif 15 <= BMI < 16:
        print("Underweight")
    elif 16 <= BMI < 18.5:
        print("Normal")
    elif 18.5 <= BMI < 25:
        print("Overweight")
    elif 25 <= BMI < 30:
        print("Obese Class I")
    elif 30 <= BMI < 35:
        print("Obese class II")
    elif 35 <= BMI < 40:
        print("Obese Class III")
    else:
        print("Very severely underweight")


if __name__ == '__main__':
    BMI()
