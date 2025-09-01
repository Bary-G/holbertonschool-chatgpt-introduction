class Checkbook:
    """
    A simple checkbook class that allows deposits, withdrawals,
    and viewing the current balance.
    """

    def __init__(self):
        """
        Initialize a new Checkbook instance with a balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Parameters:
        - amount (float): The amount to deposit. Must be positive.
        """
        self.balance += amount
        print(f"✅ Deposited ${amount:.2f}")
        self.get_balance()

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook if sufficient funds exist.

        Parameters:
        - amount (float): The amount to withdraw. Must be positive and <= current balance.
        """
        if amount > self.balance:
            print("⚠️ Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"✅ Withdrew ${amount:.2f}")
            self.get_balance()

    def get_balance(self):
        """
        Print the current balance in the checkbook.
        """
        print(f"💰 Current Balance: ${self.balance:.2f}")


def main():
    """
    Main function to interact with the user. Provides a simple CLI
    for depositing, withdrawing, checking balance, or exiting.
    """
    cb = Checkbook()  # Create a new checkbook instance
    
    while True:
        # Ask the user what they want to do
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        
        if action == 'exit':
            print("👋 Goodbye!")
            break  # Exit the loop and end the program

        elif action in ['deposit', 'withdraw']:
            try:
                # Prompt the user to enter the amount
                amount = float(input("Enter the amount: $"))
                if amount <= 0:
                    print("⚠️ Please enter a positive amount.")
                    continue  # Skip the rest of the loop and prompt again

                # Perform the deposit or withdrawal
                if action == 'deposit':
                    cb.deposit(amount)
                else:
                    cb.withdraw(amount)

            except ValueError:
                # Handle non-numeric input
                print("⚠️ Invalid input. Please enter a numeric value.")

        elif action == 'balance':
            cb.get_balance()

        else:
            # Catch any invalid commands
            print("❌ Invalid command. Please try again.")


# Only run the main function if this script is executed directly
if __name__ == "__main__":
    main()
