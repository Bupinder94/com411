# tui.py
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
        print("[C] Export Data")
        print("[X] Exit")
        return input("Your choice: ").strip().upper()

    @staticmethod
    def display_view_data_menu():
        print("\nPlease enter one of the following options:")
        print("[A] View Reviews by Park")
        print("[B] Number of Reviews by Park and Reviewer Location")
        print("[C] Average Score per Year by Park")
        print("[D] Average Score per Park by Reviewer Location")
        return input("Your choice: ").strip().upper()

    @staticmethod
    def display_visualization_menu():
        print("\nPlease enter one of the following options:")
        print("[A] Most Reviewed Parks")
        print("[B] Park Ranking by Nationality")
        print("[C] Most Popular Month by Park")
        return input("Your choice: ").strip().upper()

    @staticmethod
    def display_export_options():
        print("\nSelect the format for exporting data:")
        print("[1] TXT")
        print("[2] CSV")
        print("[3] JSON")
        return input("Your choice: ").strip()

    @staticmethod
    def confirm_choice(choice):
        print(f"You have chosen option {choice}.")

    @staticmethod
    def invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_reviews(reviews):
        for review in reviews:
            print(review)

    @staticmethod
    def display_summary(summary):
        for key, value in summary.items():
            print(f"{key}: {value}")
