# basic_calculator.py

def add(a, b):
    """Addition function"""
    return a + b

def subtract(a, b):
    """Subtraction function"""
    return a - b

def multiply(a, b):
    """Multiplication function"""
    return a * b

def divide(a, b):
    """Division function"""
    if b == 0:
        return "Error! Division by zero."
    return a / b

def main():
    print("🧮 Simple Calculator")
    print("=" * 25)
    
    while True:
        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Goodbye! 👋")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("❌ Invalid input! Please enter numbers only.")
                continue
            
            if choice == '1':
                result = add(num1, num2)
                print(f"✅ Result: {num1} + {num2} = {result}")
            
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"✅ Result: {num1} - {num2} = {result}")
            
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"✅ Result: {num1} * {num2} = {result}")
            
            elif choice == '4':
                result = divide(num1, num2)
                print(f"✅ Result: {num1} / {num2} = {result}")
        else:
            print("❌ Invalid input! Please enter 1-5")

if __name__ == "__main__":
    main()