class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def get_positive_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Amount must be positive. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        
        if action == 'exit':
            print("Goodbye!")
            break
        elif action == 'deposit':
            amount = get_positive_float_input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_positive_float_input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
