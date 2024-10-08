def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    return celsius + 273.15

def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    return (celsius * 9/5) + 32

def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius"""
    return (fahrenheit - 32) * 5/9

def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvins"""
    return (fahrenheit - 32) * 5/9 + 273.15

def convertKelvinToCelsius(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius"""
    return kelvin - 273.15

def convertKelvinToFahrenheit(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Fahrenheit"""
    return (kelvin - 273.15) * 9/5 + 32

class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    # Dictionary that holds conversion logic for temperature and distance units.
    # Each unit has nested dictionaries for other units it can convert to.
    # The conversion is done using lambda functions for each unit pair.

    conversions = {
        # Celsius conversions: 
        # To Kelvin: Add 273.15, 
        # To Fahrenheit: Multiply by 9/5, then add 32
        # Celsius to Celsius is just an identity function
        "Celsius": {
            "Kelvin": lambda x: x + 273.15,
            "Fahrenheit": lambda x: (x * 9/5) + 32,
            "Celsius": lambda x: x
        },

        # Kelvin conversions: 
        # To Celsius: Subtract 273.15,
        # To Fahrenheit: Subtract 273.15, then multiply by 9/5 and add 32
        "Kelvin": {
            "Celsius": lambda x: x - 273.15,
            "Fahrenheit": lambda x: (x - 273.15) * 9/5 + 32,
            "Kelvin": lambda x: x  # Identity function for same unit conversion
        },

        # Fahrenheit conversions: 
        # To Celsius: Subtract 32, then multiply by 5/9
        # To Kelvin: Same as above, but add 273.15 at the end
        "Fahrenheit": {
            "Celsius": lambda x: (x - 32) * 5/9,
            "Kelvin": lambda x: (x - 32) * 5/9 + 273.15,
            "Fahrenheit": lambda x: x
        },

        # Miles conversions: 
        # To Yards: Multiply by 1760, 
        # To Meters: Multiply by 1609.34
        "Miles": {
            "Yards": lambda x: x * 1760,
            "Meters": lambda x: x * 1609.34,
            "Miles": lambda x: x
        },

        # Yards conversions: 
        # To Miles: Divide by 1760, 
        # To Meters: Divide by 1.09361
        "Yards": {
            "Miles": lambda x: x / 1760,
            "Meters": lambda x: x / 1.09361,
            "Yards": lambda x: x
        },

        # Meters conversions: 
        # To Miles: Divide by 1609.34, 
        # To Yards: Multiply by 1.09361
        "Meters": {
            "Miles": lambda x: x / 1609.34,
            "Yards": lambda x: x * 1.09361,
            "Meters": lambda x: x
        }
    }

    # Check if the provided 'fromUnit' and 'toUnit' are valid (i.e., present in the conversion dictionary).
    # If either of them is invalid, raise an exception (ConversionNotPossible).
    if fromUnit not in conversions or toUnit not in conversions[fromUnit]:
        raise ConversionNotPossible(f"Cannot convert {fromUnit} to {toUnit}")

    # If valid, perform the conversion by calling the appropriate lambda function
    # using the conversion formula and return the result.
    return conversions[fromUnit][toUnit](value)