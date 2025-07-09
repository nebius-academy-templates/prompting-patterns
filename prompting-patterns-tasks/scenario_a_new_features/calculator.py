#!/usr/bin/env python3
"""
Basic Calculator - Ready for New Features
==========================================

This is a working basic calculator that students can extend with new features.
Currently supports: add, subtract, multiply, divide

Practice Challenge: Use the "New Features" prompt pattern to add scientific functions
"""

class BasicCalculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def show_history(self):
        """Show calculation history"""
        if not self.history:
            print("No calculations yet")
        else:
            print("Calculation History:")
            for calc in self.history:
                print(f"  {calc}")
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
        print("History cleared")

def main():
    calc = BasicCalculator()
    
    print("Basic Calculator")
    print("Commands: add, subtract, multiply, divide, history, clear, quit")
    
    while True:
        try:
            command = input("\nEnter command: ").strip().lower()
            
            if command == "quit":
                break
            elif command == "history":
                calc.show_history()
            elif command == "clear":
                calc.clear_history()
            elif command in ["add", "subtract", "multiply", "divide"]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                
                if command == "add":
                    result = calc.add(a, b)
                elif command == "subtract":
                    result = calc.subtract(a, b)
                elif command == "multiply":
                    result = calc.multiply(a, b)
                elif command == "divide":
                    result = calc.divide(a, b)
                
                print(f"Result: {result}")
            else:
                print("Unknown command")
                
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main() 