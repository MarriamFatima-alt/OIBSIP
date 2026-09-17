 # BMI Calculator - Task 2
# BMI Calculator - Task 2
# Oasis Infobyte Internship - Python Track

def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)"""
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def classify_bmi(bmi):
    """Classify BMI into standard health categories"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_valid_input(prompt):
    """Keep asking until user enters a valid positive number"""
    while True:
        value = input(prompt)
        try:
            value = float(value)
            if value <= 0:
                print("Error: Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number.")


def main():
    print("===== BMI Calculator =====")
    weight = get_valid_input("Enter your weight in kg: ")
    height = get_valid_input("Enter your height in meters (e.g. 1.70): ")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"\nYour BMI is: {bmi}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
