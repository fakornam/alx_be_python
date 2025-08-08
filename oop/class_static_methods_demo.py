class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Performs addition without needing class or instance context."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Performs multiplication and references a class-level attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b