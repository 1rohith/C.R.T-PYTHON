class ATM:
    def __init__(self):
        self.accounts = {
            'rupay': 2000,
            'visa': 5000,
            'mastercard': 8499
        }

    def validate_user(self, username, password):
        # Simple validation, replace with your authentication logic
        if username == "user" and password == "pass":
            return True
        else:
            return False

    def check_balance(self, card_type):
        return self.accounts[card_type]

    def withdraw_cash(self, card_type, amount):
        if amount <= self.accounts[card_type]:
            self.accounts[card_type] -= amount
            return True
        else:
            print("Limit is crossed.")
            return False

    def deposit_cash(self, card_type, amount):
        self.accounts[card_type] += amount

    def mini_statement(self):
        # Implement mini statement logic
        pass


def main():
    atm = ATM()

    print("Welcome to the ATM system")
    print("Please select your card type: ")
    print("1. RuPay\n2. Visa\n3. MasterCard")

    card_type = input("Enter your card type: ").lower()

    if card_type in atm.accounts:
        print("Card type accepted.")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if atm.validate_user(username, password):
            print("Authentication successful!")
            while True:
                print("\nChoose an option:")
                print("1. Check Balance")
                print("2. Cash Withdrawal")
                print("3. Cash Deposit")
                print("4. Mini Statement")
                print("5. Exit")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    print("Your current balance is:", atm.check_balance(card_type))
                elif choice == 2:
                    amount = int(input("Enter the amount to withdraw: "))
                    if atm.withdraw_cash(card_type, amount):
                        print("Withdrawal successful. Please take your cash.")
                    else:
                        print("Withdrawal failed.")
                elif choice == 3:
                    amount = int(input("Enter the amount to deposit: "))
                    atm.deposit_cash(card_type, amount)
                    print("Deposit successful.")
                elif choice == 4:
                    atm.mini_statement()
                elif choice == 5:
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Authentication failed. Please try again.")

    else:
        print("Invalid card type.")

if __name__ == "__main__":
    main()
