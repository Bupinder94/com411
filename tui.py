class UserInterface:
    @staticmethod
    def display_title(title):
        dashes = "-" * len(title)
        print(dashes)
        print(title)
        print(dashes)

    @staticmethod
    def display_menu():
        print("\nPlease enter the letter which corresponds with your desired menu choice:")
        print("[A] View Data")
        print("[B] Visualize Data")
        print("[X] Exit")
        return input("Your choice: ").strip().upper()

    @staticmethod
    def confirm_choice(choice):
        print(f"You have chosen option {choice}.")

    @staticmethod
    def invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_message(message):
        print(message)
