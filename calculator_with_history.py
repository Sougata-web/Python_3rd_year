history_file = 'C:/Users/SOUGATA/OneDrive/Desktop/programs/3rd_year/Python/history.txt'

def show_history():
    with open(history_file, 'r') as file:
        lines = file.readlines()
        if not lines:
            print("No history found.")
        else:
            for line in reversed(lines):
                print(line.strip())

def clear_history():
    open(history_file, 'w').close()
    print('History Cleared')

def save_to_history(equation, result):
    with open(history_file, 'a') as file:
        file.write(f"{equation} = {result}\n")
    print('History Saved!')

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Invalid operator"

def calculator():
    while True:
        hey = input("Enter equation or command (show, clear, exit): ").strip().lower()

        if hey == "show":
            show_history()
            continue
        elif hey == "clear":
            clear_history()
            continue
        elif hey == "exit":
            print("Calculator closed.")
            break

        try:
            num1, operator, num2 = hey.split()
            num1 = float(num1)
            num2 = float(num2)

            result = calculate(num1, operator, num2)
            print("Result:", result)

            if isinstance(result, (int, float)):
                save_to_history(hey, result)

        except ValueError:
            print("Invalid input format. Use: number operator number (e.g. 2 + 3)")

if __name__ == '__main__':
    calculator()
