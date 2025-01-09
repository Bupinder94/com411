from process import DataProcessor
from tui import UserInterface

class DisneylandReviewAnalyser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.processor = DataProcessor(file_path)
        self.ui = UserInterface()
        self.is_running = True

    def start(self):
        self.ui.display_title("Disneyland Review Analyser")

        # Load dataset
        rows = self.processor.load_data()
        if rows > 0:
            self.ui.display_message(f"Dataset loaded successfully. Total rows: {rows}.")
        else:
            self.ui.display_message("Failed to load dataset. Exiting.")
            return

        # Main menu loop
        while self.is_running:
            choice = self.ui.display_menu()
            self.handle_menu_choice(choice)

    def handle_menu_choice(self, choice):
        if choice == 'A':
            self.ui.confirm_choice("A - View Data")
            # Placeholder for View Data functionality
        elif choice == 'B':
            self.ui.confirm_choice("B - Visualize Data")
            # Placeholder for Visualize Data functionality
        elif choice == 'X':
            self.ui.confirm_choice("X - Exit")
            self.is_running = False
        else:
            self.ui.invalid_choice()

if __name__ == "__main__":
    analyser = DisneylandReviewAnalyser("Disneyland_reviews.csv")
    analyser.start()
