import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_result

class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if the generated operator is one of '+', '-', or '*'
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, ['+', '-', '*'])

    def test_function_C(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (3, 4, '-', '3 - 4', -1),
            (2, 6, '*', '2 * 6', 12),
            # Add more test cases here
            (7, 3, '+', '7 + 3', 10),
            (10, 2, '*', '10 * 2', 20),
            (8, 4, '-', '8 - 4', 4),
        ]

        for num_1, num_2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate_result(num_1, num_2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
