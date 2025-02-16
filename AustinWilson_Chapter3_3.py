#imports functools reduce in order to properly analyze lists
from functools import reduce
#retrieve user expenses through a while True loop that completes when :"quit" is entered
def get_expenses():
#creates a list for expenses to be inputted
    expenses = []
    while True:
        expense_name = input("Enter name of expense or enter 'quit' to view results: ")
        if expense_name.lower() == 'quit':
            break
        expense_amount = float(input(f"Enter expense amount for {expense_name}: "))
        #uses a tuple to group together the name and amounts.
        expenses.append((expense_name, expense_amount))
    return expenses

def expense_analysis(expenses):
    total_expense = reduce(lambda acc, expense: acc + expense[1], expenses, 0)

    highest_expense = reduce(lambda acc, expense: expense if expense[1] > acc[1] else acc, expenses)

    lowest_expense = reduce(lambda acc, expense: expense if expense[1] < acc[1] else acc, expenses)

    return total_expense, highest_expense, lowest_expense

def main():
    expenses = get_expenses()
    if not expenses:
        print("No expenses entered.")
        return
    total, highest, lowest = expense_analysis(expenses)

    print (f"\nTotal Monthly Expense: ${total:.2f}")
    print (f"\nHighest Monthly Expense: {highest[0]} - ${highest[1]:.2f}")
    print (f"\nLowest Monthly Expense: {lowest[0]} - ${lowest[1]:.2f}")

if __name__ == "__main__":
    main()
input('press enter to exit')