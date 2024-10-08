import unittest

# Importing the conversion functions and exception
from conversions import (
    convertCelsiusToKelvin, 
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit
)
from conversions import convert, ConversionNotPossible


class TestCelsiusConversions(unittest.TestCase):
    """Test cases for Celsius to Kelvin and Fahrenheit conversions"""

    def test_convertCelsiusToKelvin(self):
        """Test conversion from Celsius to Kelvin with multiple test cases"""
        test_cases = [
            (300.00, 573.15),
            (0.00, 273.15),
            (-273.15, 0.00),
            (100.00, 373.15),
            (-100.00, 173.15)
        ]
        for celsius, expected_kelvin in test_cases:
            result = convertCelsiusToKelvin(celsius)
            print(f"Testing {celsius}°C to Kelvin: expected {expected_kelvin}, got {result}")
            self.assertAlmostEqual(result, expected_kelvin, places=2)  # Allow slight differences due to floating-point precision
            # Debugging in case of mismatched result
            #if not (abs(result - expected_kelvin) <= 0.01):
            #    print(f"DEBUG: Conversion failed for {celsius}°C. Expected {expected_kelvin}, got {result}")

    def test_convertCelsiusToFahrenheit(self):
        """Test conversion from Celsius to Fahrenheit with multiple test cases"""
        test_cases = [
            (300.00, 572.00),
            (0.00, 32.00),
            (-40.00, -40.00),
            (100.00, 212.00),
            (-100.00, -148.00)
        ]
        for celsius, expected_fahrenheit in test_cases:
            result = convertCelsiusToFahrenheit(celsius)
            print(f"Testing {celsius}°C to Fahrenheit: expected {expected_fahrenheit}, got {result}")
            self.assertAlmostEqual(result, expected_fahrenheit, places=2)
            # Debugging in case of mismatched result
            #if not (abs(result - expected_fahrenheit) <= 0.01):
            #    print(f"DEBUG: Conversion failed for {celsius}°C. Expected {expected_fahrenheit}, got {result}")


class TestRefactoredConversions(unittest.TestCase):
    """Test cases for refactored conversion function that supports multiple units"""

    def test_convert_temperatures(self):
        """Test temperature conversions between Celsius, Fahrenheit, and Kelvin"""
        self.assertAlmostEqual(convert("Celsius", "Kelvin", 0), 273.15, places=2)
        self.assertAlmostEqual(convert("Kelvin", "Fahrenheit", 0), -459.67, places=2)
        self.assertAlmostEqual(convert("Fahrenheit", "Celsius", 32), 0, places=2)

    def test_convert_distances(self):
        """Test distance conversions between Miles, Yards, and Meters"""
        self.assertAlmostEqual(convert("Miles", "Meters", 1), 1609.34, places=2)
        self.assertAlmostEqual(convert("Yards", "Miles", 1760), 1, places=2)

    def test_convert_same_unit(self):
        """Test that converting a unit to itself returns the same value"""
        self.assertEqual(convert("Celsius", "Celsius", 100), 100)
        self.assertEqual(convert("Meters", "Meters", 1), 1)

    def test_incompatible_units(self):
        """Test that converting between incompatible units raises an exception"""
        with self.assertRaises(ConversionNotPossible):
            convert("Celsius", "Meters", 100)

        with self.assertRaises(ConversionNotPossible):
            convert("Yards", "Kelvin", 1)


if __name__ == "__main__":
    # Enable verbose mode to see detailed output
    #unittest.main(verbosity=2)
    unittest.main()