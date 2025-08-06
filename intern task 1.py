
# calculator.py

def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    return x / y
def main():
    while True:
        print("\n--- Calculator Menu ---")
        print("1.Add (+)")
        print("2.Sub(-)")
        print("3.Mul(*)")
        print("4.Div(/)")
        print("5.Exit")
        choice = input("Choose an operation (1/2/3/4/5): ")
        if choice == '5':
            print("Tq for using cal,how can i help you!")
            break
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice, Please try again.")
            continue
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input,  Please enter numeric values.")
            continue
        if choice== '1':
            res=add(num1, num2)
        elif choice== '2':
            res=sub(num1, num2)
        elif choice== '3':
            res=mul(num1, num2)
        elif choice== '4':
            res=div(num1, num2)
        print("Result:",res)

if __name__ == "__main__":
    main()
