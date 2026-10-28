def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def menu():
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("Q. Quit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Select an option: ").strip()
        if choice.lower() == 'q':
            break
        if choice in ['1', '2']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
        else:
            print("Invalid choice!")
