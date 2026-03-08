import unittest

# Importing the basic conversion functions
from conversions import (
    convertCelsiusToKelvin, 
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit
)

from conversions_refactored import convert, ConversionNotPossible

class TestBasicConversions(unittest.TestCase):
    """Test cases for Part I, II, and III basic conversion functions"""

    def test_convertCelsiusToKelvin(self):
        test_cases =[(300.00, 573.15), (0.00, 273.15), (-273.15, 0.00), (100.00, 373.15), (-100.00, 173.15)]
        for celsius, expected in test_cases:
            result = convertCelsiusToKelvin(celsius)
            print(f"Testing {celsius}°C to Kelvin: expected {expected}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertCelsiusToFahrenheit(self):
        test_cases =[(300.00, 572.00), (0.00, 32.00), (-40.00, -40.00), (100.00, 212.00), (-100.00, -148.00)]
        for celsius, expected in test_cases:
            result = convertCelsiusToFahrenheit(celsius)
            print(f"Testing {celsius}°C to Fahrenheit: expected {expected}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertFahrenheitToCelsius(self):
        test_cases =[(572.00, 300.00), (32.00, 0.00), (-40.00, -40.00), (212.00, 100.00), (-148.00, -100.00)]
        for fahrenheit, expected in test_cases:
            result = convertFahrenheitToCelsius(fahrenheit)
            print(f"Testing {fahrenheit}°F to Celsius: expected {expected}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertFahrenheitToKelvin(self):
        test_cases =[(572.00, 573.15), (32.00, 273.15), (-40.00, 233.15), (212.00, 373.15), (-148.00, 173.15)]
        for fahrenheit, expected in test_cases:
            result = convertFahrenheitToKelvin(fahrenheit)
            print(f"Testing {fahrenheit}°F to Kelvin: expected {expected}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertKelvinToCelsius(self):
        test_cases =[(573.15, 300.00), (273.15, 0.00), (233.15, -40.00), (373.15, 100.00), (173.15, -100.00)]
        for kelvin, expected in test_cases:
            result = convertKelvinToCelsius(kelvin)
            print(f"Testing {kelvin}K to Celsius: expected {expected}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertKelvinToFahrenheit(self):
        test_cases =[(573.15, 572.00), (273.15, 32.00), (233.15, -40.00), (373.15, 212.00), (173.15, -148.00)]
        for kelvin, expected in test_cases:
            result = convertKelvinToFahrenheit(kelvin)
            print(f"Testing {kelvin}K to Fahrenheit: expected {expected}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)


class TestRefactoredConversions(unittest.TestCase):
    """Test cases for Part IV refactored conversion function"""

    def test_convert_temperatures(self):
        """1. Check that all temperature conversions are working"""
        test_cases =[
            ("Celsius", "Kelvin", 0.0, 273.15),
            ("Celsius", "Fahrenheit", 0.0, 32.0),
            ("Fahrenheit", "Celsius", 32.0, 0.0),
            ("Fahrenheit", "Kelvin", 32.0, 273.15),
            ("Kelvin", "Celsius", 273.15, 0.0),
            ("Kelvin", "Fahrenheit", 273.15, 32.0)
        ]
        for from_u, to_u, val, expected in test_cases:
            result = convert(from_u, to_u, val)
            self.assertAlmostEqual(result, expected, places=2)

    def test_convert_distances(self):
        """2. Check that all distance conversions are working"""
        test_cases =[
            ("Miles", "Yards", 1.0, 1760.0),
            ("Miles", "Meters", 1.0, 1609.34),
            ("Yards", "Miles", 1760.0, 1.0),
            ("Yards", "Meters", 1.0, 0.9144),
            ("Meters", "Miles", 1609.34, 1.0),
            ("Meters", "Yards", 0.9144, 1.0)
        ]
        for from_u, to_u, val, expected in test_cases:
            result = convert(from_u, to_u, val)
            self.assertAlmostEqual(result, expected, places=2)

    def test_convert_same_unit(self):
        """3. Check that converting from one unit to itself returns the same value"""
        units = ["Celsius", "Fahrenheit", "Kelvin", "Miles", "Yards", "Meters"]
        for unit in units:
            self.assertAlmostEqual(convert(unit, unit, 100.0), 100.0, places=2)

    def test_incompatible_units(self):
        """4. Check that converting from incompatible units raises ConversionNotPossible"""
        with self.assertRaises(ConversionNotPossible):
            convert("Celsius", "Meters", 100)
            
        with self.assertRaises(ConversionNotPossible):
            convert("Yards", "Kelvin", 1)

        with self.assertRaises(ConversionNotPossible):
            convert("Pounds", "Ounces", 100)


if __name__ == "__main__":
    # Enable verbose mode to see detailed output
    #unittest.main(verbosity=2)
    unittest.main()