import unittest

# Assuming the functions are in a module named 'age_calculator'
from calc_age import calculate_year_of_100th_birthday

class TestAgeCalculator(unittest.TestCase):
    
    def test_calculate_year_of_100th_birthday(self):
        # User == 0 years old
        self.assertEqual(calculate_year_of_100th_birthday("Alice", 0), 2124)
        
        # User == 50 years old
        self.assertEqual(calculate_year_of_100th_birthday("Bob", 50), 2074)
        
        # User == 99 years old
        self.assertEqual(calculate_year_of_100th_birthday("Charlie", 99), 2025)
        
        # User == 100 years old
        self.assertEqual(calculate_year_of_100th_birthday("Dave", 100), 2024)
        
        # User > 100 years old
        self.assertEqual(calculate_year_of_100th_birthday("Eve", 105), 2019)

if __name__ == "__main__":
    unittest.main()

        