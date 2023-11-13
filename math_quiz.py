import random


def generate_random_integer(min_value, max_value):
    """
    Generates a random integer between min_value and max_value (inclusive).
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generates a random mathematical operator: '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def calculate_result(num_1, num_2, operator):
    """
    Calculates the result of a mathematical operation and returns a tuple (problem, answer).
    """
    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2
    else:
        result = num_1 * num_2

    problem = f"{num_1} {operator} {num_2}"
    return problem, result


def math_quiz():
    """
    Conducts a math quiz game.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = calculate_result(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = 0  # Assign a default value to prevent crashing.

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
