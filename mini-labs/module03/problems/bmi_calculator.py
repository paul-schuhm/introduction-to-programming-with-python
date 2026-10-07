# This program computes Body Mass Index based on user's data.
# @see https://en.wikipedia.org/wiki/Body_mass_index
"""
Computes BMI and returns a full report (index and interpretation)
"""
def compute_bmi(height_cm, weight_kg):
    bmi = weight / ((height / 100) ** 2)
    description = None;
    if (bmi < 16):
        description = "Severe thickness"
    elif (bmi > 16 and bmi < 18.5):
        description = "Underweight"
    elif (bmi > 18.5 and bmi < 25):
        description = "Normal"
    elif (bmi > 25 and bmi < 30):
        description = "Overweight"
    elif (bmi > 30):
        description = "Obese"
    # We return a dictionary containing all relevant information for the caller
    return {"index": bmi, "description": description}

print("BMI Calculator. Please give the following information")

# Ask for user data (height and weight)
# Don't forget to convert data (string) to numbers!
height = float(input("Enter your height (cm): "))
weight = float(input("Enter your weight (kg): "))

# Let's use your nice function here
report = compute_bmi(height, weight)

# Finally, print the report data
print(f"BMI: {report['index']}")
print(f"Description: {report['description']}")
