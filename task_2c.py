# Task 2c

array_a = {
    "Red": "#FF0000",
    "White": "#FFFFFF",
    "Green": "#008000",
    "Blue": "#0000FF",
}

array_b = [
    22.7,
    28.5,
    22.1,
]

# Iterate over array_a
for (key, colour) in array_a.items():
    print(key, colour)
    
# Iterate over array_b
for (i, number) in enumerate(array_b):
    print(i, number)