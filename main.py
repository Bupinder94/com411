from process import DataProcessor
from tui import UserInterface
from visual import Visualizer
from exporter import DataExporter

class DisneylandReviewAnalyser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.processor = DataProcessor(file_path)
        self.ui = UserInterface()
        self.visualizer = Visualizer()
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
            self.view_data()
        elif choice == 'B':
            self.ui.confirm_choice("B - Visualize Data")
            self.visualize_data()
        elif choice == 'C':
            self.ui.confirm_choice("C - Export Data")
            self.export_data()
        elif choice == 'X':
            self.ui.confirm_choice("X - Exit")
            self.is_running = False
        else:
            self.ui.invalid_choice()

    def view_data(self):
        sub_choice = self.ui.display_view_data_menu()
        if sub_choice == 'A':
            park_name = input("Enter the park name: ")
            reviews = self.processor.filter_reviews_by_park(park_name)
            self.ui.display_reviews(reviews)
        elif sub_choice == 'B':
            park_name = input("Enter the park name: ")
            location = input("Enter the reviewer location: ")
            count = self.processor.count_reviews_by_location(park_name, location)
            self.ui.display_message(f"Number of reviews: {count}")
        elif sub_choice == 'C':
            park_name = input("Enter the park name: ")
            year = int(input("Enter the year: "))
            avg_rating = self.processor.average_rating_by_year(park_name, year)
            self.ui.display_message(f"Average rating: {avg_rating:.2f}")
        elif sub_choice == 'D':
            summary = self.processor.average_score_per_location()
            self.ui.display_summary(summary)
        else:
            self.ui.invalid_choice()

    def visualize_data(self):
        sub_choice = self.ui.display_visualization_menu()
        if sub_choice == 'A':
            park_reviews = {park: len(self.processor.filter_reviews_by_park(park)) for park in set(row['Branch'] for row in self.processor.data)}
            self.visualizer.plot_pie_chart(park_reviews, "Most Reviewed Parks")
        elif sub_choice == 'B':
            park_name = input("Enter the park name: ")
            location_ratings = {location: self.processor.count_reviews_by_location(park_name, location) for location in set(row['Reviewer_Location'] for row in self.processor.data if row['Branch'] == park_name)}
            self.visualizer.plot_bar_chart(location_ratings, "Park Ranking by Nationality", "Location", "Number of Reviews")
        elif sub_choice == 'C':
            park_name = input("Enter the park name: ")
            month_ratings = {}
            for row in self.processor.data:
                if row['Branch'] == park_name:
                    month = row['Year_Month']
                    if month not in month_ratings:
                        month_ratings[month] = []
                    month_ratings[month].append(int(row['Rating']))
            avg_month_ratings = {month: sum(ratings)/len(ratings) for month, ratings in month_ratings.items()}
            self.visualizer.plot_bar_chart(avg_month_ratings, "Most Popular Month by Park", "Month", "Average Rating")
        else:
            self.ui.invalid_choice()

    def export_data(self):
        exporter = DataExporter(self.processor.data)
        export_choice = self.ui.display_export_options()
        if export_choice == '1':
            exporter.export_to_txt("exported_data.txt")
            self.ui.display_message("Data exported to exported_data.txt")
        elif export_choice == '2':
            exporter.export_to_csv("exported_data.csv")
            self.ui.display_message("Data exported to exported_data.csv")
        elif export_choice == '3':
            exporter.export_to_json("exported_data.json")
            self.ui.display_message("Data exported to exported_data.json")
        else:
            self.ui.invalid_choice()

if __name__ == "__main__":
    analyser = DisneylandReviewAnalyser("Disneyland_reviews.csv")
    analyser.start()
