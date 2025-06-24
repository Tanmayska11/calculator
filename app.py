from calculator import Calculator

class CalculatorApp:
    def __init__(self):
        self.calculator = Calculator()

    def run(self):
        while True:
            print("\n**************  Calculator **************")
            print("\n--- Choose the operation ---\n")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")

            operations = input("\n choose your Operation (1 to 5): ")

            if operations == '5':
                print("Exiting calculator. Goodbye!")
                break

            if operations not in ['1', '2', '3', '4']:
                print("Invalid choice. Try again.")
                continue

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if operations == '1':
                result = self.calculator.add(num1, num2)
            elif operations == '2':
                result = self.calculator.subtract(num1, num2)
            elif operations == '3':
                result = self.calculator.multiply(num1, num2)
            elif operations == '4':
                result = self.calculator.divide(num1, num2)

            print(f"Result: {result}")


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
