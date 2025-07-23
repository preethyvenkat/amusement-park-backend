

def eligible_riders(riders):
    eligible = []
    for rider in riders:
        age = rider["age"]
        height = rider["height"]
        rider_name = rider["name"]
        if age >= 12 and height >= 140:
            eligible.append(rider_name)
    return eligible


riders = [
    {"name": "Alice", "age": 14, "height": 150},
    {"name": "Bob", "age": 11, "height": 145},
    {"name": "Charlie", "age": 13, "height": 135},
    {"name": "Dheera", "age": 20, "height": 160},
    {"name": "Elieana", "age": 7, "height": 112},
    {"name": "Fardeen", "age": 12, "height": 125}
]

dict_riders = eligible_riders(riders)
print("\n Riders ≥ 12 and height ≥ 140 cm:{}\n".format (dict_riders))
