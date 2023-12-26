def convert_length(value, source_unit, target_unit):
    # Conversion factors
    meters_to_feet = 3.28084

    try:
        # Convert user input to float
        value = float(value)

        # Perform the conversion
        if source_unit.lower() == 'meters' and target_unit.lower() == 'feet':
            result = value * meters_to_feet
            return result
        elif source_unit.lower() == 'feet' and target_unit.lower() == 'meters':
            result = value / meters_to_feet
            return result
        else:
            return "Unsupported units. Please choose meters or feet."

    except ValueError:
        return "Invalid input. Please enter a numeric value."

# User input
value = input("Enter the value to convert: ")
source_unit = input("Enter the source unit (meters or feet): ")
target_unit = input("Enter the target unit (meters or feet): ")

# Perform the conversion and handle errors
result = convert_length(value, source_unit, target_unit)
print(f"Result: {result} {target_unit.capitalize()}" if isinstance(result, float) else f"Error: {result}")

