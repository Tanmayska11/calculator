

class Calculator:
    def add(self, a, b):
        return f"Addition of {a} and {b} is {a + b}"

    def subtract(self, a, b):
        return f"Substraction of {a} and {b} is {a - b}"

    def multiply(self, a, b):
        return f"Multiplication of {a} and {b} is {a * b}"

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        else:
            return f"Dividion of {a} and {b} is {a / b}"
