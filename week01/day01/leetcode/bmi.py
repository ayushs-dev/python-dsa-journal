# BMI Calculator
# https://leetcode.com/problems/bmi-calculator/
# Problem: Calculate BMI (Body Mass Index)
# Formula: BMI = weight(kg) / height(m)²


# def bmi():
#     weight = float(input("Enter weight in kg: "))
#     height = float(input("Enter height in meters: "))
#     bmi_val = weight / (height**2)
#     print(f"Your BMI is: {bmi_val:.2f}")



def bmi(weight, height):
    bmi_val = weight / (height**2)
    return round(bmi_val, 2)