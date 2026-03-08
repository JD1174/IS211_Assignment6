class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    """
    Converts a value from one unit to another.
    Supports Temperatures: Celsius, Fahrenheit, Kelvin
    Supports Distances: Miles, Yards, Meters
    """
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    distance_units =["Miles", "Yards", "Meters"]

    # --- Temperature Conversions ---
    if fromUnit in temperature_units and toUnit in temperature_units:
        # Step 1: Convert fromUnit to Base Unit (Celsius)
        if fromUnit == "Celsius":
            base_val = value
        elif fromUnit == "Fahrenheit":
            base_val = (value - 32) * 5 / 9
        elif fromUnit == "Kelvin":
            base_val = value - 273.15

        # Step 2: Convert Base Unit (Celsius) to toUnit
        if toUnit == "Celsius":
            return float(base_val)
        elif toUnit == "Fahrenheit":
            return float((base_val * 9 / 5) + 32)
        elif toUnit == "Kelvin":
            return float(base_val + 273.15)

    # --- Distance Conversions ---
    elif fromUnit in distance_units and toUnit in distance_units:
        # Step 1: Convert fromUnit to Base Unit (Meters)
        if fromUnit == "Meters":
            base_val = value
        elif fromUnit == "Miles":
            base_val = value * 1609.34
        elif fromUnit == "Yards":
            base_val = value * 0.9144  # 1 Yard is precisely 0.9144 Meters

        # Step 2: Convert Base Unit (Meters) to toUnit
        if toUnit == "Meters":
            return float(base_val)
        elif toUnit == "Miles":
            return float(base_val / 1609.34)
        elif toUnit == "Yards":
            return float(base_val / 0.9144)

    # --- Incompatible or Unknown Units ---
    else:
        raise ConversionNotPossible(f"Cannot convert {fromUnit} to {toUnit}")