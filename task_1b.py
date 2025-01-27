# Task 1b: BMI Calculator

def calculate_bmi(weight: float, height: float) -> float:
    """Calculates the BMI of a person given their weight and height.

    Args:
        weight (float): Weight of the person in kilograms
        height (float): Height of the person in meters

    Returns:
        float: BMI of the person
    """
    
    return (weight / (height ** 2))

def weight_classification(bmi: float) -> str:
    """Determines weight classification based on BMI.

    Args:
        bmi (float): The BMI of the person

    Returns:
        str: Weight classification of person
    """
    if bmi <= 0:
        raise Exception("Invalid BMI: BMI is <= 0.")
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Dummy data
people = [
    {
        "name": "Alice",
        "weight": 50,
        "height": 11.6
    },
    {
        "name": "Bob",
        "weight": 70,
        "height": 1.8
    },
    {
        "name": "Charlie",
        "weight": 900,
        "height": 2
    }
]

for person in people:
    bmi = calculate_bmi(person["weight"], person["height"])
    classification = weight_classification(bmi)
    print(f"{person['name']} weighs {person['weight']} kilos and is {person['height']} metres tall. {person['name']}'s BMI is {bmi} which classifies them as {classification}.")