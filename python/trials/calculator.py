class Calculator:
    def __init__(self, number1, number2, operand):
        self.number1 = number1
        self.number2 = number2
        self.operand = operand

    def calculate(self):
        result = 0
        match self.operand:
            case '+':
                result = self.number1 + self.number2
            case '-':
                result = self.number1 - self.number2
            case '*':
                result = self.number1 * self.number2
            case '/':
                result = self.number1 / self.number2
        return result

    def __str__(self):
        return f"{self.number1} {self.number2}"

calculator = Calculator(2,3,'*')
print(calculator.calculate())